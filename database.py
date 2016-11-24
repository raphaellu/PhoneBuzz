from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os 
app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///calls.db'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['HEROKU_POSTGRESQL_CYAN_URL']
db = SQLAlchemy(app)


class Call(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(80))
    delay = db.Column(db.Integer)
    number = db.Column(db.Integer)
    time = db.Column(db.String(80))

    def __init__(self, phone, delay, number, time):
        self.phone = phone
        self.delay = delay
        self.number = number
        self.time = time

    def __repr__(self):
        return '<Phone>: ' + self.phone + ' <Delay>: ' + str(self.delay) + ' <Number>: ' + str(self.number) + ' <Time>: ' + self.time