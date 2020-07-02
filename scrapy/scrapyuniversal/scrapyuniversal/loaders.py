

from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst,Join,Compose


class NewsLoader(ItemLoader):
    default_output_processor = TakeFirst()  #相当于extract_first功能


class ChinaLoader(NewsLoader):
    text_out = Compose(Join(),lambda s:s.strip())
    source_out = Compose(Join(),lambda s:s.strip())
