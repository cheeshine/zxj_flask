import json

from redis import Redis

from flask import session
from flask import request
from flask import Blueprint
from flask import render_template
from flask import Markup
from flask.views import View

redis = Redis()


def _is_like(path, through=False):
    key = 'like-done:{}:{}'.format(session.sid, path)
    done = redis.get(key)
    if not done and through:
        redis.set(key, 1)
    return True if done else False


class CounterSession(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.context_processor(self.context_processor)
        app.after_request(self.after_request)
        app.add_url_rule('/like', view_func=Like.as_view('like'))

    def context_processor(self):
        path = request.path
        view_key = '{}:{}'.format('view-count', path)
        view_count = redis.get(view_key) or 0
        like_key = '{}:{}'.format('like-count', path)
        like_count = redis.get(like_key) or 0
        like_done = _is_like(path)

        return dict(view_count=view_count,
                    like_count=like_count,
                    path=path,
                    like_done=like_done)

    def after_request(self, response):
        path = request.path
        view_key = '{}:{}'.format('view-count', path)
        redis.incr(view_key)
        return response


class Like(View):
    methods = ['POST']

    def dispatch_request(self):
        if request.method == 'POST':
            path = request.form.get('path')
            key = '{}:{}'.format('like-count', path)
            if not _is_like(path, through=True):
                redis.incr(key)
            count = redis.get(key) or 0
            return '{"count":%s}' % count


class CounterRender(object):
    def __init__(self):
        pass

    def render(self, *args, **kwargs):
        return render_template(*args, **kwargs)

    @property
    def html(self):
        return Markup(self.render('CounterRedis/inline.html', rb=self))


def count_this_path(*args, **kwargs):
    counter_render = CounterRender(*args, **kwargs)
    return counter_render.html


class Counter(object):
    def __init__(self, app):
        self.init_app(app)

    def init_app(self, app):
        self.register_blueprint(app)
        app.add_template_global(count_this_path)

    def register_blueprint(self, app):
        module = Blueprint(
            'CounterRedis',
            __name__,
            template_folder='templates'
        )
        app.register_blueprint(module)
        return module


class CounterRedis(object):
    def __init__(self, app):
        CounterSession(app)
        Counter(app)
