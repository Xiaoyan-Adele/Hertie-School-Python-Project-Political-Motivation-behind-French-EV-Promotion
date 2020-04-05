import codecs
from scrapy.exporters import CsvItemExporter

#to export the result into CSV file for further text analysis 
class EvPipeline(object):

    def __init__(self):
        self.file = open('output.csv', 'wb')
        # codecs.open('ev search results.csv', 'w', encoding='utf-8')
        # open('ev search results.csv', 'wb')
        self.exporter = CsvItemExporter(file=self.file)
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

