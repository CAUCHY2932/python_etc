# coding:utf-8


import threading
from werkzeug.local import Local, LocalStack


st = LocalStack()

for item in range(10):
    st.push(item)

for item in range(10):
    print(st.top)
    print(st.pop())


