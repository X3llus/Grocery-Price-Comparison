from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from FirestoreHelper import FirestoreHelper

class ProductPipeline:

    def open_spider(self, spider):
        self.client = FirestoreHelper()
        
    def process_item(self, item, spider):
        store_type = spider.storeType
        store_firebase_id = spider.firestoreId
        adapter = ItemAdapter(item)
        sku = adapter.get('SKU')
        price = adapter.get('price')
        inStock = adapter.get('inStock', True)
        
        if sku is None:
            raise DropItem(f'Missing SKU: {item}')
        if price is None:
            raise DropItem(f'Missing price: {item}')
        
        base_product = self.client.get_base_product(sku)
        if base_product is not None:
            self.client.handle_store_price(base_product['id'], store_firebase_id, adapter, inStock)
        else:
            self.client.add_product_and_store_price(adapter, store_firebase_id, store_type)
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


        
        