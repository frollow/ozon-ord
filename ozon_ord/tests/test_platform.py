import unittest
import json
from unittest.mock import patch
from ozon_ord.platform import Platform
from ozon_ord.models import (
    PlatformData,
    PlatformResponse,
    PlatformsResponse,
    BatchPlatformRequest,
    PlatformRequest,
    PlatformListRequest,
    PlatformListResponse,
    PlatformCursor,
    UpdatedAt,
)


class TestPlatform(unittest.TestCase):
    def setUp(self):
        self.platform_data = PlatformData(
            appName="Test App",
            externalPlatformId="test_id_1",
            platformType="PLATFORM_TYPE_SITE",
            url="http://test.com",
            comment="Test comment",
        )

        self.platforms_data = BatchPlatformRequest(
            platforms=[
                PlatformRequest(
                    appName="Test App One",
                    externalPlatformId="test_id_2",
                    platformType="PLATFORM_TYPE_SITE",
                    url="http://testappone.com",
                    comment="Test comment one",
                ),
                PlatformRequest(
                    appName="Test App Two",
                    externalPlatformId="test_id_3",
                    platformType="PLATFORM_TYPE_APP",
                    url="http://testapptwo.com",
                    comment="Test comment two",
                ),
            ]
        )

        self.list_request_data = PlatformListRequest(
            cursor=PlatformCursor(externalId="", updatedAt=UpdatedAt(updatedAt=None)),
            orderBy="ASC",
            pageSize=10,
        )

    @patch("ozon_ord.platform.Platform.request")
    def test_register_or_update_platform(self, mock_request):
        mock_json_response = {
            "platform": {
                "appName": "Test App",
                "createdAt": "2020-01-01T00:00:00Z",
                "createdBy": {
                    "email": "test@example.com",
                    "id": "123",
                    "name": "Tester",
                },
                "editedAt": "2020-01-02T00:00:00Z",
                "editedBy": {
                    "email": "editor@example.com",
                    "id": "124",
                    "name": "Editor",
                },
                "externalId": "ext_id_1",
                "platformId": "plat_id_1",
                "platformType": "PLATFORM_TYPE_SITE",
                "url": "http://test.com",
                "updatedAt": "2020-01-02T00:00:00Z",
                "comment": "Test comment",
            },
            "error": None,
        }

        mock_request.return_value = json.dumps(
            mock_json_response
        )  # Преобразование словаря в JSON-строку
        response = Platform.register_or_update_platform(self.platform_data)
        self.assertIsInstance(response, PlatformResponse)
        self.assertEqual(response.platform.appName, "Test App")
        self.assertIsNotNone(response.platform.createdBy)

    @patch("ozon_ord.platform.Platform.request")
    def test_register_or_update_multiple_platforms(self, mock_request):
        mock_json_response = {
            "platforms": [
                {
                    "appName": "Test App One",
                    "createdAt": "2020-01-01T00:00:00Z",
                    "createdBy": {
                        "email": "creator@example.com",
                        "id": "1",
                        "name": "Creator One",
                    },
                    "editedAt": "2020-01-02T00:00:00Z",
                    "editedBy": {
                        "email": "editor@example.com",
                        "id": "2",
                        "name": "Editor One",
                    },
                    "externalId": "ext1",
                    "platformId": "plat1",
                    "platformType": "PLATFORM_TYPE_SITE",
                    "url": "http://testappone.com",
                    "updatedAt": "2020-01-03T00:00:00Z",
                    "comment": "Test comment one",
                },
                {
                    "appName": "Test App Two",
                    "createdAt": "2020-01-04T00:00:00Z",
                    "createdBy": {
                        "email": "creator@example.com",
                        "id": "3",
                        "name": "Creator Two",
                    },
                    "editedAt": "2020-01-05T00:00:00Z",
                    "editedBy": {
                        "email": "editor@example.com",
                        "id": "4",
                        "name": "Editor Two",
                    },
                    "externalId": "ext2",
                    "platformId": "plat2",
                    "platformType": "PLATFORM_TYPE_APP",
                    "url": "http://testapptwo.com",
                    "updatedAt": "2020-01-06T00:00:00Z",
                    "comment": "Test comment two",
                },
            ],
            "error": None,
        }
        mock_request.return_value = json.dumps(
            mock_json_response
        )  # Преобразование словаря в JSON-строку
        response = Platform.register_or_update_multiple_platforms(self.platforms_data)
        self.assertIsInstance(response, PlatformsResponse)
        self.assertEqual(len(response.platforms), 2)
        self.assertEqual(response.platforms[0].appName, "Test App One")
        self.assertEqual(response.platforms[1].appName, "Test App Two")

    @patch("ozon_ord.platform.Platform.request")
    def test_get_platform_info(self, mock_request):
        # Полный и корректный JSON-ответ для площадки
        mock_json_response = {
            "platform": {
                "appName": "Test App",
                "createdAt": "2020-01-01T00:00:00Z",
                "createdBy": {
                    "email": "creator@test.com",
                    "id": "1",
                    "name": "Creator Name",
                },
                "editedAt": "2020-01-02T00:00:00Z",
                "editedBy": {
                    "email": "editor@test.com",
                    "id": "2",
                    "name": "Editor Name",
                },
                "externalId": "test_id_1",
                "platformId": "plat_id_1",
                "platformType": "PLATFORM_TYPE_SITE",
                "url": "http://test.com",
                "updatedAt": "2020-01-03T00:00:00Z",
                "comment": "Test comment",
            },
            "error": None,
        }
        # Убедитесь, что мок возвращает строку JSON, как это будет в реальном HTTP-вызове
        mock_request.return_value = json.dumps(mock_json_response)

        # Вызов тестируемого метода
        response = Platform.get_platform_info("test_id_1")

        # Проверки для валидации корректности ответа
        self.assertIsInstance(response, PlatformResponse)
        self.assertEqual(response.platform.appName, "Test App")
        self.assertIsNotNone(response.platform.createdBy)
        self.assertEqual(response.platform.createdBy.name, "Creator Name")

    @patch("ozon_ord.platform.Platform.request")
    def test_get_platform_list(self, mock_request):
        # Полный и корректный JSON-ответ для списка платформ
        mock_json_response = {
            "platform": [
                {
                    "appName": "Test App",
                    "createdAt": "2020-01-01T00:00:00Z",
                    "createdBy": {
                        "email": "creator@test.com",
                        "id": "1",
                        "name": "Creator Name",
                    },
                    "editedAt": "2020-01-02T00:00:00Z",
                    "editedBy": {
                        "email": "editor@test.com",
                        "id": "2",
                        "name": "Editor Name",
                    },
                    "externalId": "test_id_1",
                    "platformId": "plat_id_1",
                    "platformType": "PLATFORM_TYPE_SITE",
                    "url": "http://test.com",
                    "updatedAt": "2020-01-03T00:00:00Z",
                    "comment": "Test comment",
                }
            ],
            "error": None,
        }
        # Убедитесь, что мок возвращает строку JSON, как это будет в реальном HTTP-вызове
        mock_request.return_value = json.dumps(mock_json_response)

        # Вызов тестируемого метода
        response = Platform.get_platform_list(self.list_request_data)

        # Проверки для валидации корректности ответа
        self.assertIsInstance(response, PlatformListResponse)
        self.assertEqual(len(response.platform), 1)
        self.assertEqual(response.platform[0].appName, "Test App")


if __name__ == "__main__":
    unittest.main()
