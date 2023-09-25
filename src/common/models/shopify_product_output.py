class ShopifyProductOutput:
    def __init__(self, product):
        self.product_id = product.attributes['id']
        self.title = product.attributes['title']
        self.vendor = product.attributes['vendor']
