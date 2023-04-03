from datetime import datetime
import scrapy

import re

from ..items import NewsscrapItem
from ..constants import NO_OF_PAGES

class BusinessStandard(scrapy.Spider):
    
    name = "BS"
    start_urls = [f"https://www.business-standard.com/markets/news/page-{i+1}" for i in range(NO_OF_PAGES)]
    
    def get_date(self,response):
        article = NewsscrapItem()
        try:
            date = response.css('.story-meta .meta-info::text')[2].get()
            date = re.split("\|",date)[0].strip()
            date = date.replace(" ","/")
            try:
                int(date.split("/")[1])
                date = datetime.strptime(date,"%d/%m/%Y").date()
            except:
                date = datetime.strptime(date,"%b/%d/%Y").date()
        except:
            date =None
        article['title'] = response.meta['title']
        article['date'] = date
        article['newspaper'] = 'business-standard'
        yield article

    def parse(self, response):

        for a in response.css('a.smallcard-title'):
            link_to_get_date = a.css('a::attr(href)').get()
            data_to_pass = {'title':a.css('a::text').get(),'page':response.request.url[-1]}
            yield response.follow(link_to_get_date, callback=self.get_date, meta=data_to_pass)