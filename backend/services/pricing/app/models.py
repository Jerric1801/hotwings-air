from app import db
from datetime import datetime

class Pricing(db.Model):
    __tablename__ = 'pricing'

    flight_id = db.Column(db.String(10), primary_key=True)
    seat_class = db.Column(db.String(15), nullable=False)
    customer_id = db.Column(db.String(32), nullable=False)
    created = db.Column(db.TIMESTAMP, default=datetime.utcnow, nullable=False)
    modified = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)