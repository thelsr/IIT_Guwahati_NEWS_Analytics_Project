import scrapy
from wikipedia_scrapper.items import WikipediaScrapperItem
# from scrapy.loader import ItemLoader
import csv
class WikipediaScraper(scrapy.Spider):
    name = 'wikiscraper'
    base_url = "https://en.m.wikipedia.org/wiki/"
    start_urls = []
    with open('keywords.csv', mode='r')as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            start_urls.extend(lines)
    file.close()
    
    for i in range(len(start_urls)):
        start_urls[i] = base_url + start_urls[i]

    def parse(self, response):
        content = response.css("p::text").getall()
        # item = WikipediaScrapperItem()
        keyword = response.url[len(self.base_url):]
        item = {}
        item['keyword'] =  str(keyword)
        item['content'] =  str(content)
        
        yield item