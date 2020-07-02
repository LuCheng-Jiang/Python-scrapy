# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from lianjia.settings import USER_AGENTS
import random
from selenium import webdriver

import time
from scrapy.http.response.html import HtmlResponse

class RandUserAgent(object):
    def process_request(self, request, spider):
        useragent = random.choice(USER_AGENTS)

        request.headers.setdefault("User-Agent", useragent)

class LianjiaPipeline(object):
    def process_item(self, item, spider):
        return item


class SeleniumDownloadMiddleware(object):
    def __init__(self):
        self.driver = webdriver.Chrome()


    def process_request(self,request,spider):
        self.driver.get(request.url)
        self.driver.implicitly_wait(50)
        source = self.driver.page_source
        response = HtmlResponse(url = self.driver.current_url,body=source,request =request,encoding='utf-8')
        return  response


