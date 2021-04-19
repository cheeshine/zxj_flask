from flask import Flask, request, redirect, render_template, session
app = Flask(__name__)
app.secret_key = "parseltongue"

@app.route('/')
def index():
    if session.get('x', None) == None:
        session['x'] = 0
    else:
        session['x'] += 1
    print(session['x'])
    return render_template('counter.html')

@app.route('/double', methods=['POST'])
def double():
    session['x'] += 1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['x'] = 0
    return redirect('/')


if __name__=='__main__':
    app.run(debug = True)
