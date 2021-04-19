from flask import Blueprint

app02=Blueprint('app02',__name__)

@app02.route('/')
def show():
    return 'app02.hello'