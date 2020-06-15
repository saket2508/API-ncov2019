from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from app.scrape import getCurrentData, getPreviousDayData

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
@cross_origin()
def home_view():
        return "<h1>Welcome to my API</h1>"

@app.route("/latest",methods=['GET'])
@cross_origin()
def latest_view():
        return jsonify(data= getCurrentData())

@app.route("/latest/<string:name>",methods=['GET'])
@cross_origin()
def latest_view_arg(name):
        return jsonify(data= getCurrentData()[name])

@app.route("/latest/<string:name>/<string:entity>",methods=['GET'])
@cross_origin()
def latest_view_arg2(name,entity):
        return jsonify(data= getCurrentData()[name][entity])

@app.route("/yesterday",methods=['GET'])
@cross_origin()
def yesterday_view():
        return jsonify(data= getPreviousDayData())

@app.route("/yesterday/<string:name>",methods=['GET'])
@cross_origin()
def yesterday_view_arg(name):
        return jsonify(data= getPreviousDayData()[name])

@app.route("/yesterday/<string:name>/<string:entity>",methods=['GET'])
@cross_origin()
def yesterday_view_arg2(name,entity):
        return jsonify(data= getPreviousDayData()[name][entity])