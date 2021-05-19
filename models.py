from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True) 
    email = db.Column(db.String(50), unique=True) 
    password = db.Column(db.String(80)) 
    ideal_weather = db.relationship('IdealWeather', backref='author')

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class IdealWeather(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    condition = db.Column(db.String(100), nullable=False)
    temp = db.Column(db.Integer)
    desc = db.Column(db.Text, nullable=False)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"IdealWeather('{self.condition}', '{self.temp}', '{self.desc}', '{self.date_added}')"
