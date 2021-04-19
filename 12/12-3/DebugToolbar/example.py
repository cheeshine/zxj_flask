import sys
sys.path.insert(0, '.')
import os
from flask import Flask, render_template, redirect, url_for
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True
#app.config['DEBUG_TB_PANELS'] = (
#    'flask_debugtoolbar.panels.headers.HeaderDebugPanel',
#    'flask_debugtoolbar.panels.logger.LoggingPanel',
#    'flask_debugtoolbar.panels.timer.TimerDebugPanel',
#)
#app.config['DEBUG_TB_HOSTS'] = ('127.0.0.1', '::1' )
app.config['SECRET_KEY'] = 'asd'
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL','sqlite:///' + os.path.join(app.root_path, 'test.db'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

toolbar = DebugToolbarExtension(app)


class ExampleModel(db.Model):
    __tablename__ = 'examples'
    value = db.Column(db.String(100), primary_key=True)


@app.route('/')
def index():
    app.logger.info("Hello there")
    ExampleModel.query.get(1)
    return render_template('index.html')


@app.route('/redirect')
def redirect_example():

    response = redirect(url_for('index'))
    response.set_cookie('test_cookie', '1')
    return response
db.create_all()
if __name__ == "__main__":
    app.run()
