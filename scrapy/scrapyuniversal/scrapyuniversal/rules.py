from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule


rules = {
    "china":(
        Rule(LinkExtractor(allow=r'article\/.*\.html'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'//a[text()="下一页"]')),
    )
}