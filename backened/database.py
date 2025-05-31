from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017"  # Change this to your MongoDB Atlas URI if needed

client = MongoClient(MONGO_URI)  # ✅ Correct way to initialize MongoDB client
db = client["property-app"]  # ✅ Correct way to access a database

print("Connected to MongoDb ",db)