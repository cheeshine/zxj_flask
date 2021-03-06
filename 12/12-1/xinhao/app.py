from flask import Flask, current_app
from blinker import Namespace

app = Flask(__name__)
app.secret_key = 'WOO'
my_signals = Namespace()

def moo_signal(app, message, **extra):
    print(message)

moo = my_signals.signal('moo')
moo.connect(moo_signal, app)

@app.route('/', methods=['POST', 'GET'])
def home():
    moo.send(current_app._get_current_object(), message='大家好')
    moo.send(current_app._get_current_object(), message='你正在访问')
    moo.send(current_app._get_current_object(), message='主页')
    return 'toot'


if __name__ == '__main__':
    app.run(debug=True)

