# -*- coding: utf-8 -*-

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jianshu_spider.items import JianshuSpiderItem

class JsSpider(CrawlSpider):
    name = 'js'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*/p/[0-9a-z]{12}.*'), callback='parse_detail', follow=True),#元组后面必须要有逗号，没有就会报错

    )

    # title = scrapy.Field()
    # content = scrapy.Field()
    # article_id = scrapy.Field()
    # origin_url = scrapy.Field()
    # avatar = scrapy.Field()
    # pub_time = scrapy.Field()

    def parse_detail(self,response):
        title = response.xpath("//h1/text()").get()
        subjects = ",".join(response.xpath("//div[@role='main']//div[@class='_2Nttfz']/a/span/text()").getall())
        print(title+'::::'+subjects)
        item = JianshuSpiderItem(title = title,subjects = subjects)
        return item




    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
