from flask import Blueprint, jsonify, make_response
from api import app
from api.models import *
from api.models.User import User

user = User("test", "999")


mod = Blueprint('mod', __name__, url_prefix='/func1')

@mod.route('/a')
def func1_a():
  result = user.get_search_document()

  return make_response(jsonify(result))

@mod.route('/b')
def func1_b():
  return 'func1_b'

@mod.route('/')
def hello():
  return 'hello'
