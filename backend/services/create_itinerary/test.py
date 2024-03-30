from app.services import  send_flight_details_to_search_flight, send_flight_details_to_search_accomodation, send_flight_details_to_custom_webpage, send_flight_details_to_rabbitmq

# passing old flight data to search flight complex mciroservice test
old_flight_data = {
    "flight_id" : "flight ABC123",
    "departure": "19:00",
    "arrival": "02:00",
    "origin": "SIN",
    "destination": "AUS", 
    "aircraft": "Boeing 123",
    "seat_number": ["A1", "B2", "A4"]
}
user_email = "jiayenbeh@gmail.com"
search_flight_result = send_flight_details_to_search_flight(old_flight_data, user_email)

# passing new flight data to search accommodation microservice test
new_flight_data = {
    "flight_id" : "flight XYZ789",
    "departure": "05:00",
    "arrival": "12:00",
    "origin": "SIN",
    "destination": "AUS", 
    "aircraft": "Boeing 456",
    "seat_number": ["A2", "B1", "A4"]
}  
send_flight_details_to_search_accomodation(new_flight_data)

# passing new flight data and accommodation data to create webpage microservice test 
accommodation = {
    "booking_ID": "12345678", 
    "user_ID": "user 234", 
    "room_ID": "room 786",
    "checkInDate": "20-03-24",
    "checkOutDate": "21-03-24",
    "total_amt": "200.20"

}
send_flight_details_to_custom_webpage(new_flight_data, accommodation, user_email)

# # passing data to error microservice test
stripe_result= {
    "code": '500',
    "data": "stripe_result: Payment failed",
    "message": "stripe failure sent for error handling."
}
send_flight_details_to_rabbitmq("payment_topic", "topic", "Error", "stripe.error", stripe_result)
