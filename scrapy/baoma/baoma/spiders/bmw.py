# -*- coding: utf-8 -*-
import scrapy
from baoma.items import BaomaItem
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor



class BmwSpider(CrawlSpider):
    name = 'bmw'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html']



    rules = (
        Rule(LinkExtractor(allow=r'https://car.autohome.com.cn/pic/series/65.+'),callback="parse_page",follow = True),
    )

    def parse_page(self, response):
        category = response.xpath("//div[@class='uibox']/div/text()").get()
        srcs = response.xpath("//div[contains(@class,'uibox-con')]/ul/li//img/@src").getall()
        srcs = list(map(lambda x:x.replace("t_",""),srcs))

        # urls =[]
        # for src in srcs:
        #     url = response.urljoin(src)
        #     urls.append(url)
        urls = list(map(lambda x:response.urljoin(x),srcs))
        yield BaomaItem(category=category,image_urls = urls)





    def test_parse(self,response):
        uiboxs = response.xpath("//div[@class='uibox']")[1:]
        for uibox in uiboxs:
            category = uibox.xpath(".//div[@class='uibox-title']/a/text()").get()  # 取第一个
            print(category)
            urls = uibox.xpath(".//ul/li/a/img/@src").getall()
            # for url in urls:
            #     url = "https:"+url
            #     print(url)
            urls = list(map(lambda url: response.urljoin(url), urls))
            item = BaomaItem(category=category, image_urls=urls)
            yield item
