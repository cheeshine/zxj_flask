from flask import render_template, jsonify
from routing import app
from myexceptions import *

#错误处理程序
@app.errorhandler(404)
def unexpected_error(error):
    """ 未知错误的错误处理程序 """
    return render_template('error.html'), 404

@app.errorhandler(AuthenticationException)
def auth_error(error):
    """ 用户输入数据发生异常时的错误处理程序用 """
    return jsonify({'error': error.get_message()})
