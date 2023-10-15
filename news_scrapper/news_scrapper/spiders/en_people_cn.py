import scrapy
from news_scrapper.items import NewsScrapperItem
from scrapy.loader import ItemLoader
import datetime

class ENPeopleScraper(scrapy.Spider):
    name = 'enpcn'
    start_urls = ['http://en.people.cn/90786/index1.html']
    def parse(self, response):
        base_url = "http://en.people.cn/"
        articles =  response.css('li')
        links = []
        for article in articles:
            try:
                link = base_url + article.css('a').attrib['href']
            
                yield scrapy.Request(link, callback=self.parse_content)
            except:
                print("error")
                
    def parse_content(self, response):
        name = response.css('h1::text').get()
        time = response.css('div.origin.cf').css('span::text').get()
        content = response.css('div.w860.d2txtCon.cf').css('p::text').getall()
        
        dict = {'name' : name , 'time' : time , 'content' : content} 
        yield dict
        