from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS 

from datetime import datetime

app = Flask(__name__)

# MongoDB config
app.config["MONGO_URI"] = "mongodb+srv://rcameron4747:NvsknD0ANImBBLMn@cluster0.knfwbcn.mongodb.net/DigitalTimeCapsule?retryWrites=true&w=majority&appName=Cluster0"
#app.config["MONGO_URI"] = "mongodb+srv://rcameron4747:gHnytKvoapiHKd2K@cluster0.knfwbcn.mongodb.net/"
mongo = PyMongo(app)

# Check if mongo.db is initialized
if mongo.db is None:
    print("MongoDB connection NOT initialized")
else:
    print("MongoDB connection initialized successfully")


CORS(app)

@app.route("/api/entries", methods=["GET"])
def get_entries():
    entries = list(mongo.db.entries.find())
    for entry in entries:
        entry["_id"] = str(entry["_id"])
    return jsonify(entries)

@app.route('/api/entries', methods=['POST'])
def add_entry():
    data = request.get_json()
    print("Received data:", data)  # <-- Log the data to console

    if not data:
        return jsonify({"error": "No JSON data received"}), 400
    
    message = data.get('message')
    recipient_email = data.get('recipientEmail')
    unlock_date = data.get('unlockDate')

    missing_fields = []
    if not message:
        missing_fields.append('message')
    if not recipient_email:
        missing_fields.append('recipientEmail')
    if not unlock_date:
        missing_fields.append('unlockDate')

    if missing_fields:
        return jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400
    
    # Insert into MongoDB
    mongo.db.entries.insert_one({
        "message": message,
        "recipientEmail": recipient_email,
        "unlockDate": unlock_date
    })

    return jsonify({"success": True}), 201


if __name__ == "__main__":
    app.run(port=5000, debug=True)
