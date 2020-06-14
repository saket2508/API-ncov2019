from flask import Flask 
from app.scrape import getCurrentData, getPreviousDayData
  
app = Flask(__name__)

@app.route("/")
def home_view():
        return "<h1>Welcome to my API</h1>"

@app.route("/latest")
def latest_view():
        return getCurrentData()

@app.route("/yesterday")
def yesterday_view():
        return getPreviousDayData()

