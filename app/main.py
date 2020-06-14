from flask import Flask, jsonify
from app.scrape import getCurrentData, getPreviousDayData
  
app = Flask(__name__)

@app.route("/")
def home_view():
        return "<h1>Welcome to my API</h1>"

