from flask import Flask,current_app,url_for
app = Flask(__name__)
@app.route('/')
def index():
    # 在视图函数内部可以直接访问current_app.name
    print(current_app.name)    #context_demo
    return 'Hello World!'

@app.route('/list/')
def my_list():
    return 'my_list'

# 请求上下文
with app.test_request_context():
    # 手动推入一个请求上下文到请求上下文栈中
    # 如果当前应用上下文栈中没有应用上下文
    # 那么会首先推入一个应用上下文到栈中
    print(url_for('my_list'))

if __name__ == '__main__':
    app.run(debug=True)
