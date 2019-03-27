# 插入数据库

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from . import settings
import warnings
warnings.filterwarnings("ignore")
class Spider38Pipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            port=3306,
            db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            charset='utf8',)
            # use_unicode=True)

        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()
    def process_item(self, item, spider):
        # return item
        title=item["title"]
        date=item["date"]
        content=item["content"]
        link=item["link"]
        source=item["source"]
        # print(title,date,link,source)

        try:
            insert_sql=f"""insert ignore into cms_model_test(title,date,content,link,source)values({title},{date},{content},{link},{source})"""
            print(insert_sql)
            flag=self.cursor.execute(insert_sql)
            if flag!=1:
                print(f'{title}已经存在')
                pass
            print(f'{title}已插入成功')
            self.connect.commit()

            # print()
            # insert_sql="""
            #     insert ignore into cms_model_test (title, date,content,link,source,)value(%s, %s, %s, %s, %s)
            # """.format()
            # a=(item['title'],item['date'],item['content'],item['link'],item['source'])
            # flag=self.cursor.execute(insert_sql,a)
            # if flag !=1:# 说明已经存在此记录
            #     title=item["title"]
            #     print(f'{title}已经存在')
            #     pass
            # else:
            #     self.connect.commit()
        except Exception as e:
            print(e)


        # try:
        #     # 查重处理
        #     self.cursor.execute(
        #         """select * from doubanmovie where img_url = %s""",
        #         item['img_url'])
        #     # 是否有重复数据
        #     repetition = self.cursor.fetchone()
        #
        #     # 重复
        #     if repetition:
        #         pass
        #
        #     else:
        #         # 插入数据
        #         self.cursor.execute(
        #             """insert into cms_model_test(title, date, content, link ,source,)
        #             value (%s, %s, %s, %s, %s)""",
        #             (item['title'],
        #              item['date'],
        #              item['content'],
        #              item['link'],
        #              item['source'],))
        #
        #     # 提交sql语句
        #     self.connect.commit()
        #
        # except Exception as error:
        #     # 出现错误时打印错误日志
        #     # log(error)
        #     print(error)
        # return item