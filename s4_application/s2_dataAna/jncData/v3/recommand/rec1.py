# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/4/30 12:30
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
from surprise import Dataset
from surprise import KNNBaseline
import io


def read_item_names():
    file_name = ('D:/python_learn_multiple/ml-100k/u.item')
    rid_to_name = {}
    name_to_id = {}
    with io.open(file_name, 'r', encoding='ISO-8859-1') as f:
        for line in f:
            line = line.split('|')
            rid_to_name[line[0]] = line[1]
            name_to_id[line[1]] = line[0]
        return rid_to_name, name_to_id


data = Dataset.load_builtin('ml-100k')
trainset = data.build_full_trainset()
sim_options = {'name': 'pearson_baseline', 'user_based': False}
algo = KNNBaseline(sim_options=sim_options)
algo.fit(trainset)

rid_to_name, name_to_id = read_item_names()
# print(name_to_id)

toy_story_raw_id = name_to_id['Now and Then (1995)']
# print(toy_story_raw_id)

toy_story_inner_id = trainset.to_inner_iid(toy_story_raw_id)
# print(toy_story_inner_id)

toy_story_neighbors = algo.get_neighbors(toy_story_inner_id, k=10)
# print(toy_story_neighbors)

toy_story_neighbors = (trainset.to_raw_iid(inner_id) for inner_id in toy_story_neighbors)
toy_story_neighbors = (rid_to_name[rid] for rid in toy_story_neighbors)
for item in toy_story_neighbors:
    print(item)
