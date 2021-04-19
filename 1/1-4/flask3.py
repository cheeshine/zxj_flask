import flask         					#导入flask模块
html_txt = """        					#变量html_txt初始化，作为GET请求的页面
<!DOCTYPE html>
<html>
    <body>
        <h2>如果收到了GET请求</h2>
        <form method='post'>       		#设置请求方法是“post”
        <input type='submit' value='按下我发送POST请求' />
        </form>
    </body>
</html>
"""
app = flask.Flask(__name__)          		#实例化类Flask
#URL映射，不管是‘GET’方法还是‘POST’方法，都被映射到helo()函数
@app.route('/aaa',methods=['GET','POST'])
def helo():                         		#定义业务处理函数helo()
    if flask.request.method == 'GET':  	#如果接收到的请求是GET
        return html_txt             		#返回html_txt的页面内容
    else:                         			#否则接收到的请求是POST
        return '我司已经收到POST请求！'
if __name__ == '__main__':
    app.run()                      			#运行程序
