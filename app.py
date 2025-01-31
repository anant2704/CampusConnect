from bson import ObjectId
from flask import Flask, jsonify, redirect, render_template, request, url_for, flash
from flask_cors import CORS
from pymongo import MongoClient
import urllib.parse
import json
import os
from config import Config

app = Flask(__name__)
app.config.from_object(Config)  # Load configuration from Config class

# Alternatively, you can set a fixed secret key
# app.secret_key = 'your_secret_key_here'

CORS(app)

# Connect to MongoDB

username = urllib.parse.quote_plus("dahatondeprachi1")
password = urllib.parse.quote_plus("Prachi@1234")  # Encodes special characters

client = MongoClient(f"mongodb+srv://{username}:{password}@cluster0.am4ct.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["community_platform"]

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/login")
def login():    
    return render_template("login.html")

@app.route("/hackathons")
def hackathons():
    hackathons = list(db.hackathons.find({}, {"_id": 0}))  # Fetch all fields
    return render_template("hackathons.html", hackathons=hackathons)

@app.route("/hackathon/<hackathon_name>")
def hackathon_details(hackathon_name):
    hackathon = db.hackathons.find_one({"name": hackathon_name}, {"_id": 0})
    if hackathon:
        return render_template("hackathon_details.html", hackathon=hackathon)
    else:
        return "Hackathon not found", 404

# clubs
@app.route("/clubs")
def clubs():
    clubs = list(db.clubs.find({}, {"_id": 0}))  # Fetch all clubs
    return render_template("clubs.html", clubs=clubs)

@app.route("/club/<club_name>")
def club_details(club_name):
    club = db.clubs.find_one({"name": club_name}, {"_id": 0})
    if club:
        return render_template("club_details.html", club=club)
    else:
        return "Club not found", 404

@app.route("/add_club", methods=["POST"])
def add_club():
    data = request.json
    club_name = data.get("name")
    club_description = data.get("description")
    club_features = data.get("features")
    club_why_join = data.get("whyJoin")
    club_members = data.get("members")

    if not club_name or not club_description or not club_features or not club_why_join or not club_members:
        return jsonify({"success": False, "error": "Missing fields"}), 400

    existing_club = db.clubs.find_one({"name": club_name})
    if existing_club:
        return jsonify({"success": False, "error": "Club already exists"}), 400

    new_club = {
        "name": club_name,
        "description": club_description,
        "features": club_features,
        "whyJoin": club_why_join,
        "members": int(club_members)
    }
    db.clubs.insert_one(new_club)

    return jsonify({"success": True})






# flatmates

@app.route("/flatmates", methods=["GET", "POST"])
def flatmates():
    if request.method == "POST":
        # Get form data
        name = request.form.get("name")
        location = request.form.get("location")
        rent = request.form.get("rent")
        flat_size = request.form.get("flat_size")
        occupancy_needed = request.form.get("occupancy_needed")
        area = request.form.get("area")
        facilities = request.form.get("facilities")

        # Create new flatmate document
        new_flatmate = {
            "name": name,
            "location": location,
            "rent": rent,
            "flat_size": flat_size,
            "occupancy_needed": occupancy_needed,
            "area": area,
            "facilities": facilities
        }

        # Insert into MongoDB
        db.flatmates.insert_one(new_flatmate)
        flash("Flatmate added successfully!")
        return redirect(url_for('flatmates'))

    flatmates = list(db.flatmates.find({}, {"_id": 0}))  # Fetch data from MongoDB
    return render_template("flatmates.html", flatmates=flatmates)

@app.route("/flatmate/<flatmate_name>")
def flatmate_details(flatmate_name):
    flatmate = db.flatmates.find_one({"name": flatmate_name}, {"_id": 0})
    if flatmate:
        return render_template("flatmate_details.html", flatmate=flatmate)
    else:
        return "Flatmate not found", 404

@app.route("/events")
def events():
    events = list(db.events.find({}, {"_id": 0}))  # Fetch data from MongoDB
    return render_template("events.html", events=events)

@app.route("/add_event", methods=["POST"])
def add_event():
    if request.method == "POST":
        # Get form data
        name = request.form.get("name")
        date = request.form.get("date")
        venue = request.form.get("venue")
        description = request.form.get("description")
        link = request.form.get("link")
        sponsored_by = request.form.get("sponsored_by")

        # Create new event document
        new_event = {
            "name": name,
            "date": date,
            "venue": venue,
            "description": description,
            "link": link,
            "sponsored_by": sponsored_by
        }

        # Insert into MongoDB
        db.events.insert_one(new_event)
        flash("Event added successfully!")
        return redirect(url_for('events'))

@app.route("/addhackathon", methods=["GET", "POST"])
def add_hackathon():
    if request.method == "POST":
        # Get form data
        name = request.form.get("name")
        date = request.form.get("date")
        location = request.form.get("location")
        description = request.form.get("description")
        eligibility = request.form.get("eligibility")
        project_details = request.form.get("project_details")
        prize_pool = request.form.get("prize_pool")
        schedule = request.form.get("schedule")  # Now just a date

        # Create new hackathon document
        new_hackathon = {
            "name": name,
            "date": date,
            "location": location,
            "description": description,
            "eligibility": eligibility,
            "project_details": project_details,
            "prize_pool": prize_pool,
            "schedule": schedule  # Only the date
        }

        # Insert into MongoDB
        db.hackathons.insert_one(new_hackathon)
        flash("Hackathon added successfully!")
        return redirect(url_for('hackathons'))

    return render_template("addhackathon.html")

@app.route("/event/<event_name>")
def event_details(event_name):
    event = db.events.find_one({"name": event_name}, {"_id": 0})
    if event:
        return render_template("event_details.html", event=event)
    else:
        return "Event not found", 404

if __name__ == "__main__":
    app.run(debug=True)
