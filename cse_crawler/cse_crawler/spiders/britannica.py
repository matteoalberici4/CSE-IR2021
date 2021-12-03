import json
import scrapy
from cse_crawler.items import Company


class BritannicaSpider(scrapy.Spider):
    name = 'britannica'
    start_urls = [
        'https://www.britannica.com/topic/list-of-corporations-2039518'
        ]

    
    def parse(self, response):
        for i in range(1, 30):
            for company in response.css('section')[i].css('li'):
                current = Company()
                current['name'] = company.css('::text').get()
                current['url'] = company.css('a::attr(href)').get()
                current['country'] = response.css('section')[i].css('.h1').css('a::text').get()

                yield scrapy.Request(current['url'], callback=self.details, cb_kwargs=dict(company = current))


    def details(self, response, company):
        company_industry = response.xpath("//*[contains(text(), 'Areas Of Involvement:')]").xpath("..").css('a::text').get()
        company['industry'] = company_industry.capitalize()
        yield company