from flask import Flask
from main.views import *
from app.app01.views import *
from app.app02.views import *

app = Flask(__name__)
app.register_blueprint(main)
app.register_blueprint(main,url_prefix='/index')
app.register_blueprint(app01,url_prefix='/app01')
app.register_blueprint(app02,url_prefix='/app02')
app.register_blueprint(app01,url_prefix='/app03')
app.register_blueprint(app02,url_prefix='/app04')
app.register_blueprint(app02)


if __name__=='__main__':
  app.run()
