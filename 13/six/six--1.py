from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

USERS = {
    '1': {'name': '赵敏', 'count': 1},
    '2': {'name': '芷若', 'count': 3},
    '3': {'name': '小昭', 'count': 3},
}


@app.route('/user/list')
def user_list():
    import time
    return render_template('index.html', users=USERS)


@app.route('/vote', methods=['POST'])
def vote():
    uid = request.form.get('uid')
    USERS[uid]['count'] += 1
    return "投票成功"


@app.route('/get/vote', methods=['GET'])
def get_vote():
    return jsonify(USERS)


if __name__ == '__main__':
    app.run(threaded=True)
