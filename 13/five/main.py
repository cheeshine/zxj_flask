from datetime import datetime

from redis import Redis

from flask import Flask, session, render_template
from flask.ext.session import Session

from extensions import CounterRedis

app = Flask(__name__, template_folder=".")


SESSION_TYPE = 'redis'
app.config.from_object(__name__)
Session(app)

cr = CounterRedis(app)

@app.route("/")
def index():
    return render_template('example.html')

@app.route("/world")
def world():
    return render_template('example.html')

if __name__ == "__main__":
    app.debug = True
    app.run()