from flask import Flask, jsonify
from pymongo import MongoClient
from datetime import datetime
import os

app = Flask(__name__)

SERVICE_NAME = "order-service"

MONGO_URL = os.getenv("MONGO_URL")
client = MongoClient(MONGO_URL)
db = client["microservice_logs"]
logs = db["logs"]

def log_events(level,message):
    logs.insert_one({
        "Service":"SERVICE_NAME",
        "level": level,
        "message": message,
        "timestamp": datetime.utcnow(),
        "host": os.getenv("HOSTNAME", "auth-container")
    })

@app.route("/order",methods=["POST"])
def login():
    log_events("INFO", "Order placed")
    return jsonify({"status":"order confirmed"})


