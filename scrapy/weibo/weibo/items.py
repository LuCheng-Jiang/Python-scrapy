# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class UserItem(scrapy.Item):
    collection = 'users'

    id = scrapy.Field()
    #微博名
    name = scrapy.Field()
    #头像url
    avatar = scrapy.Field()
    #微博封面
    cover = scrapy.Field()
    #性别  "f"女
    gender = scrapy.Field()
    #描述
    description = scrapy.Field()
    fans_count = scrapy.Field()
    follows_count = scrapy.Field()
    #全部微博
    weibos_count = scrapy.Field()
    #无认证
    verified = scrapy.Field()
    verified_reason = scrapy.Field()
    verified_type = scrapy.Field()
    #follows返回的是一个列表
    follows = scrapy.Field()
    fans = scrapy.Field()
    #爬取时间
    crawled_at = scrapy.Field()


class UserRelationItem(scrapy.Item):
    collection = 'users'

    id = scrapy.Field()
    follows = scrapy.Field()
    fans = scrapy.Field()


class WeiboItem(scrapy.Item):
    collection = 'weibos'

    id = scrapy.Field()
    #点赞数
    attitudes_count = scrapy.Field()
    #评论数
    comments_count = scrapy.Field()
    #转发数
    reposts_count = scrapy.Field()
    picture = scrapy.Field()
    pictures = scrapy.Field()
    #手机
    source = scrapy.Field()
    # 微博内容
    text = scrapy.Field()
    #原文字
    raw_text = scrapy.Field()
    thumbnail = scrapy.Field()
    #用户id
    user = scrapy.Field()
    #微博发表时间
    created_at = scrapy.Field()
    #爬取时间
    crawled_at = scrapy.Field()



