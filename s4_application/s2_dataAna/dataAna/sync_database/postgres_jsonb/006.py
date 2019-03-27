# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/6/4 10:00
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
from sqlalchemy import Column, Table, MetaData, create_engine, Integer
from sqlalchemy.dialects.postgresql import JSONB
import requests
import json


class AccessData(object):

    @classmethod
    def get_content(cls, url, return_json=True):
        headers = {'Content-Type': 'application/json'}
        try:
            resp = requests.get(url, headers=headers)
            if resp.status_code == 200:
                return (0, resp.json()) if return_json else (0, resp.text)
            return (1, json.dumps({})) if return_json else (1, '')
        except requests.exceptions:
            print('Invalid URL!\n')
            return -1, ''

    @classmethod
    def get_content_with_token(cls, url, payload, return_json=True):
        headers = {'Content-Type': 'application/json'}
        try:
            resp = requests.get(url, json=payload, headers=headers)
            if resp.status_code == 200:
                return (0, resp.json()) if return_json else (0, resp.text)
            return (1, json.dumps({})) if return_json else (1, '')
        except requests.exceptions:
            print('Invalid URL!\n')
            return -1, ''

    @classmethod
    def post_content_with_token(cls, url, payload, return_json=True):
        headers = {'Content-Type': 'application/json'}
        try:
            resp = requests.post(url, json=payload, headers=headers)
            if resp.status_code == 200:
                return (0, resp.json()) if return_json else (0, resp.text)
            return (1, json.dumps({})) if return_json else (1, '')
        except requests.exceptions:
            print('Invalid URL!\n')
            return -1, ''

    @classmethod
    def put_content_with_token(cls, url, payload, return_json=True):
        headers = {'Content-Type': 'application/json'}
        try:
            resp = requests.put(url, json=payload, headers=headers)
            if resp.status_code == 200:
                return (0, resp.json()) if return_json else (0, resp.text)
            return (1, json.dumps({})) if return_json else (1, '')
        except requests.exceptions:
            print('Invalid URL!\n')
            return -1, ''


def handle_resp():
    pass


def db_op(data):

    engine = create_engine('postgresql://postgres:123456@127.0.0.1:5432/postgres', echo=True)
    metadata = MetaData(bind=engine)
    # engine = create_engine("postgresql://scott:tiger@localhost/test")
    data_table = Table('data_table', metadata,
                       Column('id', Integer, primary_key=True),
                       Column('data', JSONB)
                       )

    with engine.connect() as conn:
        conn.execute(
            data_table.insert(),
            data=data
            # data={"key1": "value1", "key2": "value2"}
        )

    # with engine.connect() as conn:
    #     conn.execute(
    #         data_table.create(conn),
    #         data_table.insert(),
    #         data=data
    #         # data={"key1": "value1", "key2": "value2"}
    #     )


if __name__ == '__main__':
    # db_op(json.dumps({'a': 1, 'b': '3', 'c': 8})) # 这里不要存json化，统一使用字典格式
    # db_op({'a': 1, 'b': '3', 'c': 8})
    db_op('niaho')