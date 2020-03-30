from scrapy.item import Item, Field
from scrapy.loader.processors import MapCompose, TakeFirst
from datetime import datetime

def convert_date(text):
  return datetime.strptime(text, '%b %d, %Y')

class Vehiculeitems (Item):
    title = Field()
    link = Field()
    teaser = Field()
    publication = Field(
        input_processor = MapCompose(convert_date)
        output_processor = TakeFirst()
    article_content =Field()
    )
    tags = Field()
