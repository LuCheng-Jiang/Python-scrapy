# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from BOOK import settings
import pymysql

'''

MYSQL_HOST = '192.168.241.100'
MYSQL_DB_NAME='book'
MYSQL_PORT =3306
MYSQL_USER = 'root'
MYSQL_PASSWORD = '@Ab123456-'
'''
class BookPipeline(object):

    #1.Python和mysql服务器建立关系
    def open_spider(self,spider):
        self.connc = pymysql.Connect(
            host = settings.MYSQL_HOST,
            database = settings.MYSQL_DB_NAME,
            port = settings.MYSQL_PORT,
            user=  settings.MYSQL_USER,
            password = settings.MYSQL_PASSWORD,
            charset = 'utf8',
        )

        self.cur = self.connc.cursor()

    #2.插入数据
    def process_item(self, item, spider):
        try:
            #1.写sql语句
            sql = "insert into book_bookinfo(category,small_category,name,author,store,price,default_image) values(%s,%s,%s,%s,%s,%s,%s);"
            # item_list = list(item.values())
            # item_list.insert(0,0)
            # #2.让游标执行sql
            # self.cur.execute(sql,item_list)
            self.cur.execute(sql, (item['category'],item['small_category'],item['name'],item['author'],item['store'],item['price'],item['image']))
            self.connc.commit()
        except Exception as e:
            print(e)
            self.connc.rollback()
        return item

    #3.关闭爬虫 -- 断开和mysql的连接
    def close_spider(self,spider):
        self.cur.close()
        self.connc.close()
