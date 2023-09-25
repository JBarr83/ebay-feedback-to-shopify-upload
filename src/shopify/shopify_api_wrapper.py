from typing import List

import shopify
from shopify import Product
from shopify.collection import PaginatedCollection

from src.common.models.shopify_product_output import ShopifyProductOutput
from src.common.utilities.common_utilities import get_credentials_file


def create_product_list(product_list: PaginatedCollection[Product]) -> List[ShopifyProductOutput]:
    product_output_list = []
    for product in product_list:
        product_output_list.append(ShopifyProductOutput(product))
    return product_output_list


class ShopifyApiWrapper:
    def __init__(self):
        self.credentials = get_credentials_file()

        # Set up Shopify session
        session = shopify.Session(self.credentials['sunshine_hut']['shopify']['shop_url'],
                                  "2023-04",
                                  self.credentials['sunshine_hut']['shopify']['admin_token'])
        self.shopify_session = shopify
        self.shopify_session.ShopifyResource.activate_session(session)

    def create_master_product_list(self) -> List[ShopifyProductOutput]:
        products: PaginatedCollection[Product] = self.shopify_session.Product.find(limit=250)
        master_product_list = create_product_list(products)

        # If products have another page of results, retrieve and add to the master list until there are no more pages
        next_page: bool = products.has_next_page()
        while next_page:
            products: PaginatedCollection[Product] = products.next_page()
            master_product_list = [*master_product_list, *create_product_list(products)]
            next_page = products.has_next_page()

        return master_product_list
