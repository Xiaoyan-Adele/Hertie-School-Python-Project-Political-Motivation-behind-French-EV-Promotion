# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EvArticleItems(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    publication = scrapy.Field()
    content = scrapy.Field()
    pass
