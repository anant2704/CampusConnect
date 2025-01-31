import os

class Config:
    SECRET_KEY = os.urandom(24)  # Generates a random secret key

    # Alternatively, you can set a fixed secret key
    # SECRET_KEY = 'your_secret_key_here'
    MONGO_URI = "mongodb://localhost:27017/community_platform"

