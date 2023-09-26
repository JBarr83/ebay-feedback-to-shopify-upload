from typing import List

from src.common.models.ebay_feedback_output import EbayFeedbackOutput
from src.common.models.shopify_product_output import ShopifyProductOutput
from src.common.utilities.csv import output_shopify_products_to_csv, output_ebay_feedback_to_csv, \
    output_joined_ebay_feedback_shopify_product_to_csv
from src.common.ebay.ebay_api_wrapper import EbayApiWrapper
from src.common.shopify.shopify_api_wrapper import ShopifyApiWrapper


def build_shopify_product_csv() -> List[ShopifyProductOutput]:
    shopify_wrapper = ShopifyApiWrapper()
    master_product_list = shopify_wrapper.create_master_product_list()
    output_shopify_products_to_csv(master_product_list)
    return master_product_list


def build_ebay_feedback_csv() -> List[EbayFeedbackOutput]:
    ebay_wrapper = EbayApiWrapper()
    feedback_details = ebay_wrapper.get_account_feedback()

    ebay_feedback_output_list = []
    for x in feedback_details:
        ebay_feedback_output_list.append(EbayFeedbackOutput(x))

    output_ebay_feedback_to_csv(ebay_feedback_output_list)
    return ebay_feedback_output_list


def create_shopify_review_upload_csv(product_list: List[ShopifyProductOutput],
                                     feedback_list: List[EbayFeedbackOutput]):
    # Join shopify products to eBay feedback by the product titles and handle the Shopify star rating
    rating_map = {
        'Positive': 5,
        'Neutral': 3,
        'Negative': 1
    }
    product_dict: dict[str, ShopifyProductOutput] = {product.title: product for product in product_list}

    for feedback in feedback_list:
        if product_dict.get(feedback.item_title) is not None:
            feedback.shopify_product_id = product_dict.get(feedback.item_title).product_id
        feedback.shopify_rating = rating_map.get(feedback.comment_type, 5)

    output_joined_ebay_feedback_shopify_product_to_csv(feedback_list)


if __name__ == '__main__':
    shopify_product_list = build_shopify_product_csv()
    ebay_feedback_list = build_ebay_feedback_csv()
    create_shopify_review_upload_csv(shopify_product_list, ebay_feedback_list)
