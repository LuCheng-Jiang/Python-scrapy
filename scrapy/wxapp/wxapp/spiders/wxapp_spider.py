# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from wxapp.items import WxappItem

class WxappSpiderSpider(CrawlSpider):
    name = 'wxapp_spider'
    allowed_domains = ['wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=1&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'http://www.wxapp-union.com/portal.php?mod=list&catid=1&page=\d'), follow=True),
        Rule(LinkExtractor(allow=r'.+article-.+-1.html'),callback="parse_detail",follow=False)
    )



    def parse_detail(self,reponse):
        title = reponse.xpath("//h1/text()").get()
        author_p = reponse.xpath("//p[@class='authors']")
        author_name  =author_p.xpath("./a/text()").get()
        author_pubdate = author_p.xpath("./span/text()").get()
        content = reponse.xpath("//section/p/text()").getall()
        content = "".join(content).strip()
        print("title is %s \n"%title)
        print("the author is %s ,pubdate is %s"%(author_name,author_pubdate))
        print("content    : %s"%content)
        items = WxappItem(title= title,author_name=author_name,author_pubdate=author_pubdate,content=content)
        yield  items
