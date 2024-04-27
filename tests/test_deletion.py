import unittest
from unittest.mock import patch, Mock
from ozon_ord.deletion import Deletion
import json
from ozon_ord.models import (
    DeleteItemRequest,
    DeleteOperationRequest,
    DeleteOperationObjectType,
    DeleteEntityCountResponse,
    ListRelatedResponse,
)


class TestDeletion(unittest.TestCase):
    @patch("ozon_ord.deletion.Deletion.request")
    def test_create_delete_operation(self, mock_request):
        # Предполагаем, что сервер возвращает успешный JSON-ответ
        mock_response_json = {}
        mock_request.return_value = json.dumps(mock_response_json)

        # Подготовка данных для запроса
        delete_item_request = DeleteOperationRequest(
            item=DeleteItemRequest(
                externalObjectId="12344",
                objectType="DELETE_OPERATION_OBJECT_TYPE_STATISTIC",
            )
        )
        # Вызов тестируемого метода
        response = Deletion.create_delete_operation(delete_item_request)
        # Проверка возвращаемых данных
        self.assertEqual(response.message, True)

    @patch("ozon_ord.deletion.Deletion.request")
    def test_get_entity_count(self, mock_request):
        # Подготовка мокированного ответа, который имитирует JSON от сервера
        mock_response_json = {
            "entityCount": [
                {"count": 5, "objectType": DeleteOperationObjectType.STATISTIC},
                {"count": 3, "objectType": DeleteOperationObjectType.CONTRACT},
            ]
        }
        mock_request.return_value = json.dumps(mock_response_json)

        # Подготовка данных для запроса
        delete_item_request = DeleteItemRequest(
            externalObjectId="123456", objectType=DeleteOperationObjectType.STATISTIC
        )

        # Вызов тестируемого метода
        response = Deletion.get_entity_count(delete_item_request)

        # Проверка возвращаемых данных
        self.assertIsInstance(response, DeleteEntityCountResponse)
        self.assertEqual(len(response.entityCount), 2)
        self.assertEqual(response.entityCount[0].count, 5)
        self.assertEqual(
            response.entityCount[0].objectType, DeleteOperationObjectType.STATISTIC
        )

    @patch("ozon_ord.deletion.Deletion.request")
    def test_get_related_entities(self, mock_request):
        # Подготовка мокированного ответа, который имитирует JSON от сервера
        mock_response_json = {
            "items": [
                {
                    "externalId": "external123",
                    "objectId": 12345,
                    "objectType": DeleteOperationObjectType.STATISTIC,
                },
                {
                    "externalId": "external456",
                    "objectId": 12346,
                    "objectType": DeleteOperationObjectType.CONTRACT,
                },
            ]
        }
        mock_request.return_value = json.dumps(mock_response_json)

        # Подготовка данных для запроса
        delete_item_request = DeleteItemRequest(
            externalObjectId="12345", objectType=DeleteOperationObjectType.STATISTIC
        )

        # Вызов тестируемого метода
        response = Deletion.get_related_entities(delete_item_request)

        # Проверка возвращаемых данных
        self.assertIsInstance(response, ListRelatedResponse)
        self.assertEqual(len(response.items), 2)
        self.assertEqual(response.items[0].externalId, "external123")
        self.assertEqual(response.items[0].objectId, 12345)
        self.assertEqual(
            response.items[0].objectType, DeleteOperationObjectType.STATISTIC
        )
        self.assertEqual(response.items[1].externalId, "external456")
        self.assertEqual(response.items[1].objectId, 12346)


if __name__ == "__main__":
    unittest.main()
