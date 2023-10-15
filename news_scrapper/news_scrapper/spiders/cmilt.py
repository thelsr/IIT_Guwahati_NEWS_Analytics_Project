import scrapy
from ..items import CmilItem

class CmiltSpider(scrapy.Spider):
    name = 'cmilt'
    page_number = 2
    start_urls = ['http://eng.chinamil.com.cn/armed-forces/node_86976.htm', 'http://eng.chinamil.com.cn/armed-forces/node_86978.htm', 'http://eng.chinamil.com.cn/armed-forces/node_86980.htm', 'http://eng.chinamil.com.cn/armed-forces/node_86982.htm' , 'http://eng.chinamil.com.cn/armed-forces/node_86985.htm', 'http://eng.chinamil.com.cn/armed-forces/node_86987.htm', 'http://eng.chinamil.com.cn/armed-forces/node_86987.htm', 'http://eng.chinamil.com.cn/armed-forces/node_86989.htm', 'http://eng.chinamil.com.cn/armed-forces/node_86991.htm', 'http://eng.chinamil.com.cn/armed-forces/node_86993.htm', 'http://eng.chinamil.com.cn/armed-forces/node_86995.htm', 'http://eng.chinamil.com.cn/armed-forces/node_86997.htm','http://eng.chinamil.com.cn/armed-forces/node_86999.htm', 'http://eng.chinamil.com.cn/cmc/node_86686.htm', 'http://eng.chinamil.com.cn/cmc/node_86704.htm','http://eng.chinamil.com.cn/cmc/node_86705.htm','http://eng.chinamil.com.cn/cmc/node_86706.htm','http://eng.chinamil.com.cn/cmc/node_86707.htm','http://eng.chinamil.com.cn/cmc/node_86708.htm','http://eng.chinamil.com.cn/cmc/node_86709.htm','http://eng.chinamil.com.cn/cmc/node_86710.htm','http://eng.chinamil.com.cn/cmc/node_86711.htm','http://eng.chinamil.com.cn/cmc/node_86712.htm','http://eng.chinamil.com.cn/cmc/node_86713.htm','http://eng.chinamil.com.cn/cmc/node_86714.htm','http://eng.chinamil.com.cn/cmc/node_86715.htm','http://eng.chinamil.com.cn/cmc/node_86716.htm','http://eng.chinamil.com.cn/cmc/node_86717.htm','http://eng.chinamil.com.cn/cmc/node_86718.htm', 'http://eng.chinamil.com.cn/china-military/node_83132.htm','http://eng.chinamil.com.cn/china-military/node_83133.htm' ,'http://eng.chinamil.com.cn/china-military/node_83134.htm','http://eng.chinamil.com.cn/china-military/node_83135.htm','http://eng.chinamil.com.cn/china-military/node_83136.htm','http://eng.chinamil.com.cn/china-military/node_83137.htm','http://eng.chinamil.com.cn/china-military/node_83139.htm','http://eng.chinamil.com.cn/voices/node_83140.htm','http://eng.chinamil.com.cn/voices/node_83141.htm','http://eng.chinamil.com.cn/voices/node_88664.htm','http://eng.chinamil.com.cn/voices/node_83142.htm','http://eng.chinamil.com.cn/world-military/node_83144.htm','http://eng.chinamil.com.cn/world-military/node_83143.htm','http://eng.chinamil.com.cn/international-reports/node_83168.htm','http://eng.chinamil.com.cn/international-reports/node_83167.htm']
    def parse(self, response):
        items = CmilItem()

        ByClass = response.css('.breadcrumb').css('::text').extract()
        DateTime = response.css("#main-news-list .time::text").extract()
        Headline = response.css('#main-news-list .title::text').extract()
        Links = response.css('#main-news-list li a::attr(href)').extract()
        Article_Lead = [txt for item in response.css('.desc') for txt in item.css('::text').extract() or [u'']]
        Pic = response.css('.image::attr(src)').extract()
        Next = response.xpath("//a[contains(text(), 'Next')]").css("::attr(href)").extract()
        ByClass = [''.join(ByClass).replace('\r', '').replace('\n', '')]

        items['ByClass'] = ByClass * len(Headline)
        items['DateTime'] = DateTime
        items['Headline'] = Headline
        items['Article_Lead'] = Article_Lead
        items['Pic'] = Pic

        for index, Link in enumerate(Links):
            item = {}
            for k in items.keys():
                item[k] = items[k][index]
            item['Pic'] = response.urljoin(item['Pic'])
            yield scrapy.Request(response.urljoin(Link), self.parseArticle, cb_kwargs=dict(item=item))

        if Next:
            yield response.follow(response.urljoin(Next[0]), callback=self.parse)

    def parseArticle(self, response, item):
        date = response.css(".float-right dd::text").extract()
        Body = response.css("p::text").extract()
        Body = "".join(Body)
        Body = Body.replace('\n', '').replace('\r', '')

        item['Date'] = date[0] if 0 < len(date) else ''
        item['Article_Body'] = Body

        # print(item)
        yield item