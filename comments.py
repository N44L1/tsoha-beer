from app import app
from flask import redirect, render_template, request, session, flash
from db import db
from sqlalchemy.sql import text
import accounts

# This code allows the user add a comment on to a beer 
@app.route("/beer/<int:beer_id>/comment", methods=['GET', 'POST'])
def comment_beer(beer_id):
    if request.method == 'POST':
        accounts.validate_csrf_token()

        # Handle the review submission
        comment = request.form['comment']
        username = session.get('username')         

        # Check if the comment exceeds the maximum length
        if len(comment) > 300:
            return redirect(request.referrer)
    
            # Save the review to the database
        db.session.execute(text("INSERT INTO Comments (BeerID, Username, Comment) VALUES (:beer_id, :username, :comment)"),
                           {"beer_id": beer_id, "username": username, "comment": comment})
        db.session.commit()
        return redirect("/beers")
    else:
        return render_template("comment_form.html", beer_id=beer_id, csrf_token=accounts.generate_csrf_token())