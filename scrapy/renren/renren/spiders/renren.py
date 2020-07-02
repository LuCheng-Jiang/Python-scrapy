# -*- coding: utf-8 -*-
import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    def start_requests(self):
        url = "http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2020241628918"
        data = {"email":"17670743808","password":"zhangyang123"}
        request = scrapy.FormRequest(url,formdata=data,callback=self.parse_page)
        yield request



    def parse_page(self,response):
        with open("renren.html","w",encoding="utf-8") as f :
            f.write(response.text)
