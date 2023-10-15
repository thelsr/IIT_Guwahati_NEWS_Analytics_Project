import scrapy
from ..items import AllglobalItem

class GlobalSpiderSpider(scrapy.Spider):
    name = 'allglobal_spider'
    # allowed_domains = ['allglobaltimes.cn']
    start_urls = ['https://www.globaltimes.cn/china/politics/' , 'https://www.globaltimes.cn/china/society/', 'https://www.globaltimes.cn/china/diplomacy/', 'https://www.globaltimes.cn/china/military/' , 'https://www.globaltimes.cn/china/science/', 'https://www.globaltimes.cn/source/economy/', 'https://www.globaltimes.cn/source/company/']

    def parse(self, response):
        items = AllglobalItem()

        ByClass = response.css('.level02_title').css('::text').extract()
        ByClass[0] = ByClass[0].replace('\n', '').strip()
        Date_Time = response.css('.source_time::text').extract()
        Headline = response.css('.new_title_ms::text').extract()
        Links = response.css('.new_title_ms::attr(href)').extract()
        Article_Lead = response.css('p::text').extract()
        Pic = response.css('.list_img img::attr(src)').extract()

        items['ByClass'] = ByClass*len(Pic)
        items['Date_Time'] = Date_Time
        items['Headline'] = Headline
        items['Article_Lead'] = Article_Lead
        items['Pic'] = Pic

        requests = []
        for index, Link in enumerate(Links):
            item = {}
            for k in items.keys():
                item[k] = items[k][index]
            requests.append(scrapy.Request(Link, self.parseArticle, cb_kwargs=dict(item=item)))
        return requests

    def parseArticle(self, response, item):
        Body = response.css(".article_right::text").extract()
        Body = "".join(Body)
        Body = Body.replace('\n', '').replace('\r', '')
        item['Article_Body'] = Body
        yield item