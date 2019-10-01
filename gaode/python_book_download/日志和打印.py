# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/6/25 16:59
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
import sys


class Loggers(object):
    def __init__(self, filename='default.log'):
        self.filename = filename
        self.terminal = sys.stdout
        self.log = open(filename, 'a')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass


sys.stdout = Loggers("./6732.log")

print('nihaosdfasfdas')
