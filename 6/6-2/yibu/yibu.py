import threading

from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config.update(
    #EMAIL SETTINGS
    MAIL_SERVER='smtp.qq.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    # 下面写的是你的账号
    MAIL_USERNAME = '371972484@qq.com',
    # 下面写的是授权码 不是你的密码哦 被坑了一天的时间 哎
    MAIL_PASSWORD = ''
    )

mail = Mail(app)

@app.route('/')
def index():
    send_mail()
    print('email send!!')
    return "Sent"

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_mail():
    #sender-发件人邮箱    recipients-收件人邮箱
    msg = Message("Hi!This is acesh  ",sender='371972484@qq.com', recipients=['729017304@qq.com'])
    msg.body = "This is a first email"
    #Flask支持很多，比如附件和抄送等功能，根据需要自己添加就可以
    # msg.attach 邮件附件添加
    # msg.attach("文件名", "类型", 读取文件）
    #     with app.open_resource("F:\2281393651481.jpg") as fp:
    #         msg.attach("image.jpg", "image/jpg", fp.read())
    thr = threading.Thread(target =send_async_email, args = [app,msg])#创建线程
    thr.start()

if __name__ == "__main__":
    app.run()
