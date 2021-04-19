class Foo(object):
    def __init__(self):
        self.name = "boo"

    def __getattr__(self, item):
        print("调用__getattr__了")

    def __setattr__(self, key, value):
        print("调用__setattr__方法了")

    def __delattr__(self, item):
        print("调用__delattr__")


foo = Foo()
ret = foo.xxx    # 输出     调用__getattr__了
foo.age = 18    # 调用__setattr__方法了
del foo.age   #  输出  调用__delattr__
