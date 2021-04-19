from flask import Flask
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.config.update(
    DEBUG = True,
    MAIL_SERVER='smtp.qq.com',
    MAIL_PROT=25,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = '输入发送者邮箱',
    MAIL_PASSWORD = '这里输入授权码',
    MAIL_DEBUG = True
)

mail = Mail(app)

@app.route('/')
def index():
# sender 发送方哈，recipients 邮件接收方列表
    msg = Message("Hi!This is a test ",sender='输入发送者邮箱', recipients=['输入接收者邮箱'])
# msg.body 邮件正文
    msg.body = "This is a first email"
# msg.attach 邮件附件添加
# msg.attach("文件名", "类型", 读取文件）
    with app.open_resource("123.jpg", 'rb') as fp:
        msg.attach("image.jpg", "image/jpg", fp.read())

    mail.send(msg)
    print("Mail sent")
    return "Sent"

if __name__ == "__main__":
    app.run()
