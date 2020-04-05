import scrapy
from scrapy import Request
from vehicule.items import VehiculeItems 

class VehiculeSpider(scrapy.Spider): 
    name ='VehiculeSpider'
    allowed_domains = ["www.gouvernement.fr"]
    start_urls = ['https://www.gouvernement.fr/search/site/vehicules%2520electriques']
    
    #use xpath to locate the parse elements
    def parse(self,response):
        urls = response.xpath('//*[@id="block-system-main"]/div/div/ol/li')
        for target in urls: 
            title = sel.xpath('div[2]/h2/a/text()').extract()[0]
            link  = sel.xpath('div[2]/h2/a/@href').extract()[0]
            teaser = sel.xpath('div[2]/p/text()').extract()[0]
            publication = sel.xpath('div[2]/div/text()').extract()[0]
            
            item = VehiculeItems()
            item['title'] = title
            item['link'] = link
            item['teaser'] = teaser
            item['publication'] = publication
            yield item
            
        #to scrape the corresponding contents in the next page
        pages = response.xpath('/*[@id="block-system-main"]/div/div/div[2]/lu/li')
        next_page = pages[-1]
        if next_page.xpath('a') and 'suivant' in next_page.xpath('a/text()').extract()[0]:
            next_url = "https://" + self.allowed_domains[0] + next_page.xpath('a/@href').extract()[0]
            yield Request(url=next_url)
