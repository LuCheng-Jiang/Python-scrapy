# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from twisted.enterprise import adbapi
from pymysql import cursors

class JianshuSpiderPipeline(object):

    def __init__(self):
        dbparams={
            'host':'127.0.0.1',
            'port':3306,
            'user':'root',
            'password':'123456',
            'database':'jianshu',
        }
        self.conn = pymysql.connect(**dbparams)
        print(self.conn)
        self.cursor = self.conn.cursor()
        self._sql=None



    def process_item(self, item, spider):

        self.cursor.execute(self.sql,(item["title"]))

        self.conn.commit()
        return item


    @property
    def sql(self):
        if not self._sql:
            self._sql = """insert into article(id,title) values (null,%s)"""

            return self._sql
        return self._sql


class JianshuTwistedPipeline(object):

    def __init__(self):
        dbparams = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'password': '123456',
            'database': 'jianshu',
            'cursorclass':cursors.DictCursor
        }
        self.dbpool = adbapi.ConnectionPool("pymysql",**dbparams)
        self._sql = None

        @property
        def sql(self):
            if not self._sql:
                self._sql = """insert into article(id,title,type) values (null,%s,%s)"""

                return self._sql
            return self._sql

        def process_item(self,item,spider):
            defer  =self.dbpool.runInteraction(self.insert_item,item)
            defer.addErrback(self.handle_error,item,spider)

        def insert_item(self,cursor,item):
            cursor.execute(self.sql,(item["title"],item["subjects"]))

        def handle_error(self,error,item,spider):
            print("="*20)
            print(error)
            print("="*20)
