from app.services import send_errors


stripe_result= {
    "code": '500',
    "data": "stripe_result: Payment failed",
    "message": "stripe failure sent for error handling."
}
send_errors("stripe_topic", "topic", "stripe", stripe_result)