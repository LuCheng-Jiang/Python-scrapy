# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    name =scrapy.Field()
    address =scrapy.Field()
    totalPrice =scrapy.Field()
    layer = scrapy.Field()
    style=scrapy.Field()
    area = scrapy.Field()
    complex =scrapy.Field()
    year = scrapy.Field()
    pass
