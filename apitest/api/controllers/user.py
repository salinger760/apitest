from flask import Blueprint
from api import app
from api.models import User


mod = Blueprint('mod', __name__, url_prefix='/func1')

@mod.route('/a')
def func1_a():
  return 'func1_a'

@mod.route('/b')
def func1_b():
  return 'func1_b'

@mod.route('/')
def hello():
  return 'hello'
