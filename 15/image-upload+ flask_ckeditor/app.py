import os

from flask import Flask, render_template, request, url_for, send_from_directory
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from flask_ckeditor import CKEditor, CKEditorField, upload_fail, upload_success

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['CKEDITOR_SERVE_LOCAL'] = True
app.config['CKEDITOR_HEIGHT'] = 400
app.config['CKEDITOR_FILE_UPLOADER'] = 'upload'
#app.config['CKEDITOR_ENABLE_CSRF'] = True  		#如果要启用CSRF保护，请取消对此行的注释
app.config['UPLOADED_PATH'] = os.path.join(basedir, 'uploads')

app.secret_key = 'secret string'

ckeditor = CKEditor(app)
# csrf = CSRFProtect(app)  #如果要启用CSRF保护，请取消对此行的注释

class PostForm(FlaskForm):
    title = StringField('Title')
    body = CKEditorField('Body', validators=[DataRequired()])
    submit = SubmitField()

@app.route('/', methods=['GET', 'POST'])

def index():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        #可能需要在此处将数据存储在数据库中
        return render_template('post.html', title=title, body=body)
    return render_template('index.html', form=form)
@app.route('/files/<filename>')

def uploaded_files(filename):
    path = app.config['UPLOADED_PATH']
    return send_from_directory(path, filename)
@app.route('/upload', methods=['POST'])

def upload():
    f = request.files.get('upload')
    extension = f.filename.split('.')[1].lower()
    if extension not in ['jpg', 'gif', 'png', 'jpeg']:
        return "上传图片的格式非法！"
    f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
    url = url_for('uploaded_files', filename=f.filename)
    return url

if __name__ == '__main__':
    app.run(debug=True)




