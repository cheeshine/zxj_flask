from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
   return '欢迎%s' % name +'登录本系统'

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['biaodan']
      return redirect(url_for('success',name = user))  #URL重定向
   else:
      user = request.args.get('biaodan')
      return redirect(url_for('success',name = user))  #URL重定向

if __name__ == '__main__':
   app.run(debug = True)
