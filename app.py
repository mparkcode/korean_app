import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from dotenv import load_dotenv
import json

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
    parent = None
    if 'sound' in request.args:
        verbs = list(mongo.db.verbs.find({'sounds': request.args['sound']}))
        parent = request.args['parent']
    return render_template("display_verbs.html", sound=request.args['sound'], verbs=verbs, parent=parent) 

@app.route("/quiz")
def quiz():
    parent_verbs = list(mongo.db.verbs.find({'sounds': request.args['parent']}))
    for verb in parent_verbs:
        verb.pop('_id', None)
    if 'sound' in request.args:
        verbs = list(mongo.db.verbs.find({'sounds': request.args['sound']}))
        for verb in verbs:
            verb.pop('_id', None)
    return render_template("quiz.html", parent_verbs=json.dumps(parent_verbs), verbs=json.dumps(verbs))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)