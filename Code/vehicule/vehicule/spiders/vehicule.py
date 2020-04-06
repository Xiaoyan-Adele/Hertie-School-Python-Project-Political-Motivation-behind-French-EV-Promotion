import scrapy
from scrapy import Request
from vehicule.items import VehiculeItems


class VehiculeSpider(scrapy.Spider):

    name = 'VehiculeSpider'
    allowed_domains = ["www.gouvernement.fr"]
    start_urls = ['https://www.gouvernement.fr/search/site/vehicules%2520electriques']

    def parse(self, response):
        # use xpath to parse elements
        body = response.xpath('//*[@id="block-system-main"]/div/div/ol/li')
        for sel in body:
            title = sel.xpath('div[2]/h2/a/text()').extract()[0]
            link = sel.xpath('div[2]/h2/a/@href').extract()[0]
            publication = sel.xpath('div[2]/div/text()').extract()[0]

            item = VehiculeItems()
            item['title'] = title
            item['link'] = link
            item['publication'] = publication
            yield item

        # next page
        # //*[@id="block-system-main"]/div/div/div[2]/ul/li[7]/a
        pagers = response.xpath('//*[@id="block-system-main"]/div/div/div[2]/ul/li')
        next_page = pagers[-1]
        if next_page.xpath('a') and 'suivant' in next_page.xpath('a/text()').extract()[0]:
            next_url = "https://" + self.allowed_domains[0] + next_page.xpath('a/@href').extract()[0]
            yield Request(url=next_url)




