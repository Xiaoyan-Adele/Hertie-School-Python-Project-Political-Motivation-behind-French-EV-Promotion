# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
from scrapy.exporters import CsvItemExporter

class EvArticlePipeline(object):
    
    def __init__(self):
        self.file = open('evarticle.csv','wb')
        self.exporter = CsvItemExporter(file=self.file)
        self.exporter.start_exporting()
    
    def process_item(self, item, spider):
        self.exporter.export_item(item)
    
    def close_spider(self,spider):
        self.exporter.finish_exporting()
        self.file.close()
