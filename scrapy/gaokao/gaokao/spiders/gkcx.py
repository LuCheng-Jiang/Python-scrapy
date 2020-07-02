# -*- coding: utf-8 -*-
import scrapy

from gaokao.items import GaokaoItem

class GkcxSpider(scrapy.Spider):
    name = 'gkcx'
    allowed_domains = ['gkcx.eol.cn']
    start_urls = ['https://gkcx.eol.cn/linespecialty?province=&schoolyear=2015']

    def parse(self, response):
        item = GaokaoItem()
        trs = response.xpath("//tbody//tr")
        for tr in trs:
            item = {}
            item['uni_name'] = tr.xpath("./td[1]/text()").get()
            item['uni_major'] = tr.xpath("./td[2]/text()").get()
            item["enroll_addr"] = tr.xpath("./td[3]/text()").get()
            item["stu_type"] = tr.xpath("./td[4]/text()").get()
            item['eaxm_year'] = tr.xpath("./td[5]/text()").get()
            item["enroll_batch"] = tr.xpath("./td[6]/text()").get()
            item['min_score'] = tr.xpath("./td[last()]/text()").get()
            item['max_score'] = tr.xpath("./td[last()-1]/text()").get()
            print(item)






