from server.config import db
from datetime import datetime
# from server.models.location import Location
# from server.models.user import User

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gold_amount = db.Column(db.Integer, nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, onupdate=datetime.utcnow)