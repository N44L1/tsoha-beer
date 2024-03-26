from app import app
from flask import redirect, render_template, request, session
from db import db
from sqlalchemy.sql import text

# This code allows the user add a comment on to a beer 
@app.route("/beer/<int:beer_id>/comment", methods=['GET', 'POST'])
def comment_beer(beer_id):
    if request.method == 'POST':

        # Handle the review submission
        comment = request.form['comment']
        username = session.get('username')         
        # Save the review to the database
    
        db.session.execute(text("INSERT INTO Comments (BeerID, Username, Comment) VALUES (:beer_id, :username, :comment)"),
                           {"beer_id": beer_id, "username": username, "comment": comment})
        db.session.commit()
        return redirect("/beers")
    else:
        return render_template("comment_form.html", beer_id=beer_id)