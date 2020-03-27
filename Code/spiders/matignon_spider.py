import scrapy

class EVSpider(scrapy.Spider):
  name = 'Matignon_keyword_automobile'
  allowed_domains = ["www.gouvernement.fr"]
  start_urls = ['https://www.gouvernement.fr/search/site/automobile']
    
  def parse(self,response):
      titles = response.css('h2.node-titre')
      for title in titles:
        loader = ItemLoader（item = Automobileitems(), selector = title)
        loader.add_css('title','h2.node-titre a::text')
        loader.add_css('link','h2.node-titre a::attr(href)')
        loader.add_css('teaser',' p.teaser-intro::text')
        loader.add_css('publication',' h2 > div.teaser-populication::text')
        Automobileitems = loader.load_item()
        content_url = title.css('.node-titre + a::attr(href)').get()
        yield response.follow(content_url, self.parse_author, meta={'Automobileiteam':Automobileitem})
          
      for a in response.css('li.pager-next_last a'):
        yield response.follow(a, self.parse)
