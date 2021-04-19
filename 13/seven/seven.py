from flask import Flask, render_template, request, jsonify, session
import uuid
import queue

app = Flask(__name__)
app.secret_key = 'asdfasdfasd'

USERS = {
    '1': {'name': '赵敏', 'count': 1},
    '2': {'name': '芷若', 'count': 0},
    '3': {'name': '小昭', 'count': 0},
}

QUEQUE_DICT = {
    # 'asdfasdfasdfasdf':Queue()
}


@app.route('/user/list')
def user_list():
    user_uuid = str(uuid.uuid4())
    QUEQUE_DICT[user_uuid] = queue.Queue()

    session['current_user_uuid'] = user_uuid
    return render_template('index.html', users=USERS)


@app.route('/vote', methods=['POST'])
def vote():
    uid = request.form.get('uid')
    USERS[uid]['count'] += 1
    for q in QUEQUE_DICT.values():
        q.put(USERS)
    return "投票成功"


@app.route('/get/vote', methods=['GET'])
def get_vote():
    user_uuid = session['current_user_uuid']
    q = QUEQUE_DICT[user_uuid]

    ret = {'status': True, 'data': None}
    try:
        users = q.get(timeout=10)
        ret['data'] = users
    except queue.Empty:
        ret['status'] = False

    return jsonify(ret)


if __name__ == '__main__':
    app.run(threaded=True)

