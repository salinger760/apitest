from . import *
from api import app
from marshmallow import Schema, fields, post_load, pprint


class User(Model):
  __tablename__ = 'users'
  id = Column('user_id', Integer, primary_key=True)
  openid = Column('openid', String(200))
  name = Column('name', String(200))

  #def __init__(self):

  def to_json(self):
    return dict(name = self.name, is_admin = self.is_admin)

  def to_dict(self, user):
    return {
      'id': user.id,
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


class UserSchema(Schema):
  id = fields.Integer(dump_only=True)
  openid = fields.Str(required=True)
  name = fields.Str()

  class Meta:
    strict = True

  def format_name(self, author):
        return "{}, {}".format(user.openid, user.name)
