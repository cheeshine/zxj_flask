# -*- encoding:utf-8 -*-
import os
import flask
from flask import g,request,render_template,session,redirect,url_for
from sqlite3 import connect

DBNAME = 'test.db'

app = flask.Flask(__name__)
app.secret_key = 'dfadff#$#5dgfddgssgfgsfgr4$T^%^'

@app.before_request
def before_request():
    g.db = connect(DBNAME)

@app.teardown_request
def teardown_request(e):
    db = getattr(g,'db',None)
    if db:
        db.close()
    g.db.close()

@app.route('/')
def index():
    if 'username' in session:
        return "你好，" + session['username'] + '<p><a href="/logout">注销</a></p>'
    else:
        return '<a href="/login">登录</a>,<a href="/signup">注册</a>'

@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    else:
        name = 'name' in request.form and request.form['name']
        passwd = 'passwd' in request.form and request.form['passwd']
        if name and passwd:
            cur = g.db.cursor()
            cur.execute('insert into user (name,passwd) values (?,?)',(name,passwd))
            cur.connection.commit()
            cur.close()
            session['username'] = name
            return redirect(url_for('index'))
        else:
            return redirect(url_for('signup'))

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        name = 'name' in request.form and request.form['name']
        passwd = 'passwd' in request.form and request.form['passwd']
        if name and passwd:
            cur = g.db.cursor()
            cur.execute('select * from user where name=?',(name,))
            res = cur.fetchone()
            if res and res[1] == passwd:
                session['username'] = name
                return redirect(url_for('index'))
            else:
                return '登录失败!'
        else:
            return '参数不全!'
        
@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('index'))

def init_db():
    if not os.path.exists(DBNAME):
        cur = connect(DBNAME).cursor()
        cur.execute('create table user (name text,passwd text)')
        cur.connection.commit()
        print('数据库初始化完成!')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
