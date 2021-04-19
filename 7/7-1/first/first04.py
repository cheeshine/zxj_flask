from flask import Flask
from flask_admin import Admin, BaseView, expose

class MyView(BaseView):
    @expose('/')
    def index(self):
        return self.render('index.html')

app = Flask(__name__)

admin = Admin(app, name='后台管理')
admin.add_view(MyView(name='管理员1', endpoint='test1', category='管理员'))
admin.add_view(MyView(name='管理员2', endpoint='test2', category='管理员'))
admin.add_view(MyView(name='管理员3', endpoint='test3', category='管理员'))
app.run()
