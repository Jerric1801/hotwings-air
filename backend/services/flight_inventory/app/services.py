from app import db
from bson.objectid import ObjectId

def update_seats(seat_id, seats):
    try:
        print("seats", seats)
        print("seatID", seat_id)

        seating_plan_collection = db['seating__plan']

        for seat_number in seats:
            result = seating_plan_collection.update_one({
                '_id': ObjectId(seat_id),
                'seats.seat_number': seat_number 
            }, {
                '$set': {
                    'seats.$.available': False  
                }
            })

            if result.modified_count == 0:
                print(f"Seat {seat_number} not found or already marked unavailable")
            else:
                print("Seats updated succesfully")
                return True


    except Exception as e:  # Catch more specific exceptions if needed
        print("Failed to update Seating:", e)
        return False