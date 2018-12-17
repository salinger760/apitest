from yourapplication import app
from yourapplication.views import admin, frontend

modules_define = [admin.func1, frontend.func2]
for view in modules_define:
  app.register_blueprint(view)