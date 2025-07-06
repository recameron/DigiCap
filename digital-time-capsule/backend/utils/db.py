from pymongo import MongoClient
import os

client = MongoClient(os.getenv("MONGODB_URI", "mongodb://localhost:27017"))
db = client["timecapsule"]
collection = db["entries"]
