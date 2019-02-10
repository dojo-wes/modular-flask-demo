import re
from datetime import datetime
from server.config import app, db

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserHelper:
    def validate(self, form):
        errors = []
        if len(form['first_name']) < 2:
            errors.append('First name must be at least 2 characters long.')
        if len(form['last_name']) < 2:
            errors.append('First name must be at least 2 characters long.')
        if not EMAIL_REGEX.match(form['email']):
            errors.append('Email must be valid.')
        else:
            matching_emails = User.query.filter_by(email=form['email']).first()
            print("MATCHING EMAILS", matching_emails)
            if matching_emails:
                errors.append("Email already in use.")
        if len(form['password']) < 8:
            errors.append("Password must be at least 8 characters long.")

        return errors

    def create(self, form):


        User(
            first_name=form['first_name'],
            last_name=form['first_name'],
            email=form['first_name'],
        )

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    pw_hash = db.Column(db.String(500), nullable=False)
    activities = db.relationship('Activity', backref="user", lazy=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, onupdate=datetime.utcnow)
    helpers = UserHelper()

    def __repr__(self):
        return "<User %r>" % self.email

