# -*- coding:utf-8 -*-

"""
    2019/4/19 10:31 by young
"""


from skeleton.pack_record_skeleton import Cutter, MongodbSaver, Reader


def go5():
    file_name = r'C:\Users\LvYangyang\Downloads\sample_test.tar\sample_test\sample_skeleton_test.csv'
    line_num = 10000
    mongodb_url = 'localhost'
    mongodb_name = 'user_new'
    mongodb_table = 'skeleton_1'

    with Reader(file_name, line_num) as rd:
        rd_gen = rd.read()

    for item in rd_gen:
        with Cutter(item) as ct:
            ct.cut_to_record()
            with MongodbSaver(mongodb_url, mongodb_name, mongodb_table) as ms:
                ms.save(ct.data)


if __name__ == '__main__':

    go5()
