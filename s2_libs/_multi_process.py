# coding: utf-8
from multiprocessing import Process
import os
from multiprocessing import Pool
import os
import time
import random

# 子进程要执行的代码


def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


def run_multiprocess_simple():
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


def run_multiprocess_poll():
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')


"""
爬虫中使用的多进程
from multiprocessing import Pool
import time
import os
"""


def print_test(n):
    time.sleep(3)
    # getppid() 获取父进程的代码 getpid() 获取当前进程的代码
    print('进程id是{}，打印的数字是{}'.format(os.getpid(), n))


def use_func():
    pool = Pool(3)
    print('test start')
    t1 = time.time()
    groups = (x for x in range(78))
    pool.map(print_test, groups)
    pool.close()
    pool.join()
    print('test over, use {}'.format(time.time()-t1))
