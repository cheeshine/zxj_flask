# coding: utf-8
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_filename):
    print("Hello World from %s!" % __name__)
    # todo application root和instalce pat
    # app = Flask(__name__, instance_relative_config=True)
    app = Flask(__name__)
    # todo
    app.config.from_object(config_filename)
    # todo
    # app.config.from_pyfile(config_filename, silent=True)

    # 每次请求后调用一个函数
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        if request.method == 'OPTIONS':
            response.headers['Access-Control-Allow-Methods'] = 'DELETE, GET, POST, PUT'
            headers = request.headers.get('Access-Control-Allow-Headers')
            if headers:
                response.headers['Access-Control-Allow-Headers'] = headers
        return response

    from app.users.model import db
    db.init_app(app)

    from app.users.api import init_api
    init_api(app)

    return app
