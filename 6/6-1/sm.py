import smtplib,email
from p_email import mypass

chst = email.charset.Charset(input_charset='utf-8')
header = ("From: %s\nTo: %s\nSubject: %s\n\n"
       % ("guanxijing820111@sina.com",
          "好人" ,
          chst.header_encode("Python smtplib 测试！")))
body = "你好！"
email_con = header.encode('utf-8') + body.encode('utf-8')
smtp = smtplib.SMTP("smtp.sina.com")
smtp.login("guanxijing820111@sina.com",mypass)
smtp.sendmail("guanxijing820111@sina.com","371972484@qq.com",email_con)
smtp.quit()
