from flask import Blueprint, jsonify, make_response
from api import app
from api.models import *
from api.models.User import User, UserSchema
#from marshmallow import pprint
import pprint

user = User()
user_schema = UserSchema()
users_schema = UserSchema(many=True)


'''
result = schema.dump(db_session.query(user).all())

pprint(result.data)
'''
 
#TEST
def dump_data():
  users = db_session.query(User).all()
  print (type(users))
  print(users)
  #for row in users:
  #  print("%d, %s : %s" % (row.id, row.name, row.openid))

#dump_data()


mod = Blueprint('func1', __name__, url_prefix='/func1')

@mod.route('/a')
def func1_a():
  return jsonify({"data": [user.to_dict(u) for u in User.query.all()]})

@mod.route('/b')
def func1_b():
  rows = db_session.query(User).all()
  #rows = User.query.all()
  # Serialize the queryset
  result = users_schema.dump(rows)
  return jsonify({'users!': result.data})

@mod.route('/')
def hello():
  print("hello")
  return 'hello'


def select_all():
  return db_session.query(User).all()

