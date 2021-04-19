from flask import Flask,current_app

app = Flask(__name__)

#如果在视图函数外部访问，则必须手动推入一个app上下文到app上下文栈中
#第一种应用上下文方法
# app_context = app.app_context()
# app_context.push()
# print(current_app.name)

#第二种应用上下文方法
with app.app_context():
    print(current_app.name)     #context_demo

@app.route('/')
def index():
    # 在视图函数内部可以直接访问current_app.name
    print(current_app.name)    #context_demo
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)
