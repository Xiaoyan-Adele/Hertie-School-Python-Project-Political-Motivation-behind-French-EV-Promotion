from scrapy import signals

class VehiculeSpiderMiddleware (object):
    
    @classmethod
    def from_crawler (cls, crawler):
        s = cls()
    #to create our spider   
    crawler.signals.connect(s.spider_opened,signal=signals.spider_opened)
        return s
    
    #called for each response to go through spider 
    def process_spider_input(self,response,spider):
        return None 
    
    #after the spider has processed the responses, it should produce the results
    def process_spider_output(self,response,result,spider):
        for i in result:
            yield i 
    
    def process_spider_exception(self,response,exception,spider):
        pass
    
    def process_start_requests(self,start_requests,spider):
        for r in start_requsts:
            yield r
            
    def spider_opened(self,spider):
        spider.logger.info('Spider Opened: %s' % spider.name)

class VehiculeDownloaderMiddleware(object):
    
    @classmethod
    def from crawler(cls,crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened,signal=signals.spider_opened)
        return s
    
    def process_request (self,request,spider):
        return None
    
    def process_exception(self, request, exception, spider):
        pass
    
    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
    