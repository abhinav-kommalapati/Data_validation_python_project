from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ValidationHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120))
    mobile = db.Column(db.String(20))
    ip_address = db.Column(db.String(45))
    date = db.Column(db.String(20))
    validation_results = db.Column(db.JSON)
    ai_insights = db.Column(db.JSON)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    validations = db.relationship('ValidationHistory', backref='user', lazy=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow) 