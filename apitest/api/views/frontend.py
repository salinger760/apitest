from flask import Blueprint
from yourapplication import app


func2 = Blueprint('func2', __name__, url_prefix='/func2')

@func2.route('/a')
def func2_a():
  return 'func2_a'