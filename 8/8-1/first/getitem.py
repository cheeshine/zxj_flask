class Foo(object):

    def __init__(self):
        self.name = "boo"

    def __getitem__(self, item):
        print("调用__getitem__了")
        if item in self.__dict__:
            return self.__dict__[item]

    def __setitem__(self, key, value):
        print("调用__setitem__方法了")
        self.__dict__[key] = value

    def __delitem__(self, key):
        print("调用__delitem__")
        del self.__dict__[key]

foo = Foo()
ret = foo["name"]
# print(ret)     		# 输出：调用__getitem__了      boo
foo["age"] = 18
# print(foo["age"])   # 输出：调用__setitem__方法了   调用__getitem__了    18
del foo["age"]   		#  输出：调用__delitem__
