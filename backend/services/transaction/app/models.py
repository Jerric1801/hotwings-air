from datetime import datetime
import uuid

class TransactionLogEntry:
    def __init__(self, type, user_id, payment_amt=None, loyalty_points=None, price_difference=None):
        self.log_id = str(uuid.uuid4())
        self.date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.type = type
        self.user_id = user_id
        self.payment_amt = payment_amt
        self.loyalty_points = loyalty_points
        self.price_difference = price_difference
