import scrapy
import asyncio
from twisted.internet import asyncioreactor
scrapy.utils.reactor.install_reactor('twisted.internet.asyncioreactor.AsyncioSelectorReactor')
is_asyncio_reactor_installed = scrapy.utils.reactor.is_asyncio_reactor_installed()
print(f"Is asyncio reactor installed: {is_asyncio_reactor_installed}")
from scrapy.utils.project import get_project_settings
from twisted.internet import defer, reactor
from scrapy.crawler import CrawlerRunner

##############################################
# asyncio and asyncioreactor imports are necessary even though it looks like they are not used
# see https://stackoverflow.com/a/63409121/12616521
##############################################

settings = get_project_settings()
process = CrawlerRunner(settings)

@defer.inlineCallbacks
def crawl(stores):
  
  for store in stores:
    storeType = str(store['type']).lower()
    print(f'\nProcessing {storeType} store {store["storeId"]}\n')
    spider_name = 'walmart' if storeType == 'walmart' else 'loblaws'
    yield process.crawl(spider_name, storeId=store['storeId'], storeType=storeType)
  reactor.stop()
  
def run(stores):
  crawl(stores)
  reactor.run()
  
  

