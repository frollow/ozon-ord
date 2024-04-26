import unittest
import json
from unittest.mock import patch
from ozon_ord.notification import Notification
from ozon_ord.models import NotificationQueryParams, ErrorListResponse


class TestNotification(unittest.TestCase):
    @patch("ozon_ord.notification.Notification.request")
    def test_get_error_list(self, mock_request):
        mock_response_json = {
            "notification": [
                {
                    "date": "2021-01-01T00:00:00Z",
                    "id": "1",
                    "objectId": "101",
                    "externalId": "001",
                    "objectType": "ERROR_NOTIFICATION_OBJECT_TYPE_INVOICE",
                    "text": "Error processing the invoice",
                    "updatedAt": "2021-01-02T00:00:00Z",
                    "url": "http://example.com/invoice/1",
                }
            ]
        }
        mock_request.return_value = json.dumps(mock_response_json)
        query_params = NotificationQueryParams(pageSize=1, gtNotificationId="1")
        response = Notification.get_error_list(query_params)
        self.assertIsInstance(response, ErrorListResponse)
        self.assertEqual(len(response.notification), 1)
        self.assertEqual(response.notification[0].id, "1")
        self.assertEqual(response.notification[0].text, "Error processing the invoice")


if __name__ == "__main__":
    unittest.main()
