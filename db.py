from app import app
from flask_sqlalchemy import SQLAlchemy
from os import getenv

# Configures database location using .env file 
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)
