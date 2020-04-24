import scrapy
from scrapy import Request
from evarticles.items import EvArticleItems


class EvArticleSpider(scrapy.Spider):

    name = 'EvArticleSpider'
    allowed_domains = ["www.gouvernement.fr"]
    start_urls = ['https://www.gouvernement.fr/search/site/vehicules%2520electriques']

    def parse(self, response):
        # use xpath to parse elements

        def parse_content(response):
            content = response.xpath('//*[@id="block-system-main"]/div/div')
            content = content.xpath('string(.)').extract()[0]
            item = EvArticleItems()
            item['content'] = content
            item['title'] = ''
            item['link'] = ''
            item['publication'] = ''
            yield item
        
        body = response.xpath('//*[@id="block-system-main"]/div/div/ol/li')
        for url in body:
            #get the content of the url link  
            content_url = url.xpath('div[2]/h2/a/@href').get()
            self.logger.info('scrape article content')
            yield response.follow(content_url, callback=parse_content)
            
        # next page
        # //*[@id="block-system-main"]/div/div/div[2]/ul/li[7]/a
        pagers = response.xpath('//*[@id="block-system-main"]/div/div/div[2]/ul/li')
        next_page = pagers[-1]
        if next_page.xpath('a') and 'suivant' in next_page.xpath('a/text()').extract()[0]:
            next_url = "https://" + self.allowed_domains[0] + next_page.xpath('a/@href').extract()[0]
            yield Request(url=next_url)




