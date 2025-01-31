from bson import ObjectId
from flask import Flask, jsonify, redirect, render_template, request, url_for, flash, session
from flask_cors import CORS
from pymongo import MongoClient
import urllib.parse
import json
import os
from config import Config
from functools import wraps

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
# User model for the database
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the user exists and the password matches
        user = db.users.find_one({"username": username})
        if user and user['password'] == password:
            session['username'] = username  # Set session variable
            session['user_type'] = user['user_type']  # Set user type in session
            return redirect(url_for('index'))  # Redirect to index.html if successful
        else:
            return "Invalid credentials, please try again."

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove the username from the session
    return redirect(url_for('index'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        user_type = request.form['user_type']  # New field for user type

        # Insert the user data into the users collection in MongoDB
        db.users.insert_one({
            'name': name,
            'email': email,
            'username': username,
            'password': password,  # Make sure to handle passwords securely in a production environment
            'user_type': user_type  # Store user type
        })
        
        return redirect(url_for('login'))  # Redirect to login page after successful signup

    return render_template('signup.html')

# Decorator to check if user is admin
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session or session.get('user_type') != 'Admin':
            return "Access denied. Admins only.", 403
        return f(*args, **kwargs)
    return decorated_function

@app.route('/index')
def index():
    return render_template('index.html')

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
@admin_required  # Restrict access to Admins
def add_club():
    if request.method == "POST":
        # Get form data
        name = request.form.get("name")
        description = request.form.get("description")
        features = request.form.get("features")
        why_join = request.form.get("why_join")
        members = request.form.get("members")
        contact_details = request.form.get("contact_details")  # New field

        # Create new club document
        new_club = {
            "name": name,
            "description": description,
            "features": features,
            "why_join": why_join,
            "members": int(members),
            "contact_details": contact_details  # New field
        }

        # Insert into MongoDB
        db.clubs.insert_one(new_club)
        flash("Club added successfully!")

        # Redirect to clubs page and trigger modal
        return redirect(url_for('clubs', show_modal=True))  # Pass a flag to show the modal

    return render_template("clubs.html")  # Render clubs.html for GET requests

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
        gender = request.form.get("gender")
        contact_details = request.form.get("contact_details")  # New field

        # Create new flatmate document
        new_flatmate = {
            "name": name,
            "location": location,
            "rent": rent,
            "flat_size": flat_size,
            "occupancy_needed": occupancy_needed,
            "area": area,
            "facilities": facilities,
            "gender": gender,
            "contact_details": contact_details  # New field
        }

        # Insert into MongoDB
        db.flatmates.insert_one(new_flatmate)
        flash("Flatmate added successfully!")
        return redirect(url_for('flatmates'))

    flatmates = list(db.flatmates.find({}, {"_id": 0}))
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
@admin_required  # Restrict access to Admins
def add_event():
    if request.method == "POST":
        # Get form data
        name = request.form.get("name")
        date = request.form.get("date")
        venue = request.form.get("venue")
        description = request.form.get("description")
        link = request.form.get("link")
        sponsored_by = request.form.get("sponsored_by")
        contact_details = request.form.get("contact_details")  # New field

        # Create new event document
        new_event = {
            "name": name,
            "date": date,
            "venue": venue,
            "description": description,
            "link": link,
            "sponsored_by": sponsored_by,
            "contact_details": contact_details  # New field
        }

        # Insert into MongoDB
        db.events.insert_one(new_event)
        flash("Event added successfully!")

        # Redirect to events page and trigger modal
        return redirect(url_for('events', show_modal=True))  # Pass a flag to show the modal

    return render_template("events.html")  # Render events.html for GET requests

@app.route("/add_hackathon", methods=["GET", "POST"])
@admin_required  # Restrict access to Admins
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
        schedule = request.form.get("schedule")
        contact_details = request.form.get("contact_details")  # New field

        # Create new hackathon document
        new_hackathon = {
            "name": name,
            "date": date,
            "location": location,
            "description": description,
            "eligibility": eligibility,
            "project_details": project_details,
            "prize_pool": prize_pool,
            "schedule": schedule,
            "contact_details": contact_details  # New field
        }

        # Insert into MongoDB
        db.hackathons.insert_one(new_hackathon)
        flash("Hackathon added successfully!")
        
        # Redirect to hackathons page and trigger modal
        return redirect(url_for('hackathons', show_modal=True))  # Pass a flag to show the modal

    return render_template("addhackathon.html")  # Render hackathons.html for GET requests

@app.route("/event/<event_name>")
def event_details(event_name):
    event = db.events.find_one({"name": event_name}, {"_id": 0})
    if event:
        return render_template("event_details.html", event=event)
    else:
        return "Event not found", 404

@app.route("/add_hackathon", methods=["GET"])
@admin_required  # Restrict access to Admins
def show_add_hackathon():
    return render_template("addhackathon.html")  # Render the add hackathon page

@app.route("/add_event", methods=["GET"])
@admin_required  # Restrict access to Admins
def show_add_event():
    return render_template("addevents.html")  # Render the add event page

@app.route("/add_club", methods=["GET"])
@admin_required  # Restrict access to Admins
def show_add_club():
    return render_template("addclubs.html")  # Render the add club page

if __name__ == "__main__":
    app.run(debug=True)
