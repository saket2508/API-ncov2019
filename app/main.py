from flask import Flask, request, jsonify
from app.scrape import getCurrentData, getPreviousDayData

app = Flask(__name__)

@app.route("/")
def home_view():
        return "<h1>Welcome to my API</h1>"

@app.route("/latest",methods=['GET'])
def latest_view():
        return jsonify(data= getCurrentData())

@app.route("/latest/<string:name>",methods=['GET'])
def latest_view_arg(name):
        return jsonify(data= getCurrentData()[name])

@app.route("/latest/<string:name>/<string:entity>",methods=['GET'])
def latest_view_arg2(name,entity):
        return jsonify(data= getCurrentData()[name][entity])

@app.route("/yesterday",methods=['GET'])
def yesterday_view():
        return jsonify(data= getPreviousDayData())

@app.route("/yesterday/<string:name>",methods=['GET'])
def yesterday_view_arg(name):
        return jsonify(data= getPreviousDayData()[name])

@app.route("/yesterday/<string:name>/<string:entity>",methods=['GET'])
def yesterday_view_arg2(name,entity):
        return jsonify(data= getPreviousDayData()[name][entity])