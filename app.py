import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from dotenv import load_dotenv

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/verbs")
def verbs():
    sounds = list(mongo.db.sounds.find())
    extended_sounds = list(mongo.db.extended_sounds.find())
    return render_template("verbs.html", sounds=sounds, extended_sounds=extended_sounds) 

@app.route("/display_verbs")
def display_verbs():
    verbs = list(mongo.db.verbs.find())
    if 'sound' in request.args:
        verbs = list(mongo.db.verbs.find({'sounds': request.args['sound']}))
    return render_template("display_verbs.html", verbs=verbs) 


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)