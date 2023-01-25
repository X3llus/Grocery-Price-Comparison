# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
    
    
class PricePipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter.get('price') is not None and adapter.get('normalizedPrice') is not None:
            return item
        else:
            raise DropItem('Missing price in %s' % item)
        
        
        
class DuplicatesPipeline:
    
    def __init__(self):
        self.productNames_seen = set()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        
        # product names seem to be unique for walmart
        if adapter.get('name') in self.productNames_seen:
            raise DropItem('Duplicate item found: %s' % item)
        else:
            self.productNames_seen.add(adapter.get('name'))
            return item
        