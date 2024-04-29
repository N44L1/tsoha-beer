from app import app
from flask import redirect, render_template, request, session
from db import db
from sqlalchemy.sql import text
import accounts

# This code allows the user to rate a beer on a scale from 1 to 10
@app.route("/beer/<int:beer_id>/review", methods=['GET', 'POST'])
def review_beer(beer_id):
    if request.method == 'POST':
        # Validate csrf token
        accounts.validate_csrf_token()

        # Handle the review submission
        rating = request.form['rating']
        username = session.get('username')         
        # Save the review to the database
    
        db.session.execute(text("INSERT INTO Reviews (BeerID, Username, Rating) VALUES (:beer_id, :username, :rating)"),
                           {"beer_id": beer_id, "username": username, "rating": rating})
        db.session.commit()
        return redirect("/beers")
    else:
        return render_template("review_form.html", beer_id=beer_id, csrf_token=accounts.generate_csrf_token())