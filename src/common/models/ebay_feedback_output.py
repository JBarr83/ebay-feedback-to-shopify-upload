from datetime import datetime


def get_api_value(ebay_feedback, attribute_name):
    if hasattr(ebay_feedback, attribute_name):
        return getattr(ebay_feedback, attribute_name)
    return ''


class EbayFeedbackOutput:
    def __init__(self, ebay_feedback):
        self.item_id = get_api_value(ebay_feedback, 'ItemID')
        self.item_title = get_api_value(ebay_feedback, 'ItemTitle')
        self.comment_type = get_api_value(ebay_feedback, 'CommentType')
        self.comment_text = get_api_value(ebay_feedback, 'CommentText')
        self.comment_user = get_api_value(ebay_feedback, 'CommentingUser')
        self.feedback_star_rating = get_api_value(ebay_feedback, 'FeedbackRatingStar')

        comment_date = get_api_value(ebay_feedback, 'CommentTime')

        if isinstance(comment_date, datetime):
            self.comment_date = comment_date.strftime("%d/%m/%Y")
        else:
            self.comment_date = ''
