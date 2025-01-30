from flask import Flask, render_template
from flask_cors import CORS
from pymongo import MongoClient
import urllib.parse

app = Flask(__name__)
CORS(app)

# Connect to MongoDB

username = urllib.parse.quote_plus("dahatondeprachi1")
password = urllib.parse.quote_plus("Prachi@1234")  # Encodes special characters

client = MongoClient(f"mongodb+srv://{username}:{password}@cluster0.am4ct.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["community_platform"]

# Insert Sample Data Only if Collections are Empty
if db.hackathons.count_documents({}) == 0:
    db.hackathons.insert_many([
        {"name": "AI Hackathon", "date": "2025-03-20", "location": "Online"},
        {"name": "Cyber Security Challenge", "date": "2025-04-15", "location": "MIT College"}
    ])

if db.clubs.count_documents({}) == 0:
    db.clubs.insert_many([
        {"name": "Coding Club", "members": 150, "description": "A club for coding enthusiasts."},
        {"name": "Music Club", "members": 100, "description": "A club for music lovers."}
    ])

if db.flatmates.count_documents({}) == 0:
    db.flatmates.insert_many([
        {"name": "John Doe", "location": "NYC", "rent": "$500"},
        {"name": "Alice Smith", "location": "LA", "rent": "$600"}
    ])

if db.events.count_documents({}) == 0:
    db.events.insert_many([
        {"name": "Tech Fest", "date": "2025-05-10", "venue": "Main Auditorium"},
        {"name": "Entrepreneurship Summit", "date": "2025-06-05", "venue": "Conference Hall"}
    ])

print("Sample data inserted successfully!")

@app.route("/")
def home():
    return render_template("./frontend/index.html")
@app.route("/login")
def login():    
    return render_template("login.html")

@app.route("/hackathons")
def hackathons():
    hackathons = list(db.hackathons.find({}, {"_id": 0}))  # Fetch data from MongoDB
    return render_template("hackathons.html", hackathons=hackathons)

@app.route("/clubs")
def clubs():
    clubs = list(db.clubs.find({}, {"_id": 0}))  # Fetch data from MongoDB
    return render_template("clubs.html", clubs=clubs)

@app.route("/flatmates")
def flatmates():
    flatmates = list(db.flatmates.find({}, {"_id": 0}))  # Fetch data from MongoDB
    return render_template("flatmates.html", flatmates=flatmates)

@app.route("/events")
def events():
    events = list(db.events.find({}, {"_id": 0}))  # Fetch data from MongoDB
    return render_template("events.html", events=events)

if __name__ == "__main__":
    app.run(debug=True)