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
  has_seen_metro = False
  count = 0
  
  for store in stores:
    storeType = str(store['type']).lower()
    storeId = store['storeId'] 
    firestoreId = store['id'] # reference to the key in firestore
    count += 1
    
    print(f'Processing {storeType} store. Store {count} of {len(stores)}...')  
    
    # Only need to process one metro store since prices are the same for all
    if storeType == 'metro':
      if has_seen_metro:
        continue
      else:
        has_seen_metro = True
    
    spider_name = ''
    if storeType == 'metro':
      spider_name = 'metro'
    elif storeType == 'walmart':
      spider_name = 'walmart'
    else:
      spider_name = 'loblaws'
      
    yield process.crawl(spider_name, storeId=storeId, storeType=storeType, firestoreId=firestoreId)
  reactor.stop()
  
def run(stores):
  crawl(stores)
  reactor.run()
  
  

