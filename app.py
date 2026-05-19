import os
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from user import User

app = Flask(__name__)

MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URI)
db = client["survey_db"]
collection = db["users"]


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        age = int(request.form.get("age"))
        gender = request.form.get("gender")
        total_income = float(request.form.get("total_income"))

        expenses = {
            "utilities": float(request.form.get("utilities_amount") or 0) if request.form.get("utilities") else 0,
            "entertainment": float(request.form.get("entertainment_amount") or 0) if request.form.get("entertainment") else 0,
            "school_fees": float(request.form.get("school_fees_amount") or 0) if request.form.get("school_fees") else 0,
            "shopping": float(request.form.get("shopping_amount") or 0) if request.form.get("shopping") else 0,
            "healthcare": float(request.form.get("healthcare_amount") or 0) if request.form.get("healthcare") else 0,
        }

        user = User(age, gender, total_income, expenses)
        collection.insert_one(user.to_dict())

        return redirect(url_for("success"))

    return render_template("index.html")


@app.route("/success")
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)
