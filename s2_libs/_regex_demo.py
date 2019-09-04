# coding:utf-8

def a(row):
    import re
    res = re.compile('([0-9]{1})([A-Z]{2})')
    
    return res.findall(row)
    # return res.split(row)
print(a('5BC'))


def find_all_demo():

    pass

def search_demo():

    pass

def match_demo():

    pass




