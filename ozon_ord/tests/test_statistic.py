import unittest
from unittest.mock import patch
import json
from ozon_ord.statistic import Statistic
from ozon_ord.models import (
    StatisticList,
    StatisticListRequest,
    StatisticResponse,
    ExternalExtUpsertStatisticResponse,
    ExternalExtStatistic,
    ExternalCursorStatistic,
    StatisticListResponse,
)


class TestStatistic(unittest.TestCase):
    @patch("ozon_ord.statistic.Statistic.request")
    def test_add_statistics(self, mock_request):
        mock_response = json.dumps({"message": "True"})
        mock_request.return_value = mock_response
        statistics_data = StatisticList(
            statistics=[
                ExternalExtStatistic(
                    creativeId="1",
                    dateEndFact="2022-01-01",
                    dateEndPlan="2022-01-02",
                    dateStartFact="2022-01-01",
                    dateStartPlan="2022-01-02",
                    externalCreativeId="ext123",
                    externalPlatformId="plat456",
                    externalStatisticId="stat789",
                    moneySpent="100",
                    unitCost="10",
                    viewsCountByFact="1000",
                    viewsCountByInvoice="950",
                    withNds=True,
                    comment="Initial load",
                )
            ]
        )
        response = Statistic.add_statistics(statistics_data)
        self.assertIsInstance(response, ExternalExtUpsertStatisticResponse)
        self.assertEqual(response.message, "True")
        mock_request.assert_called_once_with(
            "POST", "/api/external/v2/statistic", data=statistics_data.model_dump()
        )

    @patch("ozon_ord.statistic.Statistic.request")
    def test_get_statistic_list(self, mock_request):
        mock_response = json.dumps(
            {
                "items": [
                    {
                        "contractId": "12345",
                        "createdAt": "2022-01-01T12:00:00Z",
                        "createdBy": {
                            "email": "creator@example.com",
                            "id": "100",
                            "name": "Creator",
                        },
                        "creativeName": "Test Ad",
                        "creativeType": "ADV_OBJECT_TYPE_BANNER",
                        "editedAt": "2022-01-02T12:00:00Z",
                        "editedBy": {
                            "email": "editor@example.com",
                            "id": "101",
                            "name": "Editor",
                        },
                        "externalContractId": "extContract123",
                        "externalInvoiceId": "extInvoice123",
                        "invoiceId": "invoice123",
                        "platformName": "Test Platform",
                        "platformType": "PLATFORM_TYPE_SITE",
                        "statistic": {
                            "creativeId": "123",
                            "dateEndFact": "2022-12-31",
                            "dateEndPlan": "2022-12-31",
                            "dateStartFact": "2022-01-01",
                            "dateStartPlan": "2022-01-01",
                            "externalCreativeId": "ext456",
                            "externalPlatformId": "plat789",
                            "externalStatisticId": "stat012",
                            "moneySpent": "10000",
                            "platformId": "plat123",
                            "statisticId": "stat345",
                            "unitCost": "500",
                            "viewsCountByFact": "100000",
                            "viewsCountByInvoice": "95000",
                            "withNds": True,
                            "comment": "Initial load",
                        },
                        "comment": "Detailed Comment",
                    }
                ]
            }
        )
        mock_request.return_value = mock_response
        request_data = StatisticListRequest(
            cursor=ExternalCursorStatistic(externalId="last_seen_id"), pageSize=20
        )
        response = Statistic.get_statistic_list(request_data)
        mock_request.assert_called_once_with(
            "POST", "/api/external/v2/statistic/list", data=request_data.model_dump()
        )
        response_model = StatisticListResponse.model_validate_json(
            mock_request.return_value
        )
        self.assertIsInstance(response_model, StatisticListResponse)
        self.assertEqual(response_model.items[0].creativeName, "Test Ad")

    @patch("ozon_ord.statistic.Statistic.request")
    def test_get_statistic_info(self, mock_request):
        mock_response = json.dumps(
            {
                "creativeName": "Test Ad",
                "creativeType": "ADV_OBJECT_TYPE_BANNER",
                "platformName": "Test Platform",
                "platformType": "PLATFORM_TYPE_SITE",
                "statistic": {
                    "creativeId": "123",
                    "dateEndFact": "2022-12-31",
                    "dateEndPlan": "2022-12-31",
                    "dateStartFact": "2022-01-01",
                    "dateStartPlan": "2022-01-01",
                    "externalCreativeId": "ext456",
                    "externalPlatformId": "plat789",
                    "externalStatisticId": "stat012",
                    "moneySpent": "10000",
                    "platformId": "plat123",
                    "statisticId": "stat345",
                    "unitCost": "500",
                    "viewsCountByFact": "100000",
                    "viewsCountByInvoice": "95000",
                    "withNds": True,
                    "comment": "Initial load",
                },
                "comment": "Detailed Comment",
            }
        )
        mock_request.return_value = mock_response
        externalStatisticId = "123"
        response = Statistic.get_statistic_info(externalStatisticId)
        mock_request.assert_called_once_with(
            "GET", f"/api/external/v2/statistic/{externalStatisticId}"
        )
        response_model = StatisticResponse.model_validate_json(
            mock_request.return_value
        )
        self.assertIsInstance(response_model, StatisticResponse)
        self.assertEqual(response_model.creativeName, "Test Ad")


if __name__ == "__main__":
    unittest.main()
