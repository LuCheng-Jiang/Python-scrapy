# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from boss.items import BossItem



class ZhipinSpider(CrawlSpider):
    name = 'zhipin'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/c100010000/?query=python&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'.+\?query=python&page=\d'), follow=True),
        Rule(LinkExtractor(allow=r'.+job_detail/\S+.html'),callback="parse_job",follow=False)
    )


    def parse_job(self,response):
        print(response.text)
        job_name = response.xpath("//div[@class='name']/h1/text()").get().strip()  #去掉前后空格
        print(job_name)
        salary = response.xpath("//div[@class='name']/span/text()").get()
        print("*"*100)
        print(salary)
        job_info = response.xpath("//div[contains(@class,'job-p')]//div[@class='info-primary']/p//text()").getall()
        city = job_info[0]
        work_year = job_info[1]
        education = job_info[2]
        company  = response.xpath("//div[@class='company-info']/a[1]/@title").get().strip()
        item = BossItem(job_name = job_name,salary =salary,city=city,work_year = work_year,education =education ,company =company)
        yield item




    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
