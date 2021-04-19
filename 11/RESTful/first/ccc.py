from flask import Flask, abort, url_for, make_response, jsonify
from flask_restful import Resource, Api, reqparse, fields, marshal
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()
tasks = [
    {
        'id':1,
        'title':'白鹿原',
        'description':'《白鹿原》可能是当代中国，最好的一部家族史小说，它也完全有资格，在文学史树立起属于自己的丰碑。',
        'done':False
    },
    {
        'id':2,
        'title':'嫌疑人',
        'description':'这部电影光是选角就让我非常喜欢，孔侑大叔的形象超级贴合一个冷面杀手和铁血柔情的结合体，演技也是超棒，完全把妻子被杀时的绝望与愤怒、寻找女儿的决心与担忧、女儿被找到后的温柔刻画的淋漓尽致。',
        'done':False
    }
]
task_fields = {
    'title': fields.String,
    'description': fields.String,
    'done': fields.Boolean,
    'uri': fields.Url('task')
}

class TaskListAPI(Resource):
    decorators = [auth.login_required]
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, required=True,
            help='No task title provided', location='json')
        self.reqparse.add_argument('description', type=str, default="",
            location='json')
        self.reqparse.add_argument('done', type=bool, location='json')
        super(TaskListAPI, self).__init__()

    def get(self):
        return jsonify(list(map(marshal, tasks, [task_fields for i in range(len(tasks))])))

    def post(self):
        task = {}
        args = self.reqparse.parse_args()
        task['id'] = tasks[-1]['id']+1
        for k, v in args.items():
            if v != None:
                task[k] = v
        tasks.append(task)
        return {'task':task}, 201

class TaskAPI(Resource):
    decorators = [auth.login_required]
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, location='json')
        self.reqparse.add_argument('description', type=str, location='json')
        self.reqparse.add_argument('done', type=bool, location='json')
        super(TaskAPI, self).__init__()

    def get(self, id):
        task = list(filter(lambda x: x['id']==id, tasks))
        if len(task)==0:
            abort(404)
        task = task[0]
        return {'task': marshal(task, task_fields)}

    def put(self, id):
        task = list(filter(lambda t: t['id'] == id, tasks))
        if len(task) == 0:
            abort(404)
        task = task[0]
        args = self.reqparse.parse_args()
        for k, v in args.items():
            if v != None:
                task[k] = v
        # return jsonify(task=make_public_task(task))
        return {'task': marshal(task, task_fields)}

    def delete(self, id):
        task = list(filter(lambda x: x['id']==id, tasks))
        if len(task)==0:
            abort(404)
        task = task[0]
        tasks.remove(task)
        return {'result':True}

api.add_resource(TaskListAPI, '/todo/api/v1.0/tasks', endpoint='tasks')
api.add_resource(TaskAPI, '/todo/api/v1.0/tasks/<int:id>', endpoint='task')

def make_public_task(task):
    new_tasks = {}
    for field in task:
        if field=='id':
            new_tasks['uri'] = url_for('task', id=task['id'], _external=True)
        else:
            new_tasks[field] = task[field]
    return new_tasks

@auth.get_password
def get_password(username):
    if username=='abc':
        return 'abc'
    return None

@auth.error_handler
def unauthorized():
    # return make_response(jsonify(error='Unauthorized access'), 401)
    return make_response(jsonify(error='Unauthorized access'), 403)

if __name__ == '__main__':
    app.run(debug=True)
