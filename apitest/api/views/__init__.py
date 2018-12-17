from api import app
import api.views as view

modules_define = [view.admin.func1, view.frontend.func2]
for view in modules_define:
  app.register_blueprint(view)