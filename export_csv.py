import csv
import os
from pymongo import MongoClient
from user import User

MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URI)
db = client["survey_db"]
collection = db["users"]

os.makedirs("data", exist_ok=True)

records = list(collection.find())

with open("data/users.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(User.csv_headers())

    for record in records:
        user = User(
            age=record["age"],
            gender=record["gender"],
            total_income=record["total_income"],
            expenses={
                "utilities": record.get("utilities", 0),
                "entertainment": record.get("entertainment", 0),
                "school_fees": record.get("school_fees", 0),
                "shopping": record.get("shopping", 0),
                "healthcare": record.get("healthcare", 0),
            }
        )
        writer.writerow(user.to_csv_row())

print(f"Exported {len(records)} records to data/users.csv")
