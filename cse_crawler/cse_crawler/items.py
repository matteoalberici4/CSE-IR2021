# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class Company(scrapy.Item):
    name = scrapy.Field()
    rating = scrapy.Field()
    size = scrapy.Field()
    industry = scrapy.Field()
    url = scrapy.Field()
    country = scrapy.Field()