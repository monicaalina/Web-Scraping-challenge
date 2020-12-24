from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
import pandas as pd

app = Flask(__name__)

app.config["MONGO_URL"] = 'mongodb://localhost:27017/Mars_db'
mongo = PyMongo(app)

@app.route("/")
def index():
    MarsData = mongo.db.collection.find_one()
    return render_template("index.html", list = MarsData)


@app.route("/scrape")
def Scrape():
    Scrape.scrape_all()
    return redirect("/")