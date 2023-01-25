# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Field


class ProductItem(scrapy.Item):
    name = Field()
    brand = Field()
    imageUrl = Field()
    packageSize = Field()
    price = Field()
    normalizedPrice = Field()
    dateExtracted = Field()
    
    
