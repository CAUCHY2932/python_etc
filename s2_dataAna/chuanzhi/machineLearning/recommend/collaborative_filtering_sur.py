# # -*- coding:utf-8 -*-
#
# """
#     2019/4/3 15:28 by young
# """
# # 使用surprise库进行推荐系统算法分析
#
# from surprise import SVD
# from surprise import Dataset
# from surprise.model_selection import cross_validate
#
#
#
# class RecommendSystem(object):
#
#     def __init__(self, filename, sep, **format):
#         self.filename = filename
#         self.sep = sep
#         self.format = format
#
#         # 训练参数
#         self.k = 100
#         self.min_values = 10
#         self.post_normalize = True
#
#         self.svd = SVD()
#
#         # 判断是否加载
#         self.is_load = False
#
#         # 添加数据处理
#         self.data = Data()
#
#         # 添加模型评估
#         self.rmse = RMSE()
#
#     def get_data(self):
#         """
#         获取数据
#         :return: None
#         """
#         # 如果模型不存在
#         if not os.path.exists(tmpfile):
#             # 如果数据文件不存在
#             if not os.path.exists(self.filename):
#                 sys.exit()
#             # self.svd.load_data(filename=self.filename, sep=self.sep, format=self.format)
#             # 使用Data()来获取数据
#             self.data.load(self.filename, sep=self.sep, format=self.format)
#             train, test = self.data.split_train_test(percent=80)
#             return train, test
#         else:
#             self.svd.load_model(tmpfile)
#             self.is_load = True
#             return None, None
#
#
#     def train(self, train):
#         """
#         训练模型
#         :param train: 训练数据
#         :return: None
#         """
#         if not self.is_load:
#             self.svd.set_data(train)
#             self.svd.compute(k=self.k, min_values=self.min_values, post_normalize=self.post_normalize, savefile=tmpfile[:-4])
#         return None
#
#     def rs_predict(self, itemid, userid):
#         """
#         评分预测
#         :param itemid: 电影id
#         :param userid: 用户id
#         :return: None
#         """
#         score = self.svd.predict(itemid, userid)
#         print "推荐的分数为：%f" % score
#         return score
#
#     def recommend_to_user(self, userid):
#         """
#         推荐给用户
#         :param userid: 用户id
#         :return: None
#         """
#         recommend_list = self.svd.recommend(userid, is_row=False)
#
#         # 读取文件里的电影名称
#         movie_list = []
#
#         for line in open(moviefile, "r"):
#             movie_list.append(' '.join(line.split("::")[1:2]))
#
#         # 推荐具体电影名字和分数
#         for itemid, rate in recommend_list:
#             print "给您推荐了%s,我们预测分数为%s" %(movie_list[itemid],rate)
#         return None
#
#     def evaluation(self, test):
#         """
#         模型的评估
#         :param test: 测试集
#         :return: None
#         """
#         # 如果模型不是直接加载
#         if not self.is_load:
#
#             # 循环取出测试集里面的元组数据<评分，电影，用户>
#             for value, itemid, userid in test.get():
#                 try:
#                     predict = self.rs_predict(itemid, userid)
#                     self.rmse.add(value, predict)
#                 except KeyError:
#                     continue
#             # 计算返回误差（均方误差）
#             error = self.rmse.compute()
#
#             print "模型误差为%s:" % error
#
#         return None
#
#
# if __name__ == "__main__":
#     rs = RecommendSystem("./ml-1m/ratings.dat", "::", row=1, col=0, value=2, ids=int)
#     train, test = rs.get_data()
#     rs.train(train)
#     rs.evaluation(test)
#     # rs.rs_predict(1,1)
#     rs.recommend_to_user(1)
