# -*- encoding:utf-8 -*-
"""
    datetime 
    create by young
"""

import threading


def worker():
    """
    测试线程
    """
    print('i am a thread')
    work_t = threading.current_thread()
    print(work_t.getName())

# new_t = threading.Thread(target=worker)
# new_t.start()
# 多线程
worker()
t = threading.current_thread()
print(t.getName())

# 异步编程
# 更加充分利用cpu资源
# 单核cpu优势不明显
# 多核并行执行
# python 不能充分利用多核cpu优势
# python的多线程有点鸡肋
# 但可以开启多进程，进城切换比较麻烦，进城通信技术
# node.js 单进程，单线程

# python和nodejs适合io密集型的程序，等待较多

# python 并不完全是鸡肋
# 多线程，非常依赖于cpu计算，cpu密集型
# 但我们经常编写的属于io密集型的，请求网络资源，读写文件
# flask默认的服务器是单进程，单线程的，正式生产时多进程
# threaded = True ,开启多线程
# processes =1 多进程
