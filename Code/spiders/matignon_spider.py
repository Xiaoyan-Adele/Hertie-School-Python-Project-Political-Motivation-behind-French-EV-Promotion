import scrapy
from scrapy.loader import ItemLoader
from scrapy.items import Vehiculeitems

class EVSpider(scrapy.Spider):
  name = 'Matignon_keyword_vehiculeelectrique'
  allowed_domains = ["www.gouvernement.fr"]
  start_urls = ['https://www.gouvernement.fr/search/site/vehicules%2520electriques']
    
  def parse(self,response):
      titles = response.css('h2.node-titre')
      for title in titles:
        loader = ItemLoader(item=Vehiculeitems(),selector = title)
        loader.add_css('title','h2.node-titre a::text')
        loader.add_css('link','h2.node-titre a::attr(href)')
        loader.add_css('teaser',' p.teaser-intro::text')
        loader.add_css('publication','h2 > div.teaser-publication::text')
        Vehiculeitems = loader.load_item()
    #go to each article in the result list 
        content_url = title.css('.node-titre + a::attr(href)').get()
        yield response.follow(content_url, self.parse_author, meta={'Vehiculeitems':Vehiculeitems})
          
      for a in response.css('li.pager-next_last a'):
        yield response.follow(a, self.parse)

        
#to scrape content in each article  
    def content_parse (self, response):
        Vehiculeitems = response.meta[Vehiculeitems']
        loader = ItemLoader(item=Vehiculeitems, response = response)
        loader.add_css('title','h1.titre-texte::text')
        loader.add_css('article_content','div.field field-name-field-texte field-type-text-long field-label-hidden prose::text')                              
        yield loader.load_item()

        
