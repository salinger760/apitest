import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

SECRET_KEY = 'testkey'

params = {
  'user': 'root',
  'passowrd': 'password',
  'host': '192.168.33.10',
  'port': 3306,
  'database': 'testdb'
}

dsn_fmt = "mysql+pymysql://%(user)s:%(password)s@%(host)s:%(port)s/%(database)s"
DSN = dsn_fmt % params

DATABASE_URI = DSN
DATABASE_CONNECT_OPTIONS = {}
ADMINS = frozenset(['http://lucumr.pocoo.org/'])

WHOOSH_INDEX = os.path.join(_basedir, 'flask-website.whoosh')
DOCUMENTATION_PATH = os.path.join(_basedir, '../flask/docs/_build/dirhtml')

del os
