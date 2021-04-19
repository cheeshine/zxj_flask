from flask import Flask
from flask import render_template

class Myobj(object):
    def __init__(self, name):
        self.name = name

    def getname(self):
        return self.name

app = Flask(__name__)

@app.route('/')
def index():
    mydict = {'key1': '123', 'key': 'hello'}
    mylist = (123, 234, 345, 789)
    myintvar = 0
    myobj = Myobj('Hyman')
    return render_template('index.html', mydict=mydict, mylist=mylist, myintvar=0, myobj=myobj)

if __name__ == '__main__':
    app.run()
