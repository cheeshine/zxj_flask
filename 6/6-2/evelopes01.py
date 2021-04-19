from envelopes import Envelope, GMailSMTP

envelope = Envelope(  # 实例化Envelope
    from_addr=(u'from@example.com', u'From Example'),  # 必选参数，发件人信息。前面是发送邮箱，后面是发送人；只有发送邮箱也可以
    to_addr=(u'to@example.com', u'To Example'),  # 必选参数，发送多人可以直接(u'user1@example.com'， u'user2@example.com')
    subject=u'Envelopes demo',  # 必选参数，邮件标题
    html_body=u'<h1>活着之上</h1>',  # 可选参数，带HTML的邮件正文
    text_body=u"I'm a helicopter!",    # 可选参数，文本格式的邮件正文
    cc_addr=u'boss1@example.com',  # 可选参数，抄送人，也可以是列表形式
    bcc_addr=u'boss2@example.com',  # 可选参数，隐藏抄送人，也可以是列表
    headers=u'',  # 可选参数，邮件头部内容，字典形式
    charset=u'',  # 可选参数，邮件字符集
)
envelope.add_attachment('/Users/bilbo/Pictures/helicopter.jpg')  # 增加附件，注意文件是完整路径，也可以加入多个附件

# Send the envelope using an ad-hoc connection...
envelope.send('smtp.163.com', login='from@example.com',
              password='password', tls=True)  # 发送邮件，分别是smtp服务器，登陆邮箱，登陆

# 或者使用共享Gmail连接发送信封...
gmail = GMailSMTP('from@example.com', 'password')
gmail.send(envelope)