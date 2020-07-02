# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy

class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['jd.com']
    start_urls = ['https://book.jd.com/booksort.html']

    #解析大分类的名字 和 小分类的名字
    def parse(self, response):

        dt_list = response.xpath("//div[@class='mc']/dl/dt")

        for dt in dt_list:
            item = {}
            item['category'] = dt.xpath("./a/text()").extract_first()

            # 根据大分类取小分类
            em_list = dt.xpath("./following-sibling::*[1]/em")
            for em in em_list[:1]:
                item['small_category'] = em.xpath("./a/text()").extract_first()

                small_link = "https:" + em.xpath("./a/@href").extract_first()


                yield scrapy.Request(small_link,callback=self.parse_book,meta={'book':deepcopy(item)})

    def parse_book(self,response):
        item = response.meta.get('book')
        list_book = response.xpath("//ul[contains(@class,'gl-warp')]/li[@ware-type!='0']")

        total_page = response.xpath("//span[@class='p-skip']//b/text()").extract_first()
        url = response.request.url
        i = 1
        for book in list_book[:2]:

            item['name']  = book.xpath(".//div[@class='p-name']//em/text()").extract_first()
            item['price'] = book.xpath(".//strong/i/text()").extract_first()
            item['store'] = book.xpath(".//div[@class='p-shopnum']/a/text()").extract_first()
            item['author'] = book.xpath(".//span[@class='p-bi-name']/a/text()").extract_first()
            item['image'] = "https:"+book.xpath(".//a/img/@src").extract_first()
        # name = "//ul[contains(@class,'gl-warp')]/li[@ware-type!='0']//div[@class='p-name']//em/text()"
        # price = "//ul[contains(@class,'gl-warp')]/li[@ware-type!='0']//strong/i/text()"
        # store = "//ul[contains(@class,'gl-warp')]/li[@ware-type!='0']//div[@class='p-shopnum']/a/text()"
        # author = "//ul[contains(@class,'gl-warp')]/li[@ware-type!='0']//span[@class='p-bi-name']/a/text()"
        # img = "https:" + "//ul[contains(@class,'gl-warp')]/li[@ware-type!='0']//a/img"

            i+=1
            print(item)
            yield item



        # 解析下一页的网址
        # next_url = "//a[@class='pn-next']/@href"
        if i<= 3:
            next_url = url+"&page={}".format(i*2-1)
            yield response.follow(
                next_url,
                callback = self.parse_book,
                meta = {'book':deepcopy(item)}
            )
