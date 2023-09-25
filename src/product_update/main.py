# This is a sample Python script.
import csv
from typing import List, Union

import shopify
import yaml
from shopify import Product
from shopify.collection import PaginatedCollection

from src.common.models.ProductOutput import ProductOutput


def create_product_list(product_list: PaginatedCollection[Product]) -> List[ProductOutput]:
    product_output_list = []
    for product in product_list:
        product_output_list.append(ProductOutput(product.attributes['id'],
                                                 product.attributes['title'],
                                                 product.attributes['vendor']))
    return product_output_list


def output_to_csv(product_output_list: List[ProductOutput]):
    fields = ['ID', 'Title', 'Vendor']
    with open('data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(fields)
        for product in product_output_list:
            writer.writerow([product.product_id, product.title, product.vendor])


if __name__ == '__main__':
    with open('../../resources/credentials.yml', 'r') as file:
        credentials = yaml.safe_load(file)

    # Set up Shopify session
    session = shopify.Session(credentials['sunshine_hut_shopify']['shop_url'],
                              "2023-04",
                              credentials['sunshine_hut_shopify']['admin_token'])
    shopify.ShopifyResource.activate_session(session)

    # Retrieve first page of products
    products: PaginatedCollection[Product] = shopify.Product.find(limit=250)

    master_product_list = create_product_list(products)

    # If products have another page of results, retrieve and add to the master list until there are no more pages
    next_page: bool = products.has_next_page()
    while next_page:
        products: PaginatedCollection[Product] = products.next_page()
        master_product_list = [*master_product_list, *create_product_list(products)]
        next_page = products.has_next_page()

    # Output the results to a CSV
    output_to_csv(master_product_list)
