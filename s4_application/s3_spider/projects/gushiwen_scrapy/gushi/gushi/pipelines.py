# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import time

import psycopg2


class GushiPipeline(object):
    def __init__(self):
        self.conn = psycopg2.connect(database="mydb",
                                     user="postgres",
                                     password="12345678",
                                     host="127.0.0.1",
                                     port="5432")
        self.cur = self.conn.cursor()
        pass

    def process_item(self, item, spider):
        insert_sql = f"""insert into poets(name, content)values ('{item["name"]}', '{item["content"]}')
        """
        self.cur.execute(insert_sql)
        self.conn.commit()
        # t = int(time.time())
        # with open('/Users/young/codes/a_py/python_etc/s4_application/s3_spider/projects/%s.txt' % t, mode='a') as f:
        #     f.write(item)
        # return item
        pass

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()
