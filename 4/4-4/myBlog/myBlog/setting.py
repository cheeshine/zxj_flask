# _*_ coding: utf-8 _*_

#调用模式是否开启
DEBUG = True

SQLALCHEMY_TRACK_MODIFICATIONS = False
#session必须要设置key
SECRET_KEY = '\xd1\xcc\x85\xd5\xaf\xa8\x98\xaf\xdd\xf7=n\xc9H\x19\xcbY)\x8b\xe3\x10\xeaVJ'  #这个有什么要求

#mysql数据库连接
SQLALCHEMY_DATABASE_URI = "mysql://root:66688888@localhost:3306/bloguser"