from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

client = MongoClient(os.getenv("MONGODB_URI", "mongodb://localhost:27017"))
db = client["timecapsule"]
collection = db["entries"]

@app.route('/api/entry', methods=['POST'])
def create_entry():
    data = request.json
    collection.insert_one(data)
    return jsonify({"message": "Entry saved!"})

@app.route('/api/entries', methods=['GET'])
def get_entries():
    entries = list(collection.find({}, {'_id': False}))
    return jsonify(entries)

if __name__ == "__main__":
    app.run(debug=True)
