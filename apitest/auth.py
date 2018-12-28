import re
import datatime
import functools
import jwt
from flask import Flask, request
from werkzeug.security import generate_password_hash, check_password_hash
from api.models import User
from api import app


def login_required(method):
  @functools.wraps(method)
  def wrapper(self):
    header = request.headers.get('Authorization')
    _, token = header.split()
    try:
      decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms='HS256')
    except jwt.DecodeError:
      abort(400, message='Token is not valid.')
    except jwt.ExpiredSignatureError:
      abort(400, message='Token is expired.')

    if db_session.query(User).filter(User.id=='').first()
