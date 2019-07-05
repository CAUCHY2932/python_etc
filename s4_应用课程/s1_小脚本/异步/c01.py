# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/7/5 14:31
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
import asyncio


async def hello(first_print, second_print):
    print(first_print)
    await asyncio.sleep(1)
    print(second_print)


asyncio.run(hello("welcome", "Good-bye"))
