# 加书名号
from contextlib import contextmanager

@contextmanager
def book_mark():
    print(' <', end='')
    yield
    print('> ', end='')

# 调用
with book_mark():
    print('且将生活一饮而尽', end='')
