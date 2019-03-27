# coding:utf-8


import os
import re


def handle(file_name):
    with open(file_name, 'r') as f:
        for _ in range(10):
            line = f.readline().strip()
            # new_line = re.split(r' +|\t', line)
            new_line = re.findall(r'[\u4e00-\u9fa5]+|\w+', line) # 基本汉字编码
            print(new_line)


if __name__ == '__main__':
    handle('./xz.csv')
