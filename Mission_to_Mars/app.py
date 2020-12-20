
# import necessary libraries
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# create instance of Flask app
app = Flask(__name__)

# set up mongo connection
mongo =PyMongo(app, uri="mongodb://localhost:27017/mars_db")

# connect to mongo db and collection
@app.route("/")
def index():
    mars_db = mongo.db.mars_db.find_one()
    return render_template("index.html", mars_db=mars_db)

@app.route("/scrape")
def scrape():
    mars_data = scrape_mars.master_scrape()
    mongo.db.mars_db.update({}, mars_data, upsert=True)
    return redirect("/", code=302)

# Define main behavior
if __name__ == "__main__":
    app.run(debug=True)
