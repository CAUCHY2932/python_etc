# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/7/5 10:45
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
import glob

# 正则查找本地文件夹


current_dir = './*.md'


for item in glob.glob(current_dir):
    print(item)
