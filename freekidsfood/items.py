from scrapy.item import Item, Field

class FreekidsfoodItem(Item):
    name = Field()
    address = Field()
    city = Field()
    state = Field()
    phone = Field()
    days = Field()
    rating = Field()