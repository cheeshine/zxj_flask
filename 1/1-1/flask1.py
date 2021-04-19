import flask                  	#导入flask模块
app = flask.Flask(__name__)   #实例化类Flask
@app.route('/')               	#装饰器操作，实现URL地址
def hello():                   	#定义业务处理函数helo()
    return '你好，这是第一个Flask程序!'
if __name__ == '__main__':
    app.run()                	#运行程序
