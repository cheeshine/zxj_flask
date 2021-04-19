from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# url的格式为：数据库的协议：//用户名：密码@ip地址：端口号（默认可以不写）/数据库名
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:66688888@localhost/bloguser"
# 动态追踪数据库的修改. 性能不好. 且未来版本中会移除. 目前只是为了解决控制台的提示才写的
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# 创建数据库的操作对象
db = SQLAlchemy(app)


class Category(db.Model):
    __tablename__ = 'b_category'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(20), unique=True)
    content = db.Column(db.String(100))

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __repr__(self):
        return '<Category %r>' %self.title


class User(db.Model):
    __tablename__ = 'b_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(10), unique=True)
    password = db.Column(db.String(16))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' %self.username


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    # 删除所有的表
    db.drop_all()
    # 创建表
    db.create_all()