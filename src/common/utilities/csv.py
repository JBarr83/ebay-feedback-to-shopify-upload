import csv
from typing import List

from src.common.models.ebay_feedback_output import EbayFeedbackOutput
from src.common.models.shopify_product_output import ShopifyProductOutput


def output_shopify_products_to_csv(product_output_list: List[ShopifyProductOutput]):
    fields = ['Title', 'ID', 'Vendor']
    with open('../../shopify_products.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(fields)
        for product in product_output_list:
            writer.writerow([product.title, product.product_id, product.vendor])


def output_ebay_feedback_to_csv(feedback_list: List[EbayFeedbackOutput]):
    fields = ['Item Title',
              'Item ID',
              'Comment Type',
              'Comment Text',
              'Comment User',
              'Comment Date',
              'Feedback Star Rating']
    with open('../../ebay_feedback.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(fields)
        for feedback in feedback_list:
            writer.writerow([feedback.item_title,
                             feedback.item_id,
                             feedback.comment_type,
                             feedback.comment_text,
                             feedback.comment_user,
                             feedback.comment_date,
                             feedback.feedback_star_rating])


def output_joined_ebay_feedback_shopify_product_to_csv(feedback_list: List[EbayFeedbackOutput]):
    fields = ['product_id', 'body', 'reviewer_name', 'review_date', 'rating']
    with open('../../ebay_to_shopify_review_import.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(fields)
        for feedback in feedback_list:
            writer.writerow([
                feedback.shopify_product_id,
                feedback.comment_text,
                feedback.comment_user,
                feedback.comment_date,
                feedback.shopify_rating
            ])
