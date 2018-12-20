from api import app
from . import user, blog

modules_define = [user.mod, blog.mod]
for view in modules_define:
  app.register_blueprint(view)
