from flask import Flask, jsonify
from pymongo import MongoClient
from datetime import datetime
import os

app = Flask(__name__)

SERVICE_NAME = "payment-service"

MONGO_URL = os.getenv("MONGO_URL")
client = MongoClient(MONGO_URL)
db = client["microservice_logs"]
logs = db["logs"]

def log_events(level,message):
    logs.insert_one({
        "Service":SERVICE_NAME,
        "level": level,
        "message": message,
        "timestamp": datetime.utcnow(),
        "host": os.getenv("HOSTNAME", "payment-container")
    })

@app.route("/pay",methods=["POST"])
def pay():
    log_events("INFO", "Payment initiated")
    log_events("INFO", "Payment successful")
    return jsonify({"status":"payment done"})


