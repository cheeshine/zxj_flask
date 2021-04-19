from flask import Flask,request,render_template
import os
from werkzeug.utils import secure_filename
from flask import send_from_directory

app = Flask(__name__)

#新建images文件夹，UPLOAD_PATH就是images的路径
UPLOAD_PATH = os.path.join(os.path.dirname(__file__),'images')

@app.route('/upload/',methods=['GET','POST'])
def settings():
    if request.method == 'GET':
        return render_template('upload.html')
    else:
        desc = request.form.get('desc')
        avatar = request.files.get('avatar')
        # 对文件名进行包装，为了安全,不过对中文的文件名显示有问题
        filename = secure_filename(avatar.filename)
        avatar.save(os.path.join(UPLOAD_PATH,filename))
        print(desc)
        return '文件上传成功'

#访问上传的文件
#浏览器访问：http://127.0.0.1:5000/images/django.jpg/  就可以查看文件了
@app.route('/images/<filename>/',methods=['GET','POST'])
def get_image(filename):
    return send_from_directory(UPLOAD_PATH,filename)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)