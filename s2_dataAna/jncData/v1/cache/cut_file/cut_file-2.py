# -*- coding:utf-8 -*-

"""
    2019/4/12 17:17 by young
"""
import os


def split_file(file_name, dist_dir,return_files, chunk_size=100000, encoding='utf-8'):

    if not os.path.exists(dist_dir):
        os.mkdir(dist_dir)
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
    split_file(
        file_name='./UserBehavior.csv',
        dist_dir='./split_data_dist_dir',
        return_files=10,
        chunk_size=500000,
    )
