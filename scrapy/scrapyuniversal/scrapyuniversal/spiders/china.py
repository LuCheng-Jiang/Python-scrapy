# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapyuniversal.items import NewsItem
from scrapyuniversal.loaders import ChinaLoader

class ChinaSpider(CrawlSpider):
    name = 'china'
    allowed_domains = ['tech.china.com']
    start_urls = ['https://tech.china.com/articles/']

    rules = (
        Rule(LinkExtractor(allow=r'article\/.*\.html'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'//a[text()="下一页"]')),
    )

    # def parse_item(self, response):
    #     item = NewsItem()
    #     item['title'] =  response.xpath("//h1[@id='chan_newsTitle']/text()").get()
    #     item['url']  =response.url
    #     item['text'] = ''.join(response.xpath("//div[@id='chan_newsDetail']//text()").getall()).strip()
    #     item['datetime'] = response.xpath("//div[@class='chan_newsInfo_source']/span[@class='time']/text()").get()
    #     item['source']=response.xpath("//div[@class='chan_newsInfo_source']/span[@class='source']/text()").get()
    #     item['website'] = '中华网'
    #
    #
    #     return item
    def parse_item(self,response):
        loader = ChinaLoader(item = NewsItem(),response = response)
        loader.add_xpath('title',"h1[@id='chan_newsTitle']/text()")
        loader.add_value('url',response.url)
        loader.add_xpath('text',"//div[@id='chan_newsDetail']//text()")
        loader.add_xpath("datetime","//div[@class='chan_newsInfo_source']/span[@class='time']/text()",re='(\d+-\d+-\d+\s\d+:\d+:\d+)')
        loader.add_xpath("source","//div[@class='chan_newsInfo_source']/span[@class='source']/text()")
        loader.add_value('website','中华网')
        yield loader.load_item()