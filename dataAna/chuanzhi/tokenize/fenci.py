# -*- coding:utf-8 -*-

"""
    2019/4/2 15:49 by young
"""
# 分词
import jieba


seg_list = jieba.cut('我是中国人，我爱自己的祖国', cut_all=True)

print('全模式：' + '/ '.join(seg_list))




seg_list = jieba.cut('我是中国人，我爱自己的祖国', cut_all=False)

print('精确模式：' + '/ '.join(seg_list))
