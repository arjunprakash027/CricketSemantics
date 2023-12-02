import scrapy
from icecream import ic


#ic.disable()
class CricketbotSpider(scrapy.Spider):
    name = "cricketbot"
    allowed_domains = ["www.hindustantimes.com"]
    start_urls = ["https://www.hindustantimes.com/cricket"]

    def parse(self, response):
        
        titles = response.css(".hdg3 a::text").extract()
        redirects = response.css(".hdg3 a::attr(href)").extract()

        for item in zip(titles,redirects):

            ic(item)

            scraped_info = {
                'title': item[0],
                'url': item[1],
            }


            yield scrapy.Request(url = 'https://www.hindustantimes.com'+item[1],callback=self.parse_article,meta={'scraped_info':scraped_info})
            

    def parse_article(self,response):
        contents = response.css("div.detail p::text").extract()
        scraped_info = response.meta.get('scraped_info', {})

        scraped_info['content'] = "".join(contents).replace('\n',"")
        
        yield scraped_info
    