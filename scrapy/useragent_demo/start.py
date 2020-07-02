
import requests

# from scrapy import cmdline
#
# cmdline.execute("scrapy crawl httpbin".split())

url = "https://www.zhipin.com/job_detail/46f409446646c3731HJ529y9GVE~.html?ka=search_list_1"

DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    'referer': 'https://www.zhipin.com/job_detail/46f409446646c3731HJ529y9GVE~.html?ka=search_list_1',
    'x-requested-with': 'XMLHttpRequest',
    'token': 'YGiz4b7EM5SSf3W'
 }

response = requests.get(url,headers = DEFAULT_REQUEST_HEADERS)
print(response.content.decode("utf-8"))