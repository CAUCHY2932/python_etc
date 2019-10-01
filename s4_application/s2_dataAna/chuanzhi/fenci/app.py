# -*- coding:utf-8 -*-

"""
    2019/4/2 16:34 by young
"""
import jieba as ja

seg_list = ja.cut('我来到北京清华大学', cut_all=True)
print('全模式：' + '/ '.join(seg_list)) # 全模式

seg_list = ja.cut('我来到北京清华大学', cut_all=False)
print('精确模式：' + '/ '.join(seg_list))


seg_list = ja.cut('他来到网易杭研大厦')
print('默认模式:' + '/ '.join(seg_list)) # 默认是精确模式


seg_list = ja.cut_for_search('小明硕士毕业于中国科学院计算所，后再日本京都大学深造')
print('搜索引擎模式:' + '/ '.join(seg_list)) # 搜索引擎模式
