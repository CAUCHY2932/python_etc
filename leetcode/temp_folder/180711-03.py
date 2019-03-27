# coding:utf-8
# time:20180711
# author:yang

# title:回文数

# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

# 示例 1:

# 输入: 121
# 输出: true

# 示例 2:

# 输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

# 示例 3:

# 输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y=int(x)
        if x<0:
            ret=False
        elif x==0:
            ret=True
        else:
            sum=0
            while x:
                m=int(x%10)
                x=int(x/10)
                sum=sum*10+m
            if sum==y:
                ret=True
            else:
                ret=False
        return ret