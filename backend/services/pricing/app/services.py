# import pika
# import json
# import os, sys
# from amqp_connection import create_connection, check_exchange

# def send_amqp_message(exchangename, exchangetype, microservice, routing_key, payload):
#     connection = create_connection() 
#     channel = connection.channel()

#     #if the exchange is not yet created, exit the program
#     if not check_exchange(channel, exchangename, exchangetype):
#         print(f"\nCreate the 'Exchange' before running the {microservice} microservice. \nExiting the program.")
#         sys.exit(0)  # Exit with a success status

#     message = json.dumps(payload)
#     print(message)

#     # Publish message to specific queue based on the routing_key
#     channel.basic_publish(exchange=exchangename, routing_key=f"{routing_key}", body=message, properties=pika.BasicProperties(delivery_mode = 2)) 

        
#     print(f"\n Message is published to the RabbitMQ Exchange under {microservice} and Activity_Log queue:", message)

#     # Return error
#     # return {
#     #     "code": 500,
#     #     "data": {f"{microservice}_error":message},
#     #     "message": f"Transmission of data to {microservice} microservice failure sent for error handling."
#     # }

# def process_data(body):
#     if(body.new_flight):
#         user_email = body.email
#         original_pricing = get_pricing(flight_number,seat_class)
#         new_pricing = get_pricing(flight_number,seat_class)
#         difference = new_pricing - original_pricing
#         if(new_pricing < original_pricing):
#             add_points = original_pricing - new_pricing
#             trans_payload = {
#                 "user_email": user_email,
#                 "type":"points",
#                 "amount": difference
#             }
#             user_payload = {
#                 "user_email": user_email,
#                 "amount": add_points
#             }
#             send_amqp_message("pricing_topic", "topic", "user", "pricing.user", user_payload)
#         trans_payload = {
#             "user_email": user_email,
#             "type":"points",
#             "amount": difference
#         }
#         send_amqp_message("pricing_topic", "topic", "transaction", "pricing.trans", trans_payload)

#     else:
#         points = get_pricing(flight_number,seat_class)
#         user_email = body.email
#         payload = {
#             "user_email":"",
#             "loyalty_points": points
#         }
#         send_amqp_message("pricing_topic", "topic", "transaction", "pricing.trans")
#         send_amqp_message("pricing_topic", "topic", "user", "pricing.user")

# def callback(channel, method, properties, body):
#     process_data(body)
#     print(" [x] Received %r" % body)

# def consume_amqp_messages(channel):
#     try:
#         channel.basic_consume(queue="test.queue", on_message_callback=callback, auto_ack=True)
#         print('pricing microservice: Consuming from queue:', "test.queue")
#         channel.start_consuming()
    
#     except pika.exceptions.AMQPError as e:
#         print(f"pricing microservice: Failed to connect: {e}") 

#     except KeyboardInterrupt:
#         print("pricing microservice: Program interrupted by user.")

# def get_pricing(flight_number, seat_class):
#     flight = Pricing.query.filter_by(flight_number=flight_number, seat_class=seat_class).first()
#     if flight:
#         price = flight.price
#         print(price)
#         return price