from .client import OzonORDClient
from .models import (
    CreativeData,
    CreativeResponse,
    CreativesListRequest,
    CreativesListResponse,
)


class Creative(OzonORDClient):
    """Класс для работы с креативами в API Ozon ORD."""

    @classmethod
    def register_or_update_creative(
        cls, creative_data: CreativeData
    ) -> CreativeResponse:
        """Регистрация или обновление данных о креативе."""
        endpoint = "/api/external/creative"
        response = cls.request("POST", endpoint, data=creative_data.model_dump())
        return CreativeResponse.model_validate_json(response)

    @classmethod
    def get_creative_info(cls, externalCreativeId: str) -> CreativeResponse:
        """Получение информации о креативе по идентификатору."""
        endpoint = f"/api/external/creative/{externalCreativeId}"
        response = cls.request("GET", endpoint)
        return CreativeResponse.model_validate_json(response)

    @classmethod
    def get_creatives_list(
        cls, request_data: CreativesListRequest
    ) -> CreativesListResponse:
        """Получает список креативов по заданным критериям."""
        endpoint = "/api/external/creative/list"
        response = cls.request("POST", endpoint, data=request_data.model_dump())
        return CreativesListResponse.model_validate_json(response)
