from wtforms import Form,FileField,StringField
from wtforms.validators import InputRequired
from flask_wtf.file import FileRequired,FileAllowed

class UploadForm(Form):
    avatar = FileField(validators=[FileRequired(),       #FileRequired必须上传
                                   FileAllowed(['jpg','png','gif'])     #FileAllowed:必须为指定的格式的文件
                                   ])
    desc = StringField(validators=[InputRequired()])