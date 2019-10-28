# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import time


class GushiPipeline(object):
    def process_item(self, item, spider):
        # t = int(time.time())
        # with open('/Users/young/codes/a_py/python_etc/s4_application/s3_spider/projects/%s.txt' % t, mode='a') as f:
        #     f.write(item)
        # return item
        pass
