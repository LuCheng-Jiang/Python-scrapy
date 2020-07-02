# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
from urllib import request

from scrapy.pipelines.images import ImagesPipeline
from baoma import settings

class BaomaPipeline(object):

    def __init__(self):
        self.path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images')
        if not os.path.exists(self.path):
            os.mkdir(self.path)



    def process_item(self, item, spider):
        category  = item["category"]
        urls = item["urls"]

        category_path = os.path.join(self.path,category)
        if not os.path.exists(category_path):
            os.mkdir(category_path)
        for url in urls:
            image_name  = url.split('-')[-1]
            request.urlretrieve(url,os.path.join(category_path,image_name))


        return item



class BaomaImagesPipeline(ImagesPipeline):


    def get_media_requests(self, item, info):
        #这个方法是在发送请求之前调用
        #其实这个方法本身就是发送下载请求得
        request_objs = super(BaomaPipeline,self).get_media_requests(self,item,info)
        for request_obj in request_objs:
            request_obj.item = item

        return request_objs

    def file_path(self, request, response=None, info=None):
        # 这个方法在图片将要存储的时候调用，来获取图片的存储路径
        path = super(BaomaPipeline,self).file_path(request, response, info)
        category = request.item.get("category")


        images_store = settings.IMAGES_STORE
        category_path = os.path.join(images_store,category)
        if not os.path.exists(category_path):
            os.mkdir(category_path)

        image_name = path.replace("full/","")
        image_path = os.path.join(category_path,image_name)
        return image_path




