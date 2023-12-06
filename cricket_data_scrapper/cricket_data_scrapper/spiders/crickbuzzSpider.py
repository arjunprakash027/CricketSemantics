import scrapy
from icecream import ic
import re


class CrickbuzzspiderSpider(scrapy.Spider):
    name = "crickbuzzSpider"
    allowed_domains = ["m.cricbuzz.com"]
    start_urls = ["https://m.cricbuzz.com/cricket-series/6732/icc-cricket-world-cup-2023/matches"]

    def parse(self,response):
        for match_elem in response.css('.list-group-item.cb-list-group-item.cb-match-list-group-item'):
            match_name = match_elem.css('h4.list-group-item-heading::text').get().strip()
            match_url = match_elem.css('a.list-group-item::attr(href)').get()
            match_url = response.urljoin(match_url)

            ic(match_name)
            yield scrapy.Request(url=match_url,callback=self.match_parse,meta={'match_name':match_name})
            

    def match_parse(self, response):

        for item in response.css('.cb-list-item'):
            ball_info = item.css('.commtext span::text').get()
            commentary_text = ''.join(item.css('.commtext *::text').getall()).strip()
            match_name = response.meta.get('match_name')

            ic(match_name)

            if ball_info != None:
                yield {
                    "match":match_name,
                    "ball":ball_info,
                    "commentry":commentary_text
                }

        try:

            next_url = f"https://m.cricbuzz.com"+response.xpath('//button[@id="loadMorePagination"]/@value').extract()[0]
            yield scrapy.Request(url=next_url,callback=self.match_parse,meta={'match_name':match_name})

        except:
            print("Scrapping done!!")

    
