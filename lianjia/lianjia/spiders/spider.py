from sys import exec_prefix
import scrapy
from lianjia.items import MyItem # 从 items.py 中引入 MyItem 对象

class mySpider(scrapy.spiders.Spider):
    name = "lianjia" # 爬虫的名字是 lianjia
    allowed_domains = ["bj.lianjia.com/"] # 允许爬取的网站域名
    url_format = "https://bj.fang.lianjia.com/loupan/pg{}/" # URL 格式 ，即爬虫爬取的 URL 格式
    start_urls = []
    for page in range(1, 23):
        start_urls.append(url_format.format(page))

    def parse(self, response):
        item = MyItem()
        for each in response.xpath("/html/body/div[3]/ul[2]/li"):
            if each.xpath("div/div[1]/a/text()"):
                item['name'] = each.xpath("div/div[1]/a/text()").extract()[0].strip() # 名称
            if each.xpath("div/div[2]/span[1]/text()"):
                item['location1'] = each.xpath("div/div[2]/span[1]/text()").extract()[0].strip() # 位置1
            if each.xpath("div/div[2]/span[2]/text()"):
                item['location2'] = each.xpath("div/div[2]/span[2]/text()").extract()[0].strip() # 位置2
            if each.xpath("div/div[2]/a/text()"):
                item['location3'] = each.xpath("div/div[2]/a/text()").extract()[0].strip() # 位置3
            if each.xpath("div/a/span[1]/text()"):
                item['type'] = each.xpath("div/a/span[1]/text()").extract()[0].strip() # 房型
            if each.xpath("div/div[3]/span/text()"):
                item['area'] = each.xpath("div/div[3]/span/text()").extract()[0].split(' ')[1] # 面积
                if item['area'].find('-') != -1:
                    item['area'] = int(item['area'].split('-')[0])
                else:
                    item['area'] = int(item['area'].split('㎡')[0])
            if each.xpath("div/div[6]/div[1]/span[1]/text()"):
                if each.xpath("div/div[6]/div[1]/span[2]/text()").extract()[0].find('均价') != -1:
                    item['avgPrice'] = "%.4f" % (int(each.xpath("div/div[6]/div[1]/span[1]/text()").extract()[0]) / 10000.0) # 均价
                    item['totalPrice'] = "%.4f" % (item['area'] * float(item['avgPrice'])) # 总价
                if each.xpath("div/div[6]/div[1]/span[2]/text()").extract()[0].find('总价') != -1:
                    item['totalPrice'] = each.xpath("div/div[6]/div[1]/span[1]/text()").extract()[0]
                    if item['totalPrice'].find('-') == -1:
                        item['totalPrice'] = "%.4f" % (int(item['totalPrice'])) # 均价
                    else:
                        item['totalPrice'] = "%.4f" % (int(item['totalPrice'].split('-')[0])) # 均价
                    item['avgPrice'] = "%.4f" % (float(item['totalPrice']) / item['area']) # 总价
            yield(item)