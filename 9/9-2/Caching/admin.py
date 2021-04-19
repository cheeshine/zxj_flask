from flask import Flask, current_app, make_response, request
from flask_caching import Cache
cache = Cache()
from werkzeug.contrib.cache import BaseCache

app = Flask(__name__)
app.config['SECRET_KEY'] = '123'
cache.init_app(app, config={ 'CACHE_TYPE' : 'mycache.mongo',
                            'MONGO_SERVERS':'mongodb://username:passwd@localhost:27017/db'})
class MongoCache(BaseCache):
    def __init__(self, host='localhost', port=27017, username=None, password=None, default_timeout=500,**kwargs):
        BaseCache.__init__(self, default_timeout)
        if isinstance(host, str):
            try:
                from pymongo import MongoClient
            except ImportError:
                raise RuntimeError('no pymongo module found')
            self._client = MongoClient(host=host,port=port, username=username, password=password, **kwargs)
        else:
            self._client = host

    # 接下来使用pymongo实现BaseCache的各个接口
    pass

def mongo(app, config, args, kwargs):
    """
    这里处理app传进来的参数用来连接mongodb
    :param app:
    :param config:
    :param args:
    :param kwargs:
    :return:
    """
    args.append(app.config['MONGO_SERVERS'])
    return MongoCache(*args, **kwargs)

if __name__ == '__main__':
    app.run(debug=True)
