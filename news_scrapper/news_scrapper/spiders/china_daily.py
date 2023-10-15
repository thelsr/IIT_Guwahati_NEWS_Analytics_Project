import scrapy
from news_scrapper.items import NewsScrapperItem
from scrapy.loader import ItemLoader
import datetime
class EngModGovScraper(scrapy.Spider):
    name = 'engmgc'
    start_urls = ['http://eng.mod.gov.cn/']

    def parse(self, response):
        base_url = "http://eng.mod.gov.cn/"
        articles =  response.css('div.title')
        links = []
        for article in articles:
            try:
                link  = article.css('a').attrib['href']
                yield scrapy.Request(link, callback=self.parse_content)
            except:
                print("error")
                
    def parse_content(self, response):
        source_class = response.css("div.breadcrum.hidden-xs").css('font::text').get()
        name = response.css("div.artichle-info").css('h2::text').get()
        time = response.css("div.artichle-info").css('p').css('span::text').getall()
        content = response.css("div.article-content").css('p::text').getall()
        
        dict = {'source class' : source_class ,'name' : name , 'time' : time , 'content' : content} 
        yield dict
        # yield name ,time ,content
        
