from functools import partial

class Foo(object):

    def __init__(self):
        self.request = "request"
        self.session = "session"

foo = Foo()

def func(args):
    return getattr(foo,args)

re_func = partial(func,'request')
se_func = partial(func,'session')

print(re_func())
