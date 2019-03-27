# coding:utf-8

def read_file_1(file_name):
    with open(file_name, 'r') as f:
        return f.read()


def read_file_2(file_name):
    with open(file_name, 'r') as f:
        return f.readlines()


def read_file_3(file_name, block_size=1024):
    with open(file_name, 'r') as f:
        chunk = f.read(block_size)
        if chunk:
            yield chunk
        else:
            return


def read_file_4(file_name, block_size=1024):
    with open(file_name, 'r') as f:
        chunk = f.read(block_size)
        while chunk:
            yield chunk
            chunk = f.read(block_size)
        return


"""

将文件切分成小段，每次处理完小段内容后，释放内存

这里会使用yield生成自定义可迭代对象， 即generator， 每一个带有yield的函数就是一个generator。 
"""
