# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GaokaoItem(scrapy.Item):
    uni_name = scrapy.Field()
    uni_major = scrapy.Field()
    enroll_addr = scrapy.Field()
    stu_type  = scrapy.Field()
    eaxm_year = scrapy.Field()
    enroll_batch =scrapy.Field()
    min_score = scrapy.Field()
    max_score = scrapy.Field()



