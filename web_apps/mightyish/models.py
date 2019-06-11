import os
import json
import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(
    basedir,
    'mightyish.db'
    )
db = SQLAlchemy(app)


class Progress(db.Model):
    player_id = db.Column(db.ForeignKey('player.player'), primary_key = True)
    game_id = db.Column(db.ForeignKey('game.id'), primary_key = True)
    device_id = db.Column(db.ForeignKey('devices.id'))
    timestamp = db.Column(db.DateTime)
    level = db.Column(db.Integer)
    score = db.Column(db.Integer)

    def __init__(self, player_id, game_id, device_id, timestamp, level, score):
        self.player_id = player_id
        self.game_id = game_id
        self.timestamp = timestamp
        self.device_id = device_id
        self.level = level
        self.score = score

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def to_dictionary(self):
        result = {
          "timestamp": self.timestamp.isoformat(),
          "deviceId": self.device_id,
          "score": self.score,
          "level": self.level,
          "gameId": self.game_id
        }
        return result


class Player(db.Model):
#    id = db.Column(db.Integer, primary_key=True)  # Would be a UUID in production
    player = db.Column(db.String(32))  # We'll just use this for now.
    created_timestamp = db.Column(db.DateTime)
    modified_timestamp = db.Column(db.DateTime)
    first_name = db.Column(db.String(32))
    last_name = db.Column(db.String(32))
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), primary_key = True)
    active = db.Column(db.Boolean)

    def __init__(self, player, customer_id):
        self.player = player
        self.created_timestamp = datetime.datetime.now()
        self.modified_timestamp = datetime.datetime.now()
        self.customer_id = customer_id

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_timestamp = db.Column(db.DateTime)
    modified_timestamp = db.Column(db.DateTime)
    first_name = db.Column(db.String(32))
    last_name = db.Column(db.String(32))
    customer_type = db.Column(db.String(4)) # Enums are DB dependent, so using string for now
    players = db.relationship ('Player', backref='Player')
    payments = db.relationship('Payment', backref='Payment')
    active = db.Column(db.Boolean)

    # skipping rest of this class


class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.Timestamp)
    customer = db.Column(db.ForeignKey('customer.id'))
    payment_method = db.Column(db.ForeignKey('paymentmethod.id'))
    amount = db.Column(db.integer(9)) # Number of cents charged.

    # skipping rest of this class


class PaymentMethod(db.Model):  # Wildly PCI Uncompliant
    id = db.Column(db.Integer, primary_key=True)
    created_timestamp = db.Column(db.DateTime)
    customer_id = db.Column(db.ForeignKey('customer.id'))
    payment_type = db.Column(db.String(32))
    card_number = db.Column(db.String(16))
    expiration_date = db.Column(db.Datetime)
    verification_number = db.Column(db.Integer(3))
    address = db.Column(db.ForeignKey('address.id'))
    active = db.Column(db.Boolean)

    # skipping rest of this class


class Address(db.Model):
    id = db.Column(db.Integer, primar_key=True)

    # skipping rest of this class


class Device(db.Model):
    id = db.Column(db.String(32), primary_key=True)

    # skipping rest of this class


class Game(db.Model):
    id = db.Column(db.String(32))

    # skipping rest of this class


if not (os.path.isfile(os.path.join(basedir, 'mightyish.db'))):
    db.create_all()
