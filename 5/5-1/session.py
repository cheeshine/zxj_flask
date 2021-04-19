from flask import Flask,session
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

# 设置session
@app.route('/')
def set():
    session['username'] = '火云邪神' 		# 设置“字典”键值对
    return '登录成功！'

if __name__ == '__main__':
    app.run()
