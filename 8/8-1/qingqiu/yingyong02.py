from flask import Flask, _request_ctx_stack, _app_ctx_stack
# 创建两个Flask应用
app = Flask(__name__)
app2 = Flask(__name__)
# 先查看两个栈中的内容
_request_ctx_stack._local.__storage__
_app_ctx_stack._local.__storage__
# 构建一个app的请求上下文环境，在这个环境中运行app2的相关操作
with app.test_request_context():
    print("Enter app's Request Context:")
    print(_request_ctx_stack._local.__storage__)
    print(_app_ctx_stack._local.__storage__)
    print()
    with app2.app_context():
        print("Enter app2's App Context:")
        print(_request_ctx_stack._local.__storage__)
        print(_app_ctx_stack._local.__storage__)
    print("Exit app2's App Context:")
    print(_request_ctx_stack._local.__storage__)
    print(_app_ctx_stack._local.__storage__)
