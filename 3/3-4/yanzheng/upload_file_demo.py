from flask import Flask, request, render_template
import os
from werkzeug.utils import secure_filename
from flask import send_from_directory
from forms import UploadForm
from werkzeug.datastructures import CombinedMultiDict

app = Flask(__name__)

# 新建images文件夹，UPLOAD_PATH就是images的路径
UPLOAD_PATH = os.path.join(os.path.dirname(__file__), 'images')


@app.route('/upload/', methods=['GET', 'POST'])
def settings():
    if request.method == 'GET':
        return render_template('upload.html')
    else:
        # 从request,files里面获取文件，这里使用CombinedMultiDict把form和file的数据组合起来，一起验证
        form = UploadForm(CombinedMultiDict([request.form, request.files]))
        if form.validate():
            desc = request.form.get('desc')
            avatar = request.files.get('avatar')
            # 对文件名进行包装
            filename = secure_filename(avatar.filename)
            avatar.save(os.path.join(UPLOAD_PATH, filename))
            print(desc)
            return '文件上传成功'
        else:
            print(form.errors)
            return "fail"


# 访问上传的文件
# 浏览器访问：http://127.0.0.1:5000/images/django.jpg/  就可以查看文件了
@app.route('/images/<filename>/', methods=['GET', 'POST'])
def get_image(filename):
    return send_from_directory(UPLOAD_PATH, filename)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)