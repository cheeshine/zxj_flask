from flask_mail import Message
from flask import render_template
from app import mail

sender_email = None
def configure_email(app):
	global sender_email
	sender_email = app.config['MAIL_USERNAME']

def mail_message(subject,template,to,**kwargs):
	email = Message(subject,sender=sender_email,recipients=[to])
	email.body = render_template(template + '.txt',**kwargs)
	email.html = render_template(template + '.html',**kwargs)
	mail.send(email)