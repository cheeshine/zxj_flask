from flask import Flask,render_template,request,url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',title_name = '欢迎来到主页')

@app.route('/service')
def service():
    return '产品页面'

@app.route('/about')
def about():
    return '关于我们'

@app.template_test('current_link')
def is_current_link(link):
    return link == request.path

if __name__ == '__main__':
    app.run(debug=True)
