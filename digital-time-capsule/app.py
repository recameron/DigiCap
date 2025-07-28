import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
from werkzeug.utils import secure_filename
from flask import send_from_directory
from google.cloud import storage
import uuid
from datetime import datetime, timedelta

load_dotenv()

app = Flask(__name__)
bucket_name = os.environ.get("GCS_BUCKET_NAME")
# MongoDB config
app.config["MONGO_URI"] = os.getenv("MONGODB_URI")
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')
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
        entry["unlock_datetime"] = entry["unlock_datetime"].isoformat() if entry.get("unlock_datetime") else None
    return jsonify(entries)

@app.route('/api/entries', methods=['POST'])
def add_entry():
    # Check if request is multipart form data
    if 'message' not in request.form or 'recipientEmail' not in request.form or 'unlock_datetime' not in request.form:
        return jsonify({"error": "Missing required form fields"}), 400

    message = request.form['message']
    recipient_email = request.form['recipientEmail']
    unlock_datetime = request.form['unlock_datetime']

    try:
        unlock_datetime = datetime.fromisoformat(unlock_datetime.replace("Z", "+00:00"))
    except ValueError:
        return jsonify({"error": "Invalid unlock_datetime format"}), 400
    
    image_file = request.files.get('image')
    image_filename = None

    if image_file:
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        image_filename = f"{uuid.uuid4().hex}_{secure_filename(image_file.filename)}"
        blob = bucket.blob(image_filename)
        blob.upload_from_file(image_file,content_type=image_file.content_type)
        stored_blob_name = image_filename
    else:
        stored_blob_name = None
    
    # Insert into MongoDB
    entry_data = {
        "message": message,
        "recipientEmail": recipient_email,
        "unlock_datetime": unlock_datetime,
        "imageBlobName": stored_blob_name,
        "createdAt": datetime.utcnow(),
        "sent": False
    }
    mongo.db.entries.insert_one(entry_data)

    return jsonify({"success": True}), 201

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

#Serve static pages
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_react(path):
    build_dir = os.path.join(os.getcwd(), 'frontend', 'client', 'dist')
    if path != "" and os.path.exists(os.path.join(build_dir, path)):
        return send_from_directory(build_dir, path)
    else:
        return send_from_directory(build_dir, 'index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
