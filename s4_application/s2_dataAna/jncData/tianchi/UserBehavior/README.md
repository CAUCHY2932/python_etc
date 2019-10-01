# object

User Behavior Data from Taobao for Recommendation


# https://tianchi.aliyun.com/dataset/dataDetail?dataId=649

描述

This dataset is provided by Alimama
数据列表

    数据名称上传日期大小下载
    UserBehavior.csv.zip2018-05-10905.80MB
    UserBehavior.csv.zip.md52018-05-1161.00Bytes

文档

Introduction

Dataset
File 	Description 	Feature
UserBehavior.csv 	All user behavior data 	User ID, item ID, category ID, behavior type, timestamp

UserBehavior.csv

We random select about 1 million users who have behaviors including click, purchase, adding item to shopping cart and item favoring during November 25 to December 03, 2017. The dataset is organized in a very similar form to MovieLens-20M, i.e., each line represents a specific user-item interaction, which consists of user ID, item ID, item's category ID, behavior type and timestamp, separated by commas. The detailed descriptions of each field are as follows:
Field 	Explanation
User ID 	An integer, the serialized ID that represents a user
Item ID 	An integer, the serialized ID that represents an item
Category ID 	An integer, the serialized ID that represents the category which the corresponding item belongs to
Behavior type 	A string, enum-type from ('pv', 'buy', 'cart', 'fav')
Timestamp 	An integer, the timestamp of the behavior
Note that the dataset contains 4 different types of behaviors, they are
Behavior 	Explanation
pv 	Page view of an item's detail page, equivalent to an item click
buy 	Purchase an item
cart 	Add an item to shopping cart
fav 	Favor an item
Dimensions of the dataset are
Dimension 	Number
# of users 	987,994
# of items 	4,162,024
# of categories 	9,439
# of interactions 	100,150,807

Citations

1. Han Z, Xiang L, Pengye Z, et al. Learning Tree-based Deep Model for Recommender Systems. In Proceedings of the 24th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining.
2. Han Z, Daqing C, Ziru X, et al. Joint Optimization of Tree-based Index and Deep Model for Recommender Systems. arXiv:1902.07565.

———————————————————————-以下是中文描述————————————————————————-

UserBehavior是阿里巴巴提供的一个淘宝用户行为数据集，用于隐式反馈推荐问题的研究。

数据集介绍
文件名称 	说明 	包含特征
UserBehavior.csv 	包含所有的用户行为数据 	用户ID，商品ID，商品类目ID，行为类型，时间戳

UserBehavior.csv

本数据集包含了2017年11月25日至2017年12月3日之间，有行为的约一百万随机用户的所有行为（行为包括点击、购买、加购、喜欢）。数据集的组织形式和MovieLens-20M类似，即数据集的每一行表示一条用户行为，由用户ID、商品ID、商品类目ID、行为类型和时间戳组成，并以逗号分隔。关于数据集中每一列的详细描述如下：
列名称 	说明
用户ID 	整数类型，序列化后的用户ID
商品ID 	整数类型，序列化后的商品ID
商品类目ID 	整数类型，序列化后的商品所属类目ID
行为类型 	字符串，枚举类型，包括('pv', 'buy', 'cart', 'fav')
时间戳 	行为发生的时间戳
注意到，用户行为类型共有四种，它们分别是
行为类型 	说明
pv 	商品详情页pv，等价于点击
buy 	商品购买
cart 	将商品加入购物车
fav 	收藏商品
关于数据集大小的一些说明如下
维度 	数量
用户数量 	987,994
商品数量 	4,162,024
商品类目数量 	9,439
所有行为数量 	100,150,807

论文引用

1. Han Z, Xiang L, Pengye Z, et al. Learning Tree-based Deep Model for Recommender Systems. In Proceedings of the 24th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining.
2. Han Z, Daqing C, Ziru X, et al. Joint Optimization of Tree-based Index and Deep Model for Recommender Systems. arXiv:1902.07565. 