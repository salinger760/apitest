from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config.from_object('webconfig')

import api.views