from flask import Flask,url_for,render_template,request,make_response,session,flash,get_flashed_messages

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aaa bbb ccc'

@app.route("/addflash")
def addFlash():
   flash("bling bling")
   return "added a flash"

@app.route("/getFlash/")
def getFlash():
   msgs = get_flashed_messages()
   msgStr = ""
   for msg in msgs:
       msgStr += msg+","
   return msgStr


if __name__ == '__main__':
    app.run()
