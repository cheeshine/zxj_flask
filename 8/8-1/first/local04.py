from threading import Thread
from werkzeug.local import Local

locals = Local()
locals.request = '123'

class MyThread(Thread):
    def run(self):
        locals.request = 'abc'
        print('子线程',locals.request)   #子线程 abc

mythread = MyThread()
mythread.start()
mythread.join()

print('主线程',locals.request)          #主线程 123
