from flask import Flask, render_template, session, redirect, url_for,flash
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aaa bbb ccc'

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


class NameForm(FlaskForm):
    name = StringField('你叫什么名字?', validators=[Required()])
    submit = SubmitField('提交')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
   form = NameForm()
   if form.validate_on_submit():
         old_name = session.get('name')
         if old_name is not None and old_name != form.name.data:
                 flash('你刚刚修改了用户名！')
         session['name'] = form.name.data
         return redirect(url_for('index'))
   return render_template('index.html',
         form = form, name = session.get('name'))

if __name__ == '__main__':
    app.run()
