from flask import Flask
app = Flask(__name__)

@app.route('/blog/<int:ID>')
def show_blog(ID):
   return '我的年龄是：%d' % ID + '岁！'

@app.route('/rev/<float:No>')
def revision(No):
   return '我身上只有%f' % No + '元钱了！'

if __name__ == '__main__':
   app.run()
