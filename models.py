from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from config import db
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    pseudo = db.Column(db.String(50))
    ip_address = db.Column(db.String(15))
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))

    def __repr__(self):
        return f'<Message {self.id}>'

class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    members = db.relationship('Member', backref='group', lazy=True)
    messages = db.relationship('Message', backref='group', lazy=True)

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)
    ip_address = db.Column(db.String(15), nullable=False)
    
