from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'  # you need to set a secret key for security purposes


@app.route('/')
def index():
    if 'counter' in session.keys():
        session['counter'] += 1
        print('得到计数器')
        counter = session['counter']
        print(counter)
        return render_template('index.html')
    else:
        session['counter'] = 0
        counter = session['counter']
        print('没有计数器')
        print(counter)
        return render_template('index.html')


@app.route('/add2')
def add2():
    return render_template('add2.html')


@app.route('/process', methods=['POST'])
def process():
    session['counter'] += 2
    return redirect('/add2')


@app.route('/reset')
def reset():
    return render_template('reset.html')


@app.route('/doreset', methods=['POST'])
def doreset():
    session['counter'] = 1
    return redirect('/reset')

if __name__ == '__main__':
    app.run(debug=True)  # run our server
