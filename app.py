from flask import Flask
from flask_bootstrap import Bootstrap
from os import getenv

# Main flask application file
app = Flask(__name__)
Bootstrap(app)
app.secret_key = getenv("SECRET_KEY")

import beer
import accounts