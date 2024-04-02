from app.services import  create_stripe_checkout_session, send_payment_details_to_flight_inventory, send_payment_details_to_users,send_payment_details_to_rabbitmq


# passing data to stripe api microservice test [PASSED]
# product_description = "flight XYZ456"
# unit_amount = 765
# points_used = "200"
# stripe_result = create_stripe_checkout_session(product_description, unit_amount, points_used)
# print(stripe_result)

# passing data to flight inventory microservice test [need to test the url]
# flight_data = {
#     "user_id": "user 123456789",
#     "flight_id": "flight ABC123",
#     "seat_number": ["A1", "B2", "A4"]
# }  
# send_payment_details_to_flight_inventory(flight_data)

# passing data to users microservice test  [need to test the url]
# user_data = {
#     "user_id": "user 0123456789",
#     "flight_id": "flight ABC123",
#     "loyalty_points": 765
# }
# send_payment_details_to_users(user_data)

# # passing data to transaction microservice test [PASSED]
# transaction_data = {
#     "user_id": "user 4444",
#     "type": "P",
#     "payment_amt": 444.40
# }
# send_payment_details_to_rabbitmq("payment_topic", "topic", "Transactions", "payment.trans", transaction_data)

# # passing data to notification microservice test [PASSED]
# confirmation_data = {
#     "user_email": "jiayenbeh@gmail.com",
#     "msg_type": "P",
#     "payment_data": "888.80"
# }
# send_payment_details_to_rabbitmq("payment_topic", "topic", "Notification", "payment.noti", confirmation_data)

# # passing data to error microservice test
stripe_result= {
    "code": '500',
    "data": "stripe_result: Payment failed",
    "message": "stripe failure sent for error handling."
}
send_payment_details_to_rabbitmq("payment_topic", "topic", "Error", "stripe.error", stripe_result)
