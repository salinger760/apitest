from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config.from_object('webconfig')

import api.controllers


# Create tables
#from api.models import init_db
#init_db()