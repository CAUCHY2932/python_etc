# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019-06-26 23:48
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
from multiprocessing import Pool
import time
import os


def print_test(n):
    time.sleep(3)
    # getppid() 获取父进程的代码 getpid() 获取当前进程的代码
    print('进程id是{}，打印的数字是{}'.format(os.getpid(), n))


if __name__ == '__main__':
    pool = Pool(3)
    print('test start')
    t1= time.time()
    groups = (x for x in range(78))
    pool.map(print_test, groups)
    pool.close()
    pool.join()
    print('test over, use {}'.format(time.time()-t1))





