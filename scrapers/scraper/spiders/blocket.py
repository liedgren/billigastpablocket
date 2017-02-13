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
        items = response.xpath("//article[contains(@class, 'item_row')]//text()").extract();
        if len(items) > 0:
            x = 0
            lst = []
            lastLst = []
            for i in items:
                try:
                    if x == 1 or x == 0:
                        x += 1
                        continue                       

                    if x == 7:
                        x = 0
                        item = Objekt()
                        item['category'] = str(lst[0])
                        item['location'] = str(lst[1][2:])
                        item['name'] = str(lst[3])
                        item['price'] = int(lst[4].split(':')[0].replace(" ",""))
                        if lastLst != lst:
                            yield item
                            lst = []
                            lastLst = lst
                            continue
                        else:
                            continue
                    
                    if 1 < x <7:
                        x += 1

                    lst.append(i)
                except:
                    continue

            request = scrapy.Request("https://www.blocket.se/hela_sverige/?ca=11&w=3&st=s&o=%s" % str(int(response.meta["index"])+1), callback=self.parse)
            request.meta['index'] = str(int(response.meta["index"]) + 1)
            yield request
