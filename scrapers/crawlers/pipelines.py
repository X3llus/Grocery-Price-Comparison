from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from FirestoreHelper import FirestoreHelper
from fuzzywuzzy import process
import traceback

class ProductPipeline:

    def open_spider(self, spider):
        self.client = FirestoreHelper()
        self.numMatches = 0
        
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
        
        # Query the database for a product with the same SKU
        base_product = self.client.get_base_product(sku)
        
        # Found a product with the same SKU. Update the product with the new store price
        if base_product is not None:
            self.client.handle_store_price(base_product['id'], store_firebase_id, store_geo_point, store_type, adapter)
        else:
            brand = adapter.get('brand')
            size = adapter.get('packageSize')
            
            # Get products with the same brand and size
            product_brand_size = self.client.get_product_brand_size(brand, size)
            
            # If there are no products with the same brand and size, add a new entry for the product to the database
            if product_brand_size is None:
                self.client.add_product_and_store_price(store_firebase_id, store_geo_point, store_type, adapter)
            else:
                # If there are products with the same brand and size, use fuzzy matching to find the best match
                try:
                    name = adapter.get('name')
                    name = name.split(",")
                    name = name[0].split(" ")

                    matched_product = None
                    bestFuzzyMatch = -1

                    for product in name:
                        if product == brand:
                            name.remove(product)
                            
                    for match in product_brand_size:
                        addBestMatch = 0
                        nameCheck = match['name'].split(",")
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
                        if(addBestMatch > bestFuzzyMatch):
                            bestFuzzyMatch = addBestMatch
                            matched_product = match

                        addBestMatch = 0
                except:
                    print(traceback.format_exc())
            
                # If the fuzzy match is good enough, update the product with the new store price
                if(bestFuzzyMatch >= 0.95): #intergity with small chance of scraping error
                    self.numMatches += 1
                    print(f'Found {self.numMatches} matches so far.')
                    self.client.handle_store_price(matched_product['id'], store_firebase_id, store_geo_point, store_type, adapter)
                    
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


        
        