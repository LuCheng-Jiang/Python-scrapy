# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import  JsonLinesItemExporter
import pymongo

class MongoPipeline(object):
    def __init__(self,mongo_url,mongo_db):
        self.mongo_url = mongo_url
        self.mongo_db  =mongo_db

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            mongo_url = crawler.settings.get("MONGO_URI"),
            mongo_db = crawler.settings.get("MONGO_DB")
        )

    def open_spider(self,spider):
        self.client = pymongo.MongoClient(self.mongo_url)
        self.db = self.client[self.mongo_db]
        self.collection = self.db.lianjia

    def process_item(self,item,spider):
        name = item["title"]
        self.collection.insert_one(dict(item))
        return item

    def close_spider(self,spider):
        self.client.close()


class LianjiaPipeline(object):
    def __init__(self):
        self.gzesf_fp = open("gzesf.json",'wb')

        self.gzesf_exporter = JsonLinesItemExporter(self.gzesf_fp,ensure_ascii = False)



    def process_item(self, item, spider):
        self.gzesf_exporter.export_item(item)
        return item

    def close_spider(self,spider):
        self.gzesf_fp.close()





