import graphene
from graphene import ObjectType, String, Int, List, Field
from bson import ObjectId
from pymongo import MongoClient

client = MongoClient('localhost', port=27017)
db = client['accom_inventory'] 

class AddressType(graphene.ObjectType):
    street = graphene.String()
    city = graphene.String()
    state = graphene.String()
    zip = graphene.String() 

class RoomType(graphene.ObjectType):
    type = graphene.String()
    max_occupancy = graphene.Int()
    description = graphene.String()
    price_per_night = graphene.Float()
    is_available = graphene.Boolean()

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
        filter_criteria = {"location_near": origin, "rooms": {"$elemMatch": {"is_available": True}}}
        hotels = db.hotels.find(filter_criteria)
        result = []

        for hotel in hotels:
            # Sort rooms by max_occupancy in ascending order to prioritize filling up to pax with smaller rooms first
            sorted_rooms = sorted(hotel['rooms'], key=lambda room: room['max_occupancy'])
            # print(sorted_rooms)
            # Filter and accumulate rooms until the sum of max_occupancy meets/exceeds pax
            accumulated_rooms = []
            total_occupancy = 0
            for room in sorted_rooms:
                if room['is_available'] and total_occupancy < pax:
                    accumulated_rooms.append(room)
                    # print(accumulated_rooms)
                    total_occupancy += room['max_occupancy']
            
            # Create a new hotel document with the filtered rooms                   
            hotel_data = {
                'id': str(hotel['_id']),
                'hotelName': str(hotel['hotel_name']),
                'address': hotel['address'],
                'rooms': accumulated_rooms,  # Use the filtered list of rooms
            }
            result.append(hotel_data)
        
        return result