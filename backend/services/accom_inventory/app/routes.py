from flask import jsonify, request
from app import app
from bson import ObjectId
import random
import graphene
from app.schema import Query
import json

@app.route('/test', methods=['POST'])
def test():
    if request.method == "POST":
        return jsonify({"success": 1}), 200


@app.route('/accommodation', methods=['POST'])
def graphql():
    if request.method == "POST":
        print("started")
        schema = graphene.Schema(query=Query)

        data = json.loads(request.get_json())
        origin = data.get('origin')

        query = '''
        query AvailableRooms($origin: String!, $pax: Int!) { 
            availableRooms(origin: $origin, pax: $pax) { 
                hotelName
                rooms { 
                    type 
                    maxOccupancy 
                    description 
                    pricePerNight 
                    isAvailable 
                    } 
                }
            }
        '''

        variables =  {
            "origin": origin,
            "pax": 10
        }

        result = schema.execute(
            query,
            variable_values = variables
        )

        # Preparing the response object
        response = {"data": result.data}
        print(response)
        if result.errors:
            # Formatting errors as a list of messages
            response['errors'] = [error.message for error in result.errors]

        return jsonify(response), 200