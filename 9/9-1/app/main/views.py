from flask import Blueprint

main=Blueprint('main',__name__)

@main.route('/')
def show():
    return 'main.hello'