from myBlog.model.User import User
from myBlog.model.Category import Category
from flask import url_for
import os

from myBlog.__init__ import app, db
from flask import request, render_template, flash, abort, redirect, session,Flask,g


@app.route('/')
def show_entries():
    categorys = Category.query.all() #查询，并实例化
    print(categorys)
    return render_template('show_entries.html', entries=categorys)


@app.route('/add_entry', methods=['POST'])
def add_entry():
    title = request.form['title']
    content = request.form['text']
    #连接数据库
    category = Category(title, content) #实例化文本对象
    db.session.add(category)
    db.session.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


@app.route('/login', methods=['POST','GET'])
def login():
    error = None
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        passwd = User.query.filter_by(password=password).first()

        if user is None:
            error = 'Invalid username'
        elif passwd is None:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect((url_for('show_entries')))
    return render_template('login.html', error=error)


@app.route('/go2regist')
def go2regist():
    return render_template('regist.html')

@app.route('/regist', methods=['POST', 'GET'])
def regist():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username is None or password is None:
            error = 'username and password is empty!'
            return render_template('login.html', error=error)

        else:
            try:
                user = User(username, password)
                db.session.add(user)
                db.session.commit()
                flash('You regist successfully!')
                return redirect(url_for('login'))
            except:
                flash('error')
                return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))