from wtforms import Form, BooleanField, StringField, PasswordField, validators, TextAreaField, IntegerField
from wtforms.validators import DataRequired

class LoginForm(Form):
    email = StringField("邮箱", validators=[validators.Length(min=7, max=50), validators.DataRequired(message="数据非法！")])
    password = PasswordField("密码", validators=[validators.DataRequired(message="数据非法！")])

# Kullanıcı kayıt formu

class RegisterForm(Form):
    name = StringField("账号", validators=[validators.Length(min=3, max=25), validators.DataRequired(message="数据非法！")])
    username = StringField("名字", validators=[validators.Length(min=3, max=25), validators.DataRequired(message="数据非法！")])
    email = StringField("邮箱", validators=[validators.Email(message="数据非法！")])
    password = PasswordField("密码", validators=[
        validators.DataRequired(message="数据非法！"),
        validators.EqualTo(fieldname="confirm", message="数据非法！")
    ])
    confirm = PasswordField("确认密码", validators=[validators.DataRequired(message="数据非法！")])