# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/4/25 11:19
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""


# def get_data_by_keyword(q):
#     mg = MovieGetter()
#     mg.search_by_keyword(q)
#     movies = MovieViewModel()
#     movies.collection_data(mg.detail)
#     # return MysqlStorage.insert_to_mysql(id)
#     return jsonify({'items': movies.movies,
#                     'total': movies.total})


# 将以上代码进行过精简

# 抽象为
# state1
# if xx:
#     state2
#     state3
# else:
#     state2
#     state3
#
