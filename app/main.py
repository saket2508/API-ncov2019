from flask import Flask 
from scrape import getCurrentData, getPreviousDayData
  
app = Flask(__name__)

@app.route("/")
def home_view():
        return getCurrentData()

@app.route("/yesterday")
def yesterday_view():
        return getPreviousDayData()

if __name__=="__main__":
    app.run(debug=True)
