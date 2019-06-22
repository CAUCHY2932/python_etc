# coding:utf-8


def is_isbn_or_key(word):
    """
    测试一个传入的字符串是isbn还是关键词
    """
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_key = word.replace('-', '')
    if '-' in word and short_key == 10 and short_key.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key
