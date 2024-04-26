from .client import OzonORDClient
from .models import (
    NotificationQueryParams,
    ErrorListResponse,
)


class Notification(OzonORDClient):
    """Класс для получения списка ошибок в API Ozon ORD."""

    @classmethod
    def get_error_list(cls, query_params: NotificationQueryParams) -> ErrorListResponse:
        """Метод для получения списка ошибок валидации объектов в ЕРИР."""
        endpoint = "/api/external/notification/error_list"
        response = cls.request("POST", endpoint, data=query_params.model_dump())
        return ErrorListResponse.model_validate_json(response)
