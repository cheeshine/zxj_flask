from flask import Flask,session
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


# 删除session
@app.route('/delete/')
def delete():
    print(session.get('username'))
    session.pop('username')
    print(session.get('username'))
    return '删除成功'


if __name__ == '__main__':
    app.run()
