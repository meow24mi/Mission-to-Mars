from flask import Flask, render_template
from flask_pymongo import PyMongo
import scraping
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Route to html page. This function is what links our visual representation of our work, our web app, to the code that powers it.
@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

#Route flask to take. access db, and scrape data, update and return message when completed
@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scraping.scrape_all()
    mars.update({}, mars_data, upsert=True)
    return redirect('/', code=302)

#Flask to run the code
if __name__ == "__main__":
   app.run()