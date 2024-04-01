from flask import jsonify, request
from app import app, db
from app import schema
from bson import ObjectId

@app.route('/graphql', methods=['POST'])
def graphql():
    data = request.get_json()
    query = data.get('query')
    variables = data.get('variables', {})

    result = schema.execute(
        query,
        variable_values=variables,
    )

    # Preparing the response object
    response = {"data": result.data}
    if result.errors:
        # Formatting errors as a list of messages
        response['errors'] = [error.message for error in result.errors]

    return jsonify(response)

@app.route('/hotels/<hotel_id>/rooms/availability', methods=['PUT'])
def update_rooms_availability(hotel_id):
    data = request.get_json()
    room_ids = data.get('room_ids', [])
    print(room_ids)
    
    try:
        # Convert hotel_id from string to ObjectId for querying
        hotel_object_id = ObjectId(hotel_id)
        
        # Initialize updated_count
        updated_count = 0

        # Find the hotel document by ID
        hotel = db.hotels.find_one({"_id": hotel_object_id})
        
        if hotel:
            # Iterate through the rooms to check if the room_id is in the provided list and is_available is True
            for room in hotel["rooms"]:
                if str(room['_id']) in room_ids and room['is_available'] == True:
                    room['is_available'] = False
                    updated_count += 1
            
            # If any room was updated, save the changes
            if updated_count > 0:
                db.hotels.update_one({"_id": hotel_object_id}, {"$set": {"rooms": hotel["rooms"]}})
                return jsonify({"success": True, "message": f"{updated_count} room(s) availability updated."}), 200
            else:
                return jsonify({"success": False, "message": "No matching rooms found or already unavailable."}), 404
        else:
            return jsonify({"success": False, "message": "Hotel not found."}), 404
    
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500