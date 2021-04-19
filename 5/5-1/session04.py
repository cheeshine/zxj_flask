from flask import Flask, session
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)


# 设置session
@app.route('/')
def set():
    session['username'] = '火云邪神'
    return 'success'


# 读取session
@app.route('/get/')
def get():
    # session['username']
    # session.get('username')
    return session.get('username')


# 清除session中所有数据
@app.route('/clear')
def clear():
    print(session.get('username'))
    # 清除session中所有数据
    session.clear
    print(session.get('username'))
    return '清除成功！'

if __name__ == '__main__':
    app.run()
