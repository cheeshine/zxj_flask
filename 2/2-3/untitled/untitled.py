from flask import Flask,render_template
#from flask.ext.bootstrap import Bootstrap #专为Flask开发发拓展都暴露在flask.ext命名空间下，Flask-Bootstrap输出一个Bootstrap类
from flask_bootstrap import Bootstrap
app=Flask(__name__)
bootstrap=Bootstrap(app)#Flask扩展一般都在创建实例时初始化，这行代码是Flask-Bootstrap的初始化方法
@app.route('/')
def index():
 return render_template('index.html')
if __name__=="__main__":
 app.run(debug=True)