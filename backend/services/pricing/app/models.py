from app import db
from datetime import datetime

class Pricing(db.Model):
    __tablename__ = 'flight_pricing'
    pricing_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flight_number = db.Column(db.String(15), nullable=False)  # Consider a longer length
    seat_class = db.Column(db.String(15), nullable=False)
    price = db.Column(db.Float, nullable=False)
    created = db.Column(db.TIMESTAMP, default=datetime.utcnow, nullable=False)
    modified = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)