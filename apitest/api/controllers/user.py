from flask import Blueprint, jsonify, make_response
from api import app
#from api.models import *
from api.models.User import User

user = User()

mod = Blueprint('func1', __name__, url_prefix='/func1')

@mod.route('/a')
def func1_a():
  #result = user.get_search_document()
  return jsonify({"data": [user.to_dict(u) for u in user.query.all()]})
  #return make_response(jsonify(result))

@mod.route('/b')
def func1_b():
  return 'func1_b'

@mod.route('/')
def hello():
  print("hello")
  return 'hello'