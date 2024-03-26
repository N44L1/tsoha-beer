from app import app
from flask import redirect, render_template, request, session
from db import db
from sqlalchemy.sql import text
from location import location_beer
from review import review_beer
from comments import comment_beer

#This function will be used later but as reviews are not complete now it is here because it is called to return None on a page
def get_average_rating(beer_id):
    sql = "SELECT AVG(Rating) AS avg_rating FROM Reviews WHERE beerid = :beer_id"
    result = db.session.execute(text(sql), {"beer_id": beer_id})
    avg_rating = result.fetchone()[0]
    if avg_rating:
        return round(avg_rating, 2)  
    else:
        return "No reviews yet"

# This function creates the basic list of all beers in the database
# The beers are clickable hyperlinks that take the user to the beers page
@app.route("/beers")
def beers():
    result = db.session.execute(text("SELECT beerid, beername FROM beers"))
    beers = result.fetchall()
    return render_template("beers.html", count=len(beers), beers=beers)

# The page and form to add a new beer to the database
@app.route("/newbeer")
def new():
    return render_template("newbeer.html")

@app.route("/send", methods=["POST"])
def send():
    beername = request.form["beername"]
    username = session.get("username")
    sql = "INSERT INTO beers (beername, added_by_username) VALUES (:beername, :added_by_username)"
    db.session.execute(text(sql), {"beername":beername, "added_by_username":username})
    db.session.commit()
    return redirect("/beers")

# Basic search of all beers by name of beer
@app.route("/result")
def result():
    search = request.args["search"]
    sql = "SELECT beerid, beername FROM beers WHERE beername LIKE :search"
    result = db.session.execute(text(sql), {"search": f"%{search}%"})
    beers = result.fetchall()
    return render_template("result.html", count=len(beers), beers=beers)

# Code for the individual beer pages
# The page shows beer name, user who added it and the average rating when reviews are ready to use
@app.route("/beer/<int:beer_id>")
def beer(beer_id):
    # Fetch the details of the beer from the database using the beer_id
    sql = "SELECT beername, added_by_username FROM beers WHERE beerid = :beer_id"
    result = db.session.execute(text(sql), {"beer_id": beer_id})
    beer = result.fetchone()
    
    # If the beer exists, render the beer info template
    if beer:
        beer_name = beer[0]
        addedbyusername = beer[1]
        if addedbyusername:
            added_by_user = addedbyusername
        else:
            added_by_user = "Unknown"
        average_rating = get_average_rating(beer_id)
    # Code that allows the comments on the beer to show on beers page
        sql_comments = "SELECT username, comment FROM Comments WHERE BeerID = :beer_id"
        result_comments = db.session.execute(text(sql_comments), {"beer_id": beer_id})
        comments = result_comments.fetchall()
    # Code that allows the locations and prices of the beer to show on the page
        sql_locations = "SELECT username, location, price FROM Locations WHERE BeerID = :beer_id"
        result_locations = db.session.execute(text(sql_locations), {"beer_id": beer_id})
        locations = result_locations.fetchall()


        return render_template("beer.html", beer_id=beer_id, beer_name=beer_name, added_by_user=added_by_user, average_rating=average_rating, comments=comments, locations=locations)


