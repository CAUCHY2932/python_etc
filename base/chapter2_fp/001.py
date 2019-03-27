# coding=utf8

def log(func):
    def wrapper(*args, **kwargs):
        print('call %s():'%func.__name__)
        return func(*args, **kwargs)
    return wrapper


# def log2(func):
#     def wrapper(*args, **kwargs):
#         print('niaho%s:'%func.__name__)
#         return func(*args, **kwargs)
#     return warpper

@log
def now():
    print('now')

now()