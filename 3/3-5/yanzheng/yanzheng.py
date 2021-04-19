from flask import Flask, render_template, request, flash

app = Flask(__name__)

app.secret_key = 'itheima'

@app.route('/', methods=['GET','POST'])
def index():

    #request：请求对象 --> 获取请求方式、数据
    #1. 判断请求方式
    if request.method == 'POST':
        # 2.获取请求的参数 request(通过input中的name值)
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        print(username,password,password2)

        # 3.判断参数是否填写&密码是否相同(u是为了解决编码问题)
        if not all([username,password,password2]):
            # print('参数不完整')
            flash(u'参数不完整')
        elif password != password2:
            # print('密码不一致')
            flash(u'密码不一致')
        else:
            return  'success'

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)