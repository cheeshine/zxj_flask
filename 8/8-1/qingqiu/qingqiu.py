from flask import Flask, _request_ctx_stack, _app_ctx_stack
app = Flask(__name__)

# 先检查两个栈的内容
print(_request_ctx_stack._local.__storage__)
print(_app_ctx_stack._local.__storage__)

# 生成一个请求上下文对象
request_context = app.test_request_context()
request_context.push()

# 请求上下文推入栈后，再次查看两个栈的内容
print(_request_ctx_stack._local.__storage__)
print(_app_ctx_stack._local.__storage__)
request_context.pop()

# 销毁请求上下文时，再次查看两个栈的内容
print(_request_ctx_stack._local.__storage__)
print(_app_ctx_stack._local.__storage__)
