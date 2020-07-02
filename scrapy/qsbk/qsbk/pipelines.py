# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import  JsonItemExporter


class QsbkPipeline(object):

    def open_spider(self,spider):
        print("爬虫开始了")
        pass

    def process_item(self, item, spider):
        return item

    def close_spider(self,spider):
        print("爬虫结束了")
        pass


