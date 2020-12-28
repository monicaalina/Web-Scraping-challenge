# Import dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
import pandas as pd

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection

mongo = PyMongo(app, uri="mongodb://localhost:27017/MarsDB")
#app.config['MONGO_URL'] = 'mongodb://localhost:27017/MarsDB'
#mongo = PyMongo(app)



# Route to render index.html template using data from Mongo
@app.route('/')
def Home():
    
    # Find one record of data from the mongo database
    MarsScraping = mongo.db.MarsDB.find_one()

    # Return template and data
    return render_template('index.html', MarsData = MarsScraping)

# Route that will trigger the scrape function
@app.route('/scrape')
def scrape():
    
    # Run the scrape function
    
    MarsData = scrape_mars.MarsNews()
    MarsData = scrape_mars.FeaturedImage()
    MarsData = scrape_mars.MarsFacts()
    MarsData = scrape_mars.Hemispheres()

    # Update the Mongo database using update and upsert = True
    
    mongo.db.MarsDB.update({}, MarsData, upsert = True)

    # Redirect back to home page

    #print('Redirect')
    return redirect("/")


if __name__ == "__main__":
    app.run(debug = True)