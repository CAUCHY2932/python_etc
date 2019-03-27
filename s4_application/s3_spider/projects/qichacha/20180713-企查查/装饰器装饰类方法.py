def decorator(args):
    def _deco(func):
        def _func(self):
            print args
            print 'gooooo'
            func(self)
            print 'fooo'
        return _func

    return _deco


https://segmentfault.com/q/1010000004188165



def log(func):
    def wrapper(self):
        print('log')
        func(self)
    return wrapper


class Test():
    @log
    def hello(self):
        print('hello')

t = Test()
t.hello()