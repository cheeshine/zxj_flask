import os
from flask import Flask, url_for, redirect, render_template, request
from flask_admin.menu import MenuLink
from flask_sqlalchemy import SQLAlchemy
import flask_admin as admin
import flask_login as login
from flask_admin.contrib import sqla
import os.path as op

# Create application
app = Flask(__name__)

app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
# 创建虚拟secrey密钥以便使用会话
app.config['SECRET_KEY'] = '123456790'
# 数据库名字
app.config['DATABASE_FILE'] = 'sample_db.sqlite'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + app.config['DATABASE_FILE']
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(64))
    def __str__(self):
        return "{}".format(self.name)

# 创建视图
@app.route('/')
def index():
    return '<a href="/admin/">点击这里来到管理后台</a>'

admin = admin.Admin(app, name='Example: SQLAlchemy', template_mode='bootstrap3')

# 添加导航视图
admin.add_view(sqla.ModelView(Tag, db.session))
admin.add_link(MenuLink(name='Back Home', url='/', category='Links'))
admin.add_link(MenuLink(name='百度', url='http://www.baidu.com/', category='Links'))
admin.add_link(MenuLink(name='书创文化', url='http://www.toppr.net/', category='Links'))

def build_sample_db():
    db.drop_all()
    db.create_all()

    # 在数据库中添加几个数值
    tag_list = []
    for tmp in ["YELLOW", "WHITE", "BLUE", "GREEN", "RED", "BLACK", "BROWN", "PURPLE", "ORANGE"]:
        tag = Tag()
        tag.name = tmp
        tag_list.append(tag)
        db.session.add(tag)

if __name__ == '__main__':
    # 如果尚不存在示例数据库，则在运行时生成一个示例数据库.
    app_dir = op.realpath(os.path.dirname(__file__))
    database_path = op.join(app_dir, app.config['DATABASE_FILE'])
    if not os.path.exists(database_path):
        build_sample_db()

    # 运行程序
    app.run(debug=True)



