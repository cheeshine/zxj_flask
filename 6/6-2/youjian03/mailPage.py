from flask import Flask,render_template,request
import send2

app = Flask(__name__)

@app.route("/")
def my_form(name=None):
    return  render_template("mailForm.html",name=name)

@app.route("/",methods=['POST'])
def my_form_post():
    if request.method=='POST':
        myMailId = request.form.get("myMailId")
        otherMailIds  = request.form.get("otherMailIds").strip().split(',')
        sub = request.form.get("sub")
        body = request.form.get("body")
        send2.mailSend(myMailId,otherMailIds,sub,body)
        return "mail sent!!!"

if __name__=="__main__":
    app.run()

    