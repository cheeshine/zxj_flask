from flask import Flask,session
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

# 设置session
@app.route('/')
def set():
    session['username'] = '火云邪神' # 设置“字典”键值对
    return 'success'

# 读取session
@app.route('/get')
def get():
    # session['username']
    # session.get('username')
    return session.get('username')

if __name__ == '__main__':
    app.run()
