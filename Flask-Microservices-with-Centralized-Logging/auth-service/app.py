from flask import Flask, jsonify
from pymongo import MongoClient
from datetime import datetime
import os

app = Flask(__name__)

SERVICE_NAME = "auth-service"

MONGO_URL = os.getenv("MONGO_URL")
client = MongoClient(MONGO_URL)
db = client["microservice_logs"]
logs = db["logs"]

def log_event(level, message):
    logs.insert_one({
        "service": SERVICE_NAME,
        "level": level,
        "message":message,
        "timestamp": datetime.utcnow(),
        "host": os.getenv("HOSTNAME","auth-container")
    })

@app.route("/login",methods=["POST"])
def login():
    log_event("INFO","Login request received")
    return jsonify({"status":"Login successful"})
