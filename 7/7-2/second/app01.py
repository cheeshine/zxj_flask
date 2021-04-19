import pymongo
from flask import Flask, url_for, redirect, render_template, request
from flask_admin.model.fields import InlineFormField, InlineFieldList

from wtforms import form, fields, validators

import flask_admin as admin
import flask_login as login
from flask_admin.contrib.mongoengine import ModelView

# Create application
app = Flask(__name__)


# 创建应用程序


# 设置密钥
app.config['SECRET_KEY'] = '123456790'

# 数据库连接
conn = pymongo.MongoClient("mongodb://localhost:27017/")
db = conn["toppr"]
# User admin
class InnerForm(form.Form):
    name = fields.StringField('Name')
    test = fields.StringField('Test')

class UserForm(form.Form):
    name = fields.StringField('Name')
    email = fields.StringField('Email')
    password = fields.StringField('Password')
    # Inner form
    inner = InlineFormField(InnerForm)
    # Form list
    form_list = InlineFieldList(InlineFormField(InnerForm))

class UserView(ModelView):
    column_list = ('name', 'email', 'password')
    column_sortable_list = ('name', 'email', 'password')
    form = UserForm
    column_searchable_list = ('name', 'text')

# Flask视图
@app.route('/')
def index():
    return '<a href="/admin/">点击来到后台页面!</a>'

if __name__ == '__main__':
    # 创建后台
    admin = admin.Admin(app, name='PyMongo数据库')
    # 添加视图
    admin.add_view(UserView(db.user, '用户'))
    # 启动应用程序
    app.run(debug=True)
