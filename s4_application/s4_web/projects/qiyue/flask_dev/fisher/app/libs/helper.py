# -*- coding:utf-8 -*-
__author__ = 'young'


def is_isbn_or_key(word):
    """
    描述
    :param word:
    :return:
    """
    isbn_or_key = ''
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    # 多个and子句，耗费资源少的排在前面
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key



if __name__ == '__main__':
    pass
