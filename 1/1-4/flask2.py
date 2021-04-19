import flask                    		#导入flask模块
app = flask.Flask(__name__)      	#实例化类
@app.route('/')           			#装饰器操作，实现URL地址映射
@app.route('/aaa')        			#装饰器操作，实现第2个URL地址映射
def hello():
    return '你好，这是一个Flask程序！'
if __name__ == '__main__':
    app.run()           					#运行程序

