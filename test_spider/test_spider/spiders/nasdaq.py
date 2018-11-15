# -*- coding: utf-8 -*-
import scrapy
import pandas


class NasdaqSpider(scrapy.Spider):
    name = 'nasdaq'
    def start_requests(self):
        allowed_domains = ['nasdaq.com']
        start_urls = ['https://nasdaq.com/']
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        with open('nasdaq.html', 'wb') as file:
            file.write(response.body)
