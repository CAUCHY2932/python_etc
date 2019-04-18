# -*- coding:utf-8 -*-

"""
    2019/4/12 17:17 by young
"""
import os


def split_file_binary(file_name, dist_dir, chunk_size=100000, encoding='utf-8'):
    """
    二进制进行切分
    :param file_name:切分文件名
    :param dist_dir:目标文件夹
    :param chunk_size:切换大小
    :param encoding:编码方式
    :return:不返回
    """
    # 判断文件
    # os.path.ex
    if not os.path.exists(dist_dir):
        os.mkdir(dist_dir)
    # 判断文件类型
    _, suffix = os.path.splitext(file_name)
    part_num = 0

    with open(file_name, 'r', encoding=encoding) as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            part_num += 1
            file_part_name = os.path.join(dist_dir, ('part%05d' % part_num)+suffix)
            with open(file_part_name, 'w', encoding='utf-8') as f_part:
                f_part.write(chunk)


def split_file_mine(file_name, dist_dir,return_files, chunk_size=100000, encoding='utf-8'):
    """
    :param file_name:切分文件名
    :param dist_dir:目标文件夹
    :param chunk_size:切换大小
    :param encoding:编码方式
    :param return_files:生成的文件数
    :return:不返回
    """
    # 判断文件
    # os.path.ex
    if not os.path.exists(dist_dir):
        os.mkdir(dist_dir)
    # 判断文件类型
    _, suffix = os.path.splitext(file_name)
    part_num = 0

    with open(file_name, 'r', encoding=encoding) as f:
        while True:
            chunk = ''.join((f.readline() for _ in range(chunk_size)))
            if (part_num >= return_files) or (not chunk):
                break
            part_num += 1
            target_name = 'part{0:0>12}{1}'.format(part_num, suffix)
            file_part_name = os.path.join(dist_dir, target_name)
            with open(file_part_name, 'w', encoding='utf-8') as f_part:
                f_part.write(chunk)
                print('write {} file succesfully!'.format(target_name))


if __name__ == "__main__":
    split_file_mine(
        file_name='./UserBehavior.csv',
        dist_dir='./split_data_dist_dir',
        return_files=10,
        chunk_size=500000,
    )
