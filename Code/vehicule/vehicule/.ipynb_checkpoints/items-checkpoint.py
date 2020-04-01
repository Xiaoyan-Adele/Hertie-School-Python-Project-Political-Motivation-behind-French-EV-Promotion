import scrapy

#to define the fields of my items
class VehiculeItems(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    teaser = scrapy.Field()
    publication = scrapy.Field()
    