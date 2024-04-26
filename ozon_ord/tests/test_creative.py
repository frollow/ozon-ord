import unittest
from unittest.mock import patch
from ozon_ord.creative import Creative
from ozon_ord.models import (
    CreativeData,
    ExternalMediaData,
    UrlListData,
    CreativeResponse,
    CreativesListRequest,
    ExternalCursorCreative,
    CreativesListResponse,
)


class TestCreative(unittest.TestCase):
    def setUp(self):
        self.creative_data = CreativeData(
            title="Заголовок для креатива",
            advObjectType="ADV_OBJECT_TYPE_TEXT_BLOCK",
            description="Описание нового креатива.",
            externalContractIds=["doc-123456789"],
            externalCreativeId="creative-id-99988898",
            geoTargets=[],
            isSocialAdv=False,
            isNative=False,
            mediaData=[ExternalMediaData(text="Текстовый контент для креатива")],
            okvedCodes=["60.10"],
            paymentType="PAYMENT_TYPE_CPM",
            urlList=[
                UrlListData(url="https://example.com/target-1"),
                UrlListData(url="https://example.com/target-2"),
            ],
        )

    @patch("ozon_ord.creative.Creative.request")
    def test_register_or_update_creative_success(self, mock_request):
        mock_response_json = """
        {
            "creative": {
                "advObjectType": "ADV_OBJECT_TYPE_TEXT_BLOCK",
                "createdAt": "2024-04-17T12:34:56Z",
                "createdBy": {
                    "id": "creator123",
                    "email": "creator@example.com",
                    "name": "Creator Name"
                },
                "creativeId": "creative-id-99988898",
                "editedAt": "2024-04-18T12:00:00Z",
                "editedBy": {
                    "id": "editor456",
                    "email": "editor@example.com",
                    "name": "Editor Name"
                },
                "description": "Описание нового креатива.",
                "externalContractId": "contract123",
                "externalCreativeId": "external-id-123456",
                "geoTargets": [
                    {
                        "guid": "geo123",
                        "name": "Target Location"
                    }
                ],
                "isSocialAdv": false,
                "marker": "Marker123",
                "mediaData": [
                    {
                        "description": "Media Description",
                        "text": "Текстовый контент для креатива",
                        "file": {
                            "id": "file123",
                            "originalUrl": "https://example.com/original.png",
                            "url": "https://example.com/url.png"
                        }
                    }
                ],
                "okvedCodes": ["60.10"],
                "paymentType": "PAYMENT_TYPE_CPM",
                "targetLink": "https://example.com/target-link",
                "title": "Заголовок для креатива",
                "updatedAt": "2024-04-19T13:14:15Z",
                "urlList": [
                    {
                        "url": "https://example.com/target-1"
                    },
                    {
                        "url": "https://example.com/target-2"
                    }
                ],
                "comment": "Additional comments about the creative."
            }
        }"""

        mock_request.return_value = mock_response_json
        response = Creative.register_or_update_creative(self.creative_data)
        self.assertIsInstance(response, CreativeResponse)
        self.assertEqual(response.creative.creativeId, "creative-id-99988898")
        self.assertEqual(response.creative.title, "Заголовок для креатива")
        mock_request.assert_called_once_with(
            "POST", "/api/external/creative", data=self.creative_data.model_dump()
        )

    @patch("ozon_ord.creative.Creative.request")
    def test_get_creative_info(self, mock_request):
        mock_response_json = """
        {
            "creative": {
                "advObjectType": "ADV_OBJECT_TYPE_TEXT_BLOCK",
                "createdAt": "2024-04-17T12:34:56Z",
                "createdBy": {
                    "id": "creator123",
                    "email": "creator@example.com",
                    "name": "Creator Name"
                },
                "creativeId": "creative-id-99988898",
                "editedAt": "2024-04-18T12:00:00Z",
                "editedBy": {
                    "id": "editor456",
                    "email": "editor@example.com",
                    "name": "Editor Name"
                },
                "description": "Описание нового креатива.",
                "externalContractId": "contract123",
                "externalCreativeId": "external-id-123456",
                "geoTargets": [
                    {
                        "guid": "geo123",
                        "name": "Target Location"
                    }
                ],
                "isSocialAdv": false,
                "marker": "Marker123",
                "mediaData": [
                    {
                        "description": "Media Description",
                        "text": "Текстовый контент для креатива",
                        "file": {
                            "id": "file123",
                            "originalUrl": "https://example.com/original.png",
                            "url": "https://example.com/url.png"
                        }
                    }
                ],
                "okvedCodes": ["60.10"],
                "paymentType": "PAYMENT_TYPE_CPM",
                "targetLink": "https://example.com/target-link",
                "title": "Заголовок для креатива",
                "updatedAt": "2024-04-19T13:14:15Z",
                "urlList": [
                    {
                        "url": "https://example.com/target-1"
                    },
                    {
                        "url": "https://example.com/target-2"
                    }
                ],
                "comment": "Additional comments about the creative."
            }
        }"""

        mock_request.return_value = mock_response_json
        response = Creative.get_creative_info("creative-id-99988898")
        self.assertIsInstance(response, CreativeResponse)
        self.assertEqual(response.creative.creativeId, "creative-id-99988898")
        self.assertEqual(response.creative.title, "Заголовок для креатива")
        mock_request.assert_called_once_with(
            "GET", "/api/external/creative/creative-id-99988898"
        )

    @patch("ozon_ord.creative.Creative.request")
    def test_get_creatives_list(self, mock_request):
        mock_response_json = """
        {
            "creative": [
                {
                    "advObjectType": "ADV_OBJECT_TYPE_TEXT_BLOCK",
                    "createdAt": "2024-04-17T12:34:56Z",
                    "createdBy": {
                        "id": "creator123",
                        "email": "creator@example.com",
                        "name": "Creator Name"
                    },
                    "creativeId": "creative-id-99988898",
                    "editedAt": "2024-04-18T12:00:00Z",
                    "editedBy": {
                        "id": "editor456",
                        "email": "editor@example.com",
                        "name": "Editor Name"
                    },
                    "description": "Описание нового креатива.",
                    "externalContractId": "contract123",
                    "externalCreativeId": "external-id-123456",
                    "geoTargets": [
                        {
                            "guid": "geo123",
                            "name": "Target Location"
                        }
                    ],
                    "isSocialAdv": false,
                    "marker": "Marker123",
                    "mediaData": [
                        {
                            "description": "Media Description",
                            "text": "Текстовый контент для креатива",
                            "file": {
                                "id": "file123",
                                "originalUrl": "https://example.com/original.png",
                                "url": "https://example.com/url.png"
                            }
                        }
                    ],
                    "okvedCodes": ["60.10"],
                    "paymentType": "PAYMENT_TYPE_CPM",
                    "targetLink": "https://example.com/target-link",
                    "title": "Заголовок для креатива",
                    "updatedAt": "2024-04-19T13:14:15Z",
                    "urlList": [
                        {
                            "url": "https://example.com/target-1"
                        },
                        {
                            "url": "https://example.com/target-2"
                        }
                    ],
                    "comment": "Additional comments about the creative."
                }
            ]
        }"""

        mock_request.return_value = mock_response_json
        request_data = CreativesListRequest(
            cursor=ExternalCursorCreative(
                externalId="lastId", updatedAt={"updatedAt": "2024-04-17T12:34:56Z"}
            ),
            orderBy="ASC",
            pageSize=10,
        )
        response = Creative.get_creatives_list(request_data)
        self.assertIsInstance(response, CreativesListResponse)
        self.assertEqual(len(response.creative), 1)
        self.assertEqual(response.creative[0].creativeId, "creative-id-99988898")
        self.assertEqual(response.creative[0].title, "Заголовок для креатива")
        mock_request.assert_called_once_with(
            "POST", "/api/external/creative/list", data=request_data.model_dump()
        )


if __name__ == "__main__":
    unittest.main()
