from flask import Flask
from flask_script import Manager
app = Flask(__name__)

manager = Manager(app)

@manager.command        #创建命令
def hello():
    print('大江大河！')

if __name__ == '__main__':
    manager.run()
