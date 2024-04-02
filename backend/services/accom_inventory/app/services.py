import pika
import json
import os, sys
from amqp_connection import create_connection, check_exchange
from models import Hotel, Room
from bson import ObjectId
from app import db

def process_data(body):
    room_ids = body['room_id']
    hotel_id = body['hotel_id']
    print(room_ids)
    
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
            print(f"{updated_count} room(s) availability updated.")
        else:
            print("No matching rooms found or already unavailable.")
    else:
        print("Hotel not found.")
    
    

def callback(channel, method, properties, body):
    process_data(body)
    print(" [x] Received %r" % body)

def consume_amqp_messages(channel):
    try:
        channel.basic_consume(queue="update.accomodation", on_message_callback=callback, auto_ack=True)
        print('pricing microservice: Consuming from queue:', "update.accomodation")
        channel.start_consuming()
    
    except pika.exceptions.AMQPError as e:
        print(f"pricing microservice: Failed to connect: {e}") 

    except KeyboardInterrupt:
        print("pricing microservice: Program interrupted by user.")