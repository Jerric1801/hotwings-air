import pika
from bson import ObjectId
from flask import jsonify

def process_data(body):
    from app import db
    print(body)
    room_id = body['room_id']
    
    # Find the hotel document by ID
    hotels = db.hotels.find()

    for hotel in hotels:
        print(hotel)
        room = hotel['rooms']
        print(room)
        if str(room['_id']) == room_id:
            room['is_available'] = False
            return jsonify({"Success", "Room updated"}), 200
        
    return jsonify({"Failure", "Room not updated"}), 404
    

def callback(channel, method, properties, body):
    process_data(body)
    print(" [x] Received %r" % body)

def consume_amqp_messages(channel):
    try:
        channel.basic_consume(queue="accommodation", on_message_callback=callback, auto_ack=True)
        print('pricing microservice: Consuming from queue:', "update.accomodation")
        channel.start_consuming()
    
    except pika.exceptions.AMQPError as e:
        print(f"pricing microservice: Failed to connect: {e}") 

    except KeyboardInterrupt:
        print("pricing microservice: Program interrupted by user.")


# def consume_transaction():
#     connection = pika.BlockingConnection(pika.ConnectionParameters('host.docker.internal'))
#     channel = connection.channel()
#     channel.queue_declare(queue='accommodation', durable=True)
#     channel.basic_consume(queue='accommodation', on_message_callback=callback, auto_ack=False) 

#     print(' [*] Waiting for messages. To exit press CTRL+C')
#     channel.start_consuming()
