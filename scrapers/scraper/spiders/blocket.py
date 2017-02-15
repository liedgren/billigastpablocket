# -*- coding: utf-8 -*-
import scrapy
from scraper.items import Objekt
from scrapy.http import Request
import re
from scrapy.http import HtmlResponse


class blocketSpider(scrapy.Spider):
    name = "blocket"
    allowed_domains = ["blocket.se"]
    start_urls = [
        "https://www.blocket.se/hela_sverige/"   
    ]

    def start_requests(self):
        return [Request("https://www.blocket.se/hela_sverige/", callback=self.parse, meta={'index':1})]
        
    def parse(self, response):
        items = response.xpath("//article[contains(@class, 'item_row')]")
        for item in items:
            try:
                obj = Objekt()
                obj['name'] = item.xpath(".//h1/a/text()").extract()[0].encode('utf-8')
                obj['category'] = item.xpath(".//div[contains(@class, 'pull-left')]/a/text()").extract()[0].encode('utf-8')
                obj['location'] = item.xpath(".//div[contains(@class, 'pull-left')]/text()").extract()[0].encode('utf-8')[3:]
                obj['price'] = int(item.xpath(".//p[contains(@class, 'list_price')]/text()").extract()[0].encode('utf-8')[:-2].replace(" ", ""))
                yield obj 
            except:
                pass

        try:
            request = scrapy.Request("https://www.blocket.se/hela_sverige/?ca=11&w=3&st=s&o=%s" % str(int(response.meta["index"])+1), callback=self.parse)
            request.meta['index'] = str(int(response.meta["index"]) + 1)
            yield request
        except:
            return
