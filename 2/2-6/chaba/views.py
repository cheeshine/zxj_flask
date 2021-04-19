from flask.views import View
from flask import render_template

from myexceptions import AuthenticationException

class ParentView(View):
    def get_template_name(self):
        raise NotImplementedError()

    def render_template(self, context):
        return render_template(self.get_template_name(), **context)

    def dispatch_request(self):
        context = self.get_objects()
        return self.render_template(context)

class UserView(ParentView):
    def get_template_name(self):
        raise AuthenticationException('test')
        return 'users.html'

    def get_objects(self):
        return {}
