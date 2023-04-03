from datetime import datetime
import scrapy

import re

from ..items import NewsscrapItem
from ..constants import NO_OF_PAGES

url_list = []
for i in range(NO_OF_PAGES):
    if i ==0:
        url_list.append(f"https://www.moneycontrol.com/news/business/companies/")
    else:
        url_list.append(f"https://www.moneycontrol.com/news/business/companies/page-{i+1}")

class MoneyControl(scrapy.Spider):
    
    name = "MC"
    start_urls = url_list

    @staticmethod
    def get_date(text):
        year = int(text.split(",")[1].strip().split(" ")[0])
        month_part = text.split(",")[0].split(" ")
        month, day = datetime.strptime(month_part[0], "%B").month, int(month_part[1])
        return datetime(year, month, day).date()

    def parse(self, response):
        article_item = NewsscrapItem()
        for article in response.css('div#left li.clearfix'):
            article_item['title'] = article.css('h2 a::text').get()
            article_item['date'] = self.get_date(article.css('span::text').get())
            article_item['newspaper'] = 'money-control'
            yield article_item