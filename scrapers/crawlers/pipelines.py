from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from FirestoreHelper import FirestoreHelper
from RealtimeDbHelper import RealtimeDbHelper

class ProductPipeline:
    
    def __init__(self):
        self.count = 0
        self.num_existing = 0
    
    def open_spider(self, spider):
        self.client = FirestoreHelper()
        
    def close_spider(self, spider):
        self.count = 0
        self.num_existing = 0
        
    def process_item(self, item, spider):
        self.count += 1
        
        # if we've at least processed 30 products and 75% of them already exist
        # stop reading / writing to Firestore to save on costs and time
        if self.count > 30 and self.num_existing / self.count > 0.75:
            return item
        
        adapter = ItemAdapter(item)
        sku = adapter.get('SKU')
        
        existing = self.client.get_base_product(sku)
        if existing is not None:
            self.num_existing += 1
            return item
        else:
            self.client.save_base_product(adapter, spider.storeType)
            return item
        
        
class ProductPricesPipeline:
    
    def open_spider(self, spider):
        self.client = RealtimeDbHelper()
        
    def close_spider(self, spider):
        pass
    
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter.get('price') is None:
            raise DropItem(f'Missing price: {item}')
        else:
            self.client.save_product_price(spider.storeType, spider.storeId, adapter)
            return item
    

class DuplicatesPipeline:
    
    def __init__(self):
        self.seen = set()
           
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        sku = adapter.get('SKU')
        if sku is None:
            raise DropItem(f'Missing SKU: {item}')
        if sku in self.seen:
            raise DropItem(f'Duplicate item found: {item}')
        else:
            self.seen.add(sku)
            return item
        
        
class StoreLocationPipeline:
    
    def open_spider(self, spider):
        self.client = FirestoreHelper()
        
    def process_item(self, item, spider):
        self.client.save_store(item)
        return item


        
        