# coding:utf-8

class ShareState:
    def __init__(self):
        self._lock = lock()
        self._state = defaultdict(int)
        
