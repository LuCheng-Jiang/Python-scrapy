# -*- coding: utf-8 -*-
import scrapy
from lianjia.items import LianjiaItem
from urllib.parse import urljoin


class LjSpider(scrapy.Spider):
    name = 'lj'
    allowed_domains = ['lianjia.com']
    start_urls = ['https://gz.lianjia.com/ershoufang/']

    def parse(self, response):

        item = LianjiaItem()
        lis = response.xpath("//div[@class='leftContent']/ul/li[contains(@class,'LOG')]")

        for li in lis:
            item['title'] = li.xpath(".//div[@class='title']/a/text()").get()
            item['name']= li.xpath(".//div[@class='flood']//a[1]/text()").get()
            item['address'] = li.xpath(".//div[@class='flood']//a[2]/text()").get()

            houses_infos = li.xpath(".//div[@class='houseInfo']/text()").get()
            totalPrice = li.xpath(".//div[@class='totalPrice']//text()").getall()
            item['totalPrice'] = "".join(totalPrice)
            if houses_infos is None:
                continue
            houses_list = houses_infos.split("|")
            for house_item in houses_list:
                if '室' in house_item:
                    item['style'] = house_item
                elif '平米' in house_item:
                    item['area'] = house_item
                elif '装' in house_item:
                    item['complex'] = house_item
                elif '层' in house_item:
                    item['layer'] = house_item
                elif '建' in house_item:
                    item['year'] = house_item

            yield item


        next_url = response.xpath("//a[text()='下一页']/@href").get()
        print("next_url",next_url)
        if next_url is not None:
            next_url = urljoin("https://gz.lianjia.com/",next_url)
            yield scrapy.Request(url = next_url,callback=self.parse)



