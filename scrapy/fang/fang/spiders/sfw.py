# -*- coding: utf-8 -*-
import redis
import scrapy
import re

from fang.items import  NewHouseItem,ESFHouseItem
from urllib.parse import urljoin
from scrapy_redis.spiders import RedisSpider


class SfwSpider(RedisSpider):
    name = 'sfw'
    allowed_domains = ['fang.com']
    # start_urls = ['https://www.fang.com/SoufunFamily.htm']
    redis_key = "fang:start_url"


    def parse(self, response):
        trs = response.xpath("//div[@class='outCont']//tr")
        province = None
        for tr in trs:
            tds = tr.xpath(".//td[not(@class)]")
            province_td = tds[0]
            province_text = province_td.xpath(".//text()").get()
            province_text = re.sub(r"\s","",province_text)
            if province_text:
                province = province_text  ##如果前面有显示省份就用省份，没有就用上一次的
            if province == '其它':    #不爬取海外的链接
                continue
            city_td = tds[1]
            city_links  = city_td.xpath(".//a")
            for city_link in city_links:
                city = city_link.xpath(".//text()").get()
                city_url = city_link.xpath(".//@href").get()
                # print("省份",province)
                # print("城市",city)
                # print("城市url",city_url)
                #构建新房的url链接
                url_module = city_url.split("//")
                scheme = url_module[0]
                cityabbr = url_module[1].split(".")[0]
                newhouse_url ="https://" + cityabbr +".newhouse.fang.com/house/s/"
                #构建二手房的url链接
                esf_url = "https://" +"//"+cityabbr+".esf.fang.com/"
                # print("城市%s%s"%(province,city))
                # print("新房链接%s"%newhouse_url)
                # print("二手房链接%s"%esf_url)

                yield scrapy.Request(url = newhouse_url,callback=self.parse_newhouse,meta= {"info":(province,city,cityabbr)})

                yield scrapy.Request(url = esf_url , callback=self.parse_esf,meta={"info":(province,city,cityabbr)})


    def parse_newhouse(self,response):
        province,city,cityabbr = response.meta.get("info")
        print(province,city)
        lis = response.xpath("//div[contains(@class,'nl_con')]/ul/li")
        for li in lis:
            name  = li.xpath(".//div[@class='nlcd_name']/a/text()").get()
            if name is None:
                continue
            name = name.strip()
            house_type_list = li.xpath(".//div[contains(@class,'house_type')]/a/text()").getall()
            house_type_list = list(map(lambda x:re.sub(r"\s","",x),house_type_list))
            rooms = list(filter(lambda x:x.endswith("居")|x.endswith("上"),house_type_list))
            #print(rooms)
            area = "".join(li.xpath(".//div[contains(@class,'house_type')]/text()").getall())
            area = re.sub(r'\s|－|/',"",area)
            # print(area)
            address = li.xpath(".//div[@class='address']/a/@title").get()
            district_text = "".join(li.xpath(".//div[@class='address']/a//text()").getall())
            district = re.search(r".*\[(.+)\].*",district_text).group(1)
            # print(district)
            sale = li.xpath(".//div[contains(@class,'fangyuan')]/span/text()").get()
            price = "".join(li.xpath(".//div[@class='nhouse_price']//text()").getall())
            price = re.sub(r"\s","",price)
            origin_url = li.xpath(".//div[@class='nlcd_name']/a/@href").get()
            origin_url = urljoin("https:",origin_url)
            # print(origin_url)
            # print(sale,price)
            item = NewHouseItem(province = province,city = city,name=name,rooms = rooms,area = area,address=address,district = district,sale=sale,price=price,origin_url=origin_url)
            yield item

        next_url  = response.xpath("//div[@class='page']//a[@class='next']/@href").get()

        if next_url:
            temp_url = "https://" + cityabbr + ".newhouse.fang.com"
            next_url = urljoin(temp_url,next_url)
            #print("下一页:%s"%next_url)
            yield scrapy.Request(url = response.urljoin(next_url),callback=self.parse_newhouse,meta={"info":(province,city,cityabbr)})


    def parse_esf(self,response):

        province,city,cityabbr = response.meta.get("info")
        temp_url = "https://" + cityabbr + ".esf.fang.com"
        dls  = response.xpath("//div[contains(@class,'shop_list')]/dl")

        for dl  in dls:
            item = ESFHouseItem(province = province,city= city)
            item['name'] = dl.xpath(".//p[@class='add_shop']/a/@title").get()
            item['address']  =dl.xpath(".//p[@class='add_shop']/span/text()").get()
            item['price'] = "".join(dl.xpath(".//dd[@class='price_right']/span[1]//text()").getall())
            item['unit'] = dl.xpath(".//dd[@class='price_right']/span[2]//text()").get()
            origin_url = dl.xpath(".//h4/a/@href").get()

            item["origin_url"] = urljoin(temp_url,origin_url)
            infos = dl.xpath(".//p[@class='tel_shop']/text()").getall()
            infos = list(map(lambda x :re.sub(r"\s","",x),infos))
            # print(name)
            # print(address)
            # print(infos)
            for info in infos:
                if "厅" in info:
                    item['rooms'] = info
                elif "层" in info:
                    item["floor"] = info
                elif '向' in info:
                    item["toward"] = info
                elif '建' in info:
                    item["year"] = info.replace("年建","")
                elif '㎡' in info:
                    item["area"] = info
                # print(item)


        next_url = response.xpath("//a[text()='下一页']/@href").get()
        yield scrapy.Request(url = response.urljoin(temp_url,next_url),callback=self.parse_esf,meta={"info":(province,city,cityabbr)})