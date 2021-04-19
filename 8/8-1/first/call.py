class Entity:#调用实体来改变实体的位置
    def __init__(self, size, x, y):
        self.x, self.y = x, y
        self.size = size

    def __call__(self, x, y):
        '''改变实体的位置'''
        self.x, self.y = x, y

e = Entity(1, 2, 3) #创建实例
e(4, 5) #实例可以象函数那样执行，并传入x y值，修改对象的x y
