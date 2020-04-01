
BOT_NAME = 'vehicule'

SPIDER_MODULES = ['vehicule.spiders']
NEWSPIDER_MODULE = 'vehicule.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'vehicule.pipelines.EvPipeline': 300,
}

FEED_EXPORT_ENCODING = "utf-8"