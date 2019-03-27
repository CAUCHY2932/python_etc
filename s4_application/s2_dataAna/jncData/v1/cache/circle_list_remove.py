# -*- coding:utf-8 -*-

"""
    2019/4/19 8:53 by young
"""


# 在一些时候，我们需要遍历某个列表，然后从中处理数据，有时，我们需要在运行时，动态改变我们所遍历对象的值
# 例如，我们在编写如： for item in a_list时，对item进行处理的同时，也需要对a_list进行修改，我们应尽量避免这种写法
# 而是，在遍历之前，就尽量利用集合的特殊性质进行去重，如：set(a_list)，之后可以进行遍历操作

def remove_item_circle_list():
    demo_list = [item for item in range(20)] * 2
    print(demo_list)

    k = 0
    for item in demo_list:
        if item in [item for item in range(20)]:
            demo_list.remove(item)
            print(demo_list)
        k += 1

    print(k)
# 先去重，再使用遍历列表的方式


def list_to_set(demo_list):
    demo_set = set()
    demo_list = list(demo_set)
    demo_set.remove()


def set_test():

    demo_set2 = {item for item in range(18)}

    for item in demo_set2:
        print(item)


def remove_item(handle_list):

    temp_set = set(handle_list)
    # for item in temp_set:

    pass


if __name__ == "__main__":
    pass
