import graphene
from graphene import ObjectType, String, Int, List, Field
from bson import ObjectId
from pymongo import MongoClient
from app import db

# client = MongoClient('localhost', port=27017)
# db = client['accom_inventory'] 

class AddressType(graphene.ObjectType):
    street = graphene.String()
    city = graphene.String()
    state = graphene.String()
    zip = graphene.String() 

class RoomType(graphene.ObjectType):
    _id = graphene.String()
    type = graphene.String()
    max_occupancy = graphene.Int()
    description = graphene.String()
    price_per_night = graphene.Float()
    is_available = graphene.Boolean()
    id = graphene.ID()

class HotelType(graphene.ObjectType):
    rooms = graphene.List(RoomType)
    id = graphene.ID()
    hotelName = graphene.String()  # Maps to 'hotel_name' in your database if using automatic resolution
    locationNear = graphene.String()  # Maps to 'location_near' in your database
    address = graphene.Field(AddressType)
    rooms = graphene.List(RoomType)

class Query(graphene.ObjectType):
    all_accoms = List(HotelType)
    available_rooms = graphene.List(HotelType, origin=graphene.String(required=True), pax=graphene.Int(required=True))

    def resolve_available_rooms(self, info, origin, pax):
        print(origin)
        filter_criteria = {"location_near": origin, "rooms": {"$elemMatch": {"is_available": True}}}
        # filter_criteria = {"location_near": origin}
        hotels = db['hotel'].find(filter_criteria)
        result = []

        total_occupancy = 0
        accumulated_rooms = []
        fulfilled = False

        for hotel in hotels:
            print(hotel)
            # Sort rooms by max_occupancy in ascending order to prioritize filling up to pax with smaller rooms first
            # sorted_rooms = sorted(hotel['rooms'], key=lambda room: room['max_occupancy'])
            for room in hotel['rooms']:
                if room['is_available']:
                    # Assuming each room document in MongoDB has an '_id' field:
                    room_with_id = room.copy()  # Copy the room dict to avoid mutating the original
                    accumulated_rooms.append(room_with_id)
                    total_occupancy += room['max_occupancy']
                if pax < total_occupancy:
                    fulfilled = True
                    break
            
            # Create a new hotel document with the filtered rooms                   
            hotel_data = {
                'id': str(hotel['_id']),
                'hotelName': str(hotel['hotel_name']),
                'address': hotel['address'],
                'rooms': accumulated_rooms,  # Use the filtered list of rooms
            }
            result.append(hotel_data)

            if fulfilled:
                break
        
        return result
    
