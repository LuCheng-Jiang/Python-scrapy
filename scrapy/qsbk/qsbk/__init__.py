###

""""

response 是一个"scrapy.response.html.HtmlResponse"对象  可以执行xpath提取数据

提取出来的数据，是一个Selector或者是一个SelectorList对象，如果想要获取其中的字符串，必须使用getall或者get方法

getall:list
get:str

如果数据解析回来，要传给pipelines处理，可以使用yields来返回
建议在'items。py定义类型


from scrapy.exporters import  JsonItemExporter

每次把数据添加到内存中，最后统一写入磁盘  好处是满足json的数据，坏处是数据量大，那么耗费内存较大

JsonLineItemExporter   这个是每次调用export_item的时候把这个item存储到硬盘中去


"""