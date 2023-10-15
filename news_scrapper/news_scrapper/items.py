# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsScrapperItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    time = scrapy.Field()
    # link = scrapy.Field()
    content = scrapy.Field()
    pass

class CmilItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    ByClass = scrapy.Field()
    DateTime = scrapy.Field()
    Date = scrapy.Field()
    Headline = scrapy.Field()
    Article_Lead = scrapy.Field()
    Pic = scrapy.Field()
    Article_Body = scrapy.Field()
    pass

class AllglobalItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # define the fields for your item here like:

    ByClass = scrapy.Field()
    Date_Time = scrapy.Field()
    Headline = scrapy.Field()
    Article_Lead = scrapy.Field()
    Pic = scrapy.Field()
    Article_Body = scrapy.Field()



    pass
