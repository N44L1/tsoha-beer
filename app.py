from flask import Flask
from os import getenv

# Main flask application file
app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")

import beer
import accounts