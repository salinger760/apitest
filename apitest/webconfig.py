import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

config = {
  "user": "root",
  "password": "passowrd",
  "host": "127.0.0.1",
  "port": 3306,
  "database": "wikitest"
}
dsn_fmt = 'mysql+pymysql://%(user)s:%(password)s@%(host)s:%(port)s/%(database)s?charset=utf8'
dsn = dsn_fmt % config

SECRET_KEY = 'testkey'
DATABASE_URI = dsn
DATABASE_CONNECT_OPTIONS = {}
ADMINS = frozenset(['http://lucumr.pocoo.org/'])

WHOOSH_INDEX = os.path.join(_basedir, 'flask-website.whoosh')
DOCUMENTATION_PATH = os.path.join(_basedir, '../flask/docs/_build/dirhtml')

del os