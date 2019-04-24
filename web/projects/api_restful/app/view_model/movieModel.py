# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/4/24 13:38
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
import json


class MovieViewModel(object):
    def __init__(self):
        # self.total = 0
        # self.movies = []

        self.rating_average = ''
        self.title = ''
        self.year = ''
        self.id = ''
        self.subtype = ''
        self.origin_title = ''
        self.genres = ''
        self.image = ''

    # def single_data(self, data):
    #     self.id = data['id']
    #     self.origin_title = data['original_title']
    #     self.subtype = data['subtype']
    #     self.rating_average = data['rating']['average']
    #     self.title = data['title']
    #     self.year = data['year']
    #     self.genres = '|'.join(data['genres'])
    #     self.image = data['images']['large']
    #
    # def collection_data(self, data_collections):
    #     # data_collections = json.dumps(data_collections)
    #     # data_collections = dict(data_collections)
    #     self.total = data_collections['total']
    #     self.movies = [self.single_data(data) for data in data_collections['subjects']]


# class MovieCollection(object):
#     def __init__(self):
#         self.total = 0
#         self.movies = []
#
#     def fill(self, data_collections):
#         self.total = data_collections['total']
#         self.movies = []
#     pass


