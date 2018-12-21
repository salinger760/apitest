from . import *
from . import db_session
from api import app
from flask_marshmallow import Marshmallow


class User(Model):
  __tablename__ = 'users'
  id = Column('user_id', Integer, primary_key=True)
  openid = Column('openid', String(200))
  name = Column(String(200))

  def __init__(self):
    ma = Marshmallow(app)

  def to_json(self):
    return dict(name = self.name, is_admin = self.is_admin)

  def selectAll(self):
    users = db_session.query(User.name, User.openid).all()

  def to_dict(self, user):
    return {
      'id': uesr.id,
      'openid': user.openid,
      'name': user.name
      # Personに紐づいているHobbyを全部出力
      # 'hobby': [Hobby.to_dict(hobby) for hobby in self.hobbies]
    }


  @property
  def is_admin(self):
    return self.openid in app.config['ADMINS']

  def __eq__(self, other):
    return type(self) is type(other) and self.id == other.id

  def __ne__(self, other):
    return not self.__eq__(other)