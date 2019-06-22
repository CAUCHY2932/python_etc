# -*- coding:utf-8 -*-

"""
    2019/4/22 16:02 by young
"""


"""
测试键盘强制中断，之后，记录日志和写入文件等功能
"""
import time


def log_to_file():
    pass


def go(num):
    print('process has start and will sleep {} seconds.'.format(num))
    # time.sleep(num)
    try:
        print('we will sleep more {} seconds to have a good rest!'.format(num))
        # 1/0

        time.sleep(num)
        raise ZeroDivisionError
    except Exception as e:
        raise e
        # except KeyboardInterrupt:
        # print('oops! we have been interrupt by {}!'.format(e))


def replace_num(old_str):
    import re
    new_str = re.sub('[0-9]', '', old_str)
    return new_str


# filter_num_str_func = lambda old_str: filter(lambda x: x not in '0123456789', old_str)


if __name__ == "__main__":
    # go(10)
    # print(replace_num('glwjegj0980823jklgjf'))
    # filter_num_str_func('nogjow234200jkjglsw')
    old_str = 'jgwoje01394ojisfo802ru'
    str_lst = filter(lambda x: x not in '0123456789', old_str)

    # str_lst2 = filter(lambda x: x not in '0123456789', list(old_str))
    # print(str(str_lst2))
    print(''.join([item for item in str_lst]))

    str_new = ''.join([i for i in filter(lambda x: x not in '0123456789', old_str)])


    # for item in str_lst:
    #     print(item)

    # for item in old_str:
    #     print(item)
