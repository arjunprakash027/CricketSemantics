import scrapy
from icecream import ic

class CrickbuzzspiderSpider(scrapy.Spider):
    name = "crickbuzzSpider"
    allowed_domains = ["m.cricbuzz.com"]
    start_urls = ["https://m.cricbuzz.com/live-cricket-scores/82462/ind-vs-aus-4th-t20i-australia-tour-of-india-2023"]

    def parse(self, response):
        for item in response.css('.cb-list-item'):
            ball_info = item.css('.commtext span::text').get()
            commentary_text = ''.join(item.css('.commtext *::text').getall()).strip()
            
            if ball_info != None:
                yield {
                    "ball":ball_info,
                    "commentry":commentary_text
                }

        try:

            next_url = f"https://m.cricbuzz.com"+response.xpath('//button[@id="loadMorePagination"]/@value').extract()[0]
            yield scrapy.Request(url=next_url,callback=self.parse)

        except:
            print("Scrapping done!!")

    
