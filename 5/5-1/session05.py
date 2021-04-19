from flask import Flask,session
from datetime import timedelta
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7) 	#设置在7天内有效


# 设置session
@app.route('/')
def set():
    session['username'] = '火云邪神！'
    session.permanent = True
    return '设置成功！'

if __name__ == '__main__':
    app.run()
