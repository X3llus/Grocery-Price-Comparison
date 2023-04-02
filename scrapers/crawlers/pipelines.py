from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from FirestoreHelper import FirestoreHelper
from fuzzywuzzy import process

class ProductPipeline:

    def open_spider(self, spider):
        self.client = FirestoreHelper()
        
    def process_item(self, item, spider):
        store_type = spider.storeType
        store_firebase_id = spider.firestoreId
        store_geo_point = spider.storeGeoPoint
        adapter = ItemAdapter(item)
        sku = adapter.get('SKU')
        price = adapter.get('price')

        
        if sku is None:
            raise DropItem(f'Missing SKU: {item}')
        if price is None:
            raise DropItem(f'Missing price: {item}')
        
        base_product = self.client.get_base_product(sku)
        if base_product is not None:
            self.client.handle_store_price(base_product['id'], store_firebase_id, store_geo_point, store_type, adapter)
        else:
            if adapter.get('storeId') == 'vg8P4HYZAYdDY3LjyIap':
                self.client.add_product_and_store_price(store_firebase_id, store_geo_point, store_type, adapter)
            else:
                bestFuzzyMatch = 0
                brand = adapter.get('brand') #only grabbing brand, size, name if else runs
                size = adapter.get('size')
                name = adapter.get('name')
                product_brand_size = self.client.get_product_brand_size(brand, size)
                name = name.split(",")
                name = name[0].split(" ")
                for product in name: #looking for brand name in array
                    if product == brand:
                        name.remove(product)
                for array in product_brand_size: #iterating through arrayof examples
                    nameCheck = array['name'].split(",")
                    nameCheck = nameCheck[0].split(" ")
                    for brandRemoval in nameCheck:
                        if brandRemoval == brand:
                            nameCheck.remove(brandRemoval)
                    if(len(name) > len(nameCheck)):
                        n = len(nameCheck) * 100
                        for check in nameCheck:
                            best_match = process.extractOne(check, name)
                            addBestMatch += best_match[1]
                    else: 
                        n = len(name) * 100
                        for check in name:
                            best_match = process.extractOne(check, nameCheck)
                            addBestMatch += best_match[1]
                    addBestMatch /= n
                    if(addBestMatch > bestFuzzyMatch): #holding the value of the highest best_match from all product names (with same brand and size) in firestore
                        bestFuzzyMatch = addBestMatch
                        newSKU = array['skus']
                if(bestFuzzyMatch >= 0.95): #intergity with small chance of scraping error
                    enter_product = self.client.get_base_product(newSKU)
                    if enter_product is not None:
                        self.client.handle_store_price(base_product['id'], store_firebase_id, store_geo_point, store_type, adapter)
                    else:
                        self.client.add_product_and_store_price(store_firebase_id, store_geo_point, store_type, adapter)
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
        
class ProductImagePipeline:
    
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        image_url = adapter.get('imageUrl')
        if image_url is None:
            return item
        elif 'icon-no-picture' in image_url:
          item['imageUrl'] = None
        return item
        
class StoreLocationPipeline:
    
    def open_spider(self, spider):
        self.client = FirestoreHelper()
        
    def process_item(self, item, spider):
        self.client.save_store(item)
        return item


        
        