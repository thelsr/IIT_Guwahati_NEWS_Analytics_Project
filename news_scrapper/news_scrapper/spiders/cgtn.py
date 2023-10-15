import scrapy
from news_scrapper.items import NewsScrapperItem
from scrapy.loader import ItemLoader
import datetime
class CGTNScraper(scrapy.Spider):
    name = 'cgtn'
    start_urls = ['https://www.cgtn.com/china']

    def parse(self, response):
        articles =  response.css('div.cg-content-description')
        links = []
        for article in articles:
            link = article.css('a').attrib['href']
            
            yield scrapy.Request(link, callback=self.parse_content)
        
    def parse_content(self, response):
        source_class = response.css('div.news-section-date.news-text').css('span.section::text').get()
        name = response.css('div.news-title::text').get()
        time = response.css('div.news-section-date.news-text').css('span.date::text').get()
        content = response.css('div.text.en').css('p::text').getall()
        
        dict = {'source class' : source_class ,'name' : name , 'time' : time , 'content' : content} 
        yield dict
        
