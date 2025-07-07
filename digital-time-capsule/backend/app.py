from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS 

from datetime import datetime

app = Flask(__name__)

# MongoDB config
app.config["MONGO_URI"] = "mongodb+srv://rcameron4747:HAKvAlno540l9tb5@cluster0.knfwbcn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
mongo = PyMongo(app)

CORS(app)

@app.route("/api/entries", methods=["GET"])
def get_entries():
    entries = list(mongo.db.entries.find())
    for entry in entries:
        entry["_id"] = str(entry["_id"])
    return jsonify(entries)

@app.route("/api/entries", methods=["POST"])
def add_entry():
    data = request.get_json()
    message = data.get("message")
    open_date = data.get("openDate")
    if not message or not open_date:
        return jsonify({"error": "Missing fields"}), 400
    mongo.db.entries.insert_one({
        "message": message,
        "openDate": open_date,
        "createdAt": datetime.now()
    })
    return jsonify({"message": "Entry added"}), 201

if __name__ == "__main__":
    app.run(port=5000, debug=True)
