import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(
    basedir,
    'logsworth.db')
db = SQLAlchemy(app)


class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime)
    message = db.Column(db.String)

    def __init__(self, timestamp, message):
        self.timestamp = timestamp
        self.message = message

    def __repr__(self):
        return "{} {}".format(self.timestamp.isoformat(), self.message)

if not (os.path.isfile(os.path.join(basedir, 'logsworth.db'))):
    db.create_all()
