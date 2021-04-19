from flask import Blueprint

app01=Blueprint('app01',__name__)

@app01.route('/')
def show():
    return 'app01.hello'