# This is a sample Python script.
from src.common.models.ebay_feedback_output import EbayFeedbackOutput
from src.common.utilities.csv import output_shopify_products_to_csv, output_ebay_feedback_to_csv
from src.ebay.ebay_api_wrapper import EbayApiWrapper
from src.shopify.shopify_api_wrapper import ShopifyApiWrapper


def build_shopify_product_csv():
    shopify_wrapper = ShopifyApiWrapper()
    output_shopify_products_to_csv(shopify_wrapper.create_master_product_list())


def build_ebay_feedback_csv():
    ebay_wrapper = EbayApiWrapper()
    feedback_details = ebay_wrapper.get_account_feedback()

    ebay_feedback_output_list = []
    for x in feedback_details:
        ebay_feedback_output_list.append(EbayFeedbackOutput(x))

    output_ebay_feedback_to_csv(ebay_feedback_output_list)


if __name__ == '__main__':
    build_shopify_product_csv()
    build_ebay_feedback_csv()
