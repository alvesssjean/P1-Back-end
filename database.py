from pymongo import MongoClient

MONGO_URL = "mongodb://mongodb:27018"

client = MongoClient(MONGO_URL)

db = client["bank"]

transations_collection = db["transations"]