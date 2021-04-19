from flask import Flask
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)


# 命令既可以用-n,也可以用--name，dest="name"用户输入的命令的名字作为参数传给了函数中的name
@manager.option('-n', '--name', dest='name',
                help='Your name',
                default='world')
# 命令既可以用-u,也可以用--url,dest="url"用户输入的命令的url作为参数传给了函数中的url
@manager.option('-u', '--url', dest='url',
                default='www.csdn.com')
def hello(name, url):
    print('hello', name)
    print(url)


if __name__ == '__main__':
    manager.run()
