# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019-05-11 12:03
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""


def compare_two_record(record1, record2):
    """
    比较函数，用来比较任意两个记录的大小，并返回较大的结果
    :param record1:
    :param record2:
    :return:
    """
    record2_list = record2.split('.')
    record1_list = record1.split('.')
    max_record = record2

    if len(record2_list) < len(record1_list):
        if record2 not in record1:
            for item in zip(record1_list, record2_list):
                if int(item[1]) < int(item[0]):
                    max_record = record1
                    break
                elif int(item[1]) > int(item[0]):
                    break
                else:
                    pass
        else:
            pass
    elif len(record2_list) > len(record1_list):
        if record2 not in record1:
            for item in zip(record1_list, record2_list):
                if int(item[1]) < int(item[0]):
                    max_record = record1
                    break
                elif int(item[1]) > int(item[0]):
                    break
                else:
                    pass
        else:
            max_record = record1
    else:
        for item in zip(record1_list, record2_list):
            if int(item[1]) < int(item[0]):
                max_record = record1
                break
            elif int(item[1]) > int(item[0]):
                break
            else:
                pass
        pass

    return max_record


if __name__ == '__main__':
    max_record = compare_two_record('14.2.3', '15.0.8')
    print(max_record)
