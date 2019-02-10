from server.config import db
from datetime import datetime

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    min_gold = db.Column(db.Integer, nullable=False)
    max_gold = db.Column(db.Integer, nullable=False)
    activities = db.relationship('Activity', backref="location", lazy=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, onupdate=datetime.utcnow)

    def __repr__(self):
        return "<Location %r>" % self.name