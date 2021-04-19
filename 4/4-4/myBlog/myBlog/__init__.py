# _*_ coding: utf-8 _*_
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from myBlog.controller import blog_message

#创建项目对象
app = Flask(__name__)
#数据库配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:66688888@localhost:3306/bloguser'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SECRET_KEY'] = '\xd1\xcc\x85\xd5\xaf\xa8\x98\xaf\xdd\xf7=n\xc9H\x19\xcbY)\x8b\xe3\x10\xeaVJ'  #要用到flash消息闪现，要设置SERET_KEY,值任意
#创建数据库对象
db = SQLAlchemy(app)