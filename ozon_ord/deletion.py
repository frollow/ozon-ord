from .client import OzonORDClient
from .models import (
    DeleteItemRequest,
    DeleteOperationResponse,
    DeleteEntityCountResponse,
    ListRelatedResponse,
)


class Deletion(OzonORDClient):
    """Класс для обработки операций удаления в API Ozon ORD."""

    @classmethod
    def create_delete_operation(cls, delete_request: DeleteItemRequest) -> dict:
        """Метод для создания запроса на удаление данных из различных разделов рекламного кабинета."""
        endpoint = "/api/external/delete_operation/create"
        response = cls.request("POST", endpoint, data=delete_request.model_dump())
        return DeleteOperationResponse.model_validate_json(response)

    @classmethod
    def get_entity_count(
        cls, request_data: DeleteItemRequest
    ) -> DeleteEntityCountResponse:
        """Метод для получения количества вложенных объектов по заданному типу объекта."""
        endpoint = "/api/external/delete_operation/entity_count"
        response = cls.request("POST", endpoint, data=request_data.model_dump())
        return DeleteEntityCountResponse.model_validate_json(response)

    @classmethod
    def get_related_entities(
        cls, request_data: DeleteItemRequest
    ) -> ListRelatedResponse:
        """Метод для получения списка связанных сущностей по идентификатору объекта."""
        endpoint = "/api/external/delete_operation/related_entities"
        response = cls.request("POST", endpoint, data=request_data.model_dump())
        return ListRelatedResponse.model_validate_json(response)
