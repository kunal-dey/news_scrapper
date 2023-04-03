import scrapy


class NewsscrapItem(scrapy.Item):
    date = scrapy.Field()
    title = scrapy.Field()
    newspaper = scrapy.Field()