# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GraphicsCardResearchItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    # 性价比
    rating = scrapy.Field()
    # 性能
    performance = scrapy.Field()
    # 出厂年份
    year = scrapy.Field()
    pass