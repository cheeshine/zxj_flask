import time
import threading
# from threading import current_thread as getcurrent
from greenlet import getcurrent

class Local(object):

    def __init__(self):
        object.__setattr__(self,"_storage",{})

    def __setattr__(self, key, value):

        # ident = threading.get_ident()
        ident = getcurrent()   # 定制粒度更细的
        if ident in self._storage:
            self._storage[ident][key] = value
        else:
            self._storage[ident] = {key:value}

    def __getattr__(self, item):
        # ident = threading.get_ident()
        ident = getcurrent()
        return self._storage[ident][item]

local = Local()

def func(n):
    local.val = n
    time.sleep(2)
    print(local.val)

for i in range(10):
    t = threading.Thread(target=func,args=(i,))
    t.start()
