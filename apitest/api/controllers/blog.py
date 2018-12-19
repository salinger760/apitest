from flask import Blueprint
from api import app


mod = Blueprint('func2', __name__, url_prefix='/func2')

@mod.route('/a')
def func2_a():
  return 'func2_a'