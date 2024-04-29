from app import app
from flask import redirect, render_template, request, session
from db import db
from sqlalchemy.sql import text
import accounts

# This code allows the user to report sightings of a beer with the location and price of the beer at said location
@app.route("/beer/<int:beer_id>/location", methods=['GET', 'POST'])
def location_beer(beer_id):
    if request.method == 'POST':
        # Validate csrf token
        accounts.validate_csrf_token()

        # Handle the review submission
        location = request.form['location']
        price = request.form['price']
        username = session.get('username')         
        # Save the review to the database
    
        db.session.execute(text("INSERT INTO Locations (BeerID, Username, Location, Price) VALUES (:beer_id, :username, :location, :price)"),
                           {"beer_id": beer_id, "username": username, "location": location, "price": price})
        db.session.commit()
        return redirect("/beers")
    else:
        return render_template("location_form.html", beer_id=beer_id, csrf_token=accounts.generate_csrf_token())