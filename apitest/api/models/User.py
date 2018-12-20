from . import *
from api import app
from flask_marshmallow import Marshmallow


class User(Model):
  __tablename__ = 'users'
  id = Column('user_id', Integer, primary_key=True)
  openid = Column('openid', String(200))
  name = Column(String(200))

  def __init__(self, name, openid):
    self.name = name
    self.openid = openid
    ma = Marshmallow(app)

  def to_json(self):
    return dict(name=self.name, is_admin=self.is_admin)

  def get_search_document(self):
    
    users = db_session.query(User).all()
    print(users)
    return users
    '''
    return dict(
      id = self.id,
      name = self.name,
      openid = self.openid
    )
    '''

  @property
  def is_admin(self):
    return self.openid in app.config['ADMINS']

  def __eq__(self, other):
    return type(self) is type(other) and self.id == other.id

  def __ne__(self, other):
    return not self.__eq__(other)