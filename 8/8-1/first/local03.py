from threading import Thread

request = '123'

class MyThread(Thread):
    def run(self):
        global request
        request = 'abc'
        print('子线程',request)   #子线程 abc

mythread = MyThread()
mythread.start()
mythread.join()

print('主线程',request)          #主线程 abc
