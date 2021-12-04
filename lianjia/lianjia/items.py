# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class MyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    location1 = scrapy.Field()
    location2 = scrapy.Field()
    location3 = scrapy.Field()
    type = scrapy.Field()
    area = scrapy.Field()
    totalPrice = scrapy.Field()
    avgPrice = scrapy.Field()
    pass