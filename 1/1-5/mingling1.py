from flask import Flask
from flask_script import Manager,Server
from flask_script import Command
app = Flask(__name__)

manager = Manager(app)

class Hello(Command):
    def run(self):
        print('大江大河！')

manager.add_command('hello', Hello())   		#自定义命令hello
manager.add_command("runserver", Server())	#自定义命令runserver
if __name__ == '__main__':
    manager.run()
