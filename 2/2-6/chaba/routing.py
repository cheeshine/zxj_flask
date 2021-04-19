from flask import Flask

from views import UserView

#App配置
app= Flask(__name__)

#URLs
app.add_url_rule('/users', view_func=UserView.as_view('user_view'), methods=['GET'])

from error_handlers import *

if __name__ == '__main__':
    app.run()
