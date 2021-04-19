from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_ckeditor import CKEditor, CKEditorField
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'

# 创建数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///123.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)
ckeditor = CKEditor(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    text = db.Column(db.Text)


# Flask视图
@app.route('/')
def index():
    return '<a href="/admin/">来到管理平台</a>'


# Admin管理选项
class PostAdmin(ModelView):
    #使用CKEditorField
    form_overrides = dict(text=CKEditorField)
    create_template = 'edit.html'
    edit_template = 'edit.html'


admin = Admin(app, name='Flask-CKEditor例子')
admin.add_view(PostAdmin(Post, db.session))


def init_db():
    """
    Populate a small db with some example entries.
    """
    db.drop_all()
    db.create_all()

    # Create sample Post
    title = "勇士输球，火箭扳回一局！"
    text = "勇士输球，火箭扳回一局勇士输球，火箭扳回一局勇士输球，火箭扳回一局勇士输球，火箭扳回一局"

    post = Post(title=title, text=text)
    db.session.add(post)
    db.session.commit()

init_db()
if __name__ == '__main__':

    app.run(debug=True)
