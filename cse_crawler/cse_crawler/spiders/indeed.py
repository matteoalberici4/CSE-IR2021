import json
import scrapy
from cse_crawler.items import Company


class IndeedSpider(scrapy.Spider):
    name = 'indeed'
    start_urls = [
        'https://ch.indeed.com/companies/search?q=switzerland',
        'https://ch.indeed.com/companies/search?q=italy',
        'https://ch.indeed.com/companies/search?q=france',
        'https://ch.indeed.com/companies/search?q=germany',
        'https://ch.indeed.com/companies/search?q=austria'
        ]


    def parse(self, response):
        for company in response.css('.css-7vf1t1-Flex'): 
            current = Company()
            current['name'] = company.css('.css-15p3hu3-Text::text').get()
            current['rating'] = company.css('span::text').get()

            company_details = response.urljoin('https://ch.indeed.com' + company.css('a::attr(href)').get())
            current['url'] = company_details

            company_country = response.url.split('q=')[1]
            current['country'] = company_country.capitalize()

            yield scrapy.Request(company_details, callback=self.details, cb_kwargs=dict(company = current))


    def details(self, response, company):
        company['size'] = response.xpath('//li[@data-testid="companyInfo-employee"]').css('.css-1k40ovh::text').get()
        company['industry'] = response.xpath('//li[@data-testid="companyInfo-industry"]').css('.css-1w0iwyp::text').get()
        yield company
