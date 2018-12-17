from flask import Blueprint
from api import app


func1 = Blueprint('func1', __name__, url_prefix='/func1')

@func1.route('/a')
def func1_a():
  return 'func1_a'

@func1.route('/b')
def func1_b():
  return 'func1_b'