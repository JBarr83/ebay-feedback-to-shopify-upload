from ebaysdk.exception import ConnectionError as EbayConnectionError
from ebaysdk.trading import Connection as EbayTradingConnection

from src.common.utilities.common_utilities import get_credentials_file


class EbayApiWrapper:
    def __init__(self):
        self.credentials = get_credentials_file()
        self.trading_api = EbayTradingConnection(appid=self.credentials['sunshine_hut']['ebay']['app_id'],
                                                 devid=self.credentials['sunshine_hut']['ebay']['dev_id'],
                                                 certid=self.credentials['sunshine_hut']['ebay']['cert_id'],
                                                 token=self.credentials['sunshine_hut']['ebay']['token'],
                                                 config_file=None)

    def get_account_feedback(self):
        try:
            feedback_query_data = {
                'UserID': self.credentials['sunshine_hut']['ebay']['user_id'],
                'DetailLevel': 'ReturnAll',
                'Pagination': {
                    'EntriesPerPage': 200,
                    'PageNumber': 0
                }
            }

            response = self.trading_api.execute('GetFeedback', feedback_query_data)

            if response.reply.Ack == 'Success':
                feedback_total_pages = int(response.reply.PaginationResult.TotalNumberOfPages)
                master_feedback_details = response.reply.FeedbackDetailArray.FeedbackDetail

                print('Total Pages: ' + str(feedback_total_pages))
                for x in range(2, feedback_total_pages + 1):
                    feedback_query_data['Pagination']['PageNumber'] = x
                    response = self.trading_api.execute('GetFeedback', feedback_query_data)
                    if response.reply.Ack == 'Success':
                        master_feedback_details = [*master_feedback_details,
                                                   *response.reply.FeedbackDetailArray.FeedbackDetail]
                    else:
                        print('Error retrieving feedback page: ' + str(x))

                return master_feedback_details

        except EbayConnectionError as e:
            print(e)
            return None
