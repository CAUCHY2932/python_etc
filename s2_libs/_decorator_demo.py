# coding: utf-8
import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


def deco2(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        print('do somethings')
        rv = f(*args, **kwargs)
        other = ''
        print('do somethings')
        return rv, other

    return wrapper


def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator
