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


class AccessData(object):

    @classmethod
    def get_content(cls, url, json=True):
        headers = {'Content-Type': 'application/json'}
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            return resp.json() if json else resp.text
        return {} if json else ''

    @classmethod
    def get_content_with_token(cls, url, payload, json=True):
        headers = {'Content-Type': 'application/json'}
        resp = requests.get(url, json=payload, headers=headers)
        if resp.status_code == 200:
            return resp.json() if json else resp.text
        return {} if json else ''

    @classmethod
    def post_content_with_token(cls, url, payload, json=True):
        headers = {'Content-Type': 'application/json'}
        resp = requests.get(url, json=payload, headers=headers)
        if resp.status_code == 200:
            return resp.json() if json else resp.text
        return {} if json else ''

    @classmethod
    def put_content_with_token(cls, url, payload, json=True):
        headers = {'Content-Type': 'application/json'}
        resp = requests.get(url, json=payload, headers=headers)
        if resp.status_code == 200:
            return resp.json() if json else resp.text
        return {} if json else ''


def op():
    metadata = MetaData()
    engine = create_engine("postgresql://scott:tiger@localhost/test")
    data_table = Table('data_table', metadata,
                       Column('id', Integer, primary_key=True),
                       Column('data', JSONB)
                       )

    with engine.connect() as conn:
        conn.execute(
            data_table.insert(),
            data={"key1": "value1", "key2": "value2"}
        )

