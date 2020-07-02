# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyuniversalItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class NewsItem(scrapy.Item):

    title = scrapy.Field()
    url = scrapy.Field()
    #正文
    text = scrapy.Field()
    #发布时间
    datetime = scrapy.Field()
    #来源
    source = scrapy.Field()
    #站点名称
    website = scrapy.Field()

