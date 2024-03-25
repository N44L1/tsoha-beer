from app import app
from flask import redirect, render_template, request, session
from werkzeug.security import check_password_hash, generate_password_hash
from db import db
from sqlalchemy.sql import text

# When opening the page the user is greeted with a login screen as the website requires an acconut to use it
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login",methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
# Use the HTML form to get the login details and compare them to the ones on record
    sql = "SELECT username, password FROM users WHERE username=:username"
    result = db.session.execute(text(sql), {"username":username})
    user = result.fetchone()
# I have made separate pages for different events during the login process.
    if not user:
        return render_template("/user_not_exist.html")
    
    else:
        hash_value = user.password
        if check_password_hash(hash_value, password):            
            session["username"] = username
            return redirect("/")
        else:
            return render_template("/login_wrong.html")    
    
# Simple logout and return to login screen
@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

# Allows the user to create an account
@app.route("/signup")
def signuppage():
    return render_template("signup.html")
# Checks availability of username given
def user_exists(username):
    result = db.session.execute(text("SELECT COUNT(*) FROM Users WHERE Username = :username"), {"username":username})
    return result.scalar() > 0
# Hashes the password and add the user to the database of users
@app.route("/signup",methods=["POST"])
def signup():
    username = request.form["username"]
    password = request.form["password"]
    hash_value = generate_password_hash(password)

    if user_exists(username):
        return render_template("username_taken.html")

    sql = "INSERT INTO users (username, password, visible) VALUES (:username, :password, 1)"
    db.session.execute(text(sql), {"username":username, "password":hash_value})
    db.session.commit()
    return redirect("/creation")
# Simple info screen telling the user that the account creation was successful and prompting login
@app.route("/creation")
def creationsuccessful():
    return render_template("creation.html")

# The following allows the user to delete their account along with all info ever given on the website by them
# This is a choice I made as I believe that deleting one's account should remove all traces of them
@app.route("/deletion")
def deletionpage():
    return render_template("deletion.html")
# Deletion requires credentials
@app.route("/deletion", methods=["POST"])
def deletion():
    username = request.form["username"]
    password = request.form["password"]

    sql = "SELECT username, password FROM users WHERE username=:username"
    result = db.session.execute(text(sql), {"username": username})
    user = result.fetchone()
# The database is configured with ON DELETE CASCADE and thus everything that refrences the user is deleted
    if user:
        hash_value = user.password
        if check_password_hash(hash_value, password):
            # Delete the user's account (cascade deletion handled by the database)
            delete_user_sql = "DELETE FROM users WHERE username=:username"
            db.session.execute(text(delete_user_sql), {"username": username})

            db.session.commit()
            del session["username"]  # Optional: Log out user after deletion
            return redirect("/")
        else:
            return render_template("/login_wrong.html")
    else:
        return render_template("/user_not_exist.html")