# -*-coding:utf-8-*-

# 20181005

# 测试输入一个函数并调用
def now():
    from datetime import datetime
    now=datetime.now()
    print(now)

f=now
f()


