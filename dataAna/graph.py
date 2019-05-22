# coding:utf-8
import numpy as np


# 修改圈的子函数
def modify_circle(a, l, c):
    """
        a为矩阵
        l为
        c为初始圈
    """
    for _ in range(l):
        flag = 0  # 退出标志
        for m in range(l - 2):
            for n in range(m + 1, l):
                if (a[c[m], c[n]] + a[c[m + 1], c[n + 1]]) < (a[c[m], c[m + 1]] + a[c[n], c[n + 1]]):
                    c[m + 1:n:1] = c[n - 1:m:-1]  # numpy 支持局部逆置
                    flag = flag + 1  # 修改一次，标志加一
        if flag == 0:  # 一条边也没有修改，就返回
            long = 0  # 圈长的初始值
            for i in range(1, l + 1):
                long = long + a[c[i], c[i + 1]]  # 求改良圈的长度
            circle = c  # 返回修改圈
            print('has no change')
            return circle, long
        print('has changed')
        return c, 0


def go():
    # a = np.zeors(6)
    a = [[0, 56, 35, 21, 51, 60],
         [56, 0, 21, 57, 78, 70],
         [35, 21, 0, 36, 68, 68],
         [21, 57, 36, 0, 51, 61],
         [51, 78, 68, 51, 0, 13],
         [60, 70, 68, 61, 13, 0],
         ]
    arr = np.array(a)
    # print(arr)
    # print(type(arr))
    l = len(arr)
    # print(l)
    # c = np.array([5, 1, 4, 6, 5]) - np.array([1, 1, 1, 1, 1, 1, 1]) # 这里要和Matlab里面的下标进行处理
    c = np.array([1, 2, 3, 4, 5, 6, 1]) - np.array([1, 1, 1, 1, 1, 1, 1])  # 这里要和Matlab里面的下标进行处理
    print(c)
    # print(arr[2,3])
    circle, long = modify_circle(arr, l, c)
    print(circle, long)


if __name__ == "__main__":
    go()
