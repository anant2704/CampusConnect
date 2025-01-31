from flask_pymongo import PyMongo
from flask import Flask

app = Flask(__name__)
app.config.from_object("config.Config")
mongo = PyMongo(app)

# Collections
hackathon_collection = mongo.db.hackathons
club_collection = mongo.db.clubs
flatmate_collection = mongo.db.flatmates
event_collection = mongo.db.events

