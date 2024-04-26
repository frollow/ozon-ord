from .client import OzonORDClient
from .models import (
    PlatformData,
    PlatformResponse,
    PlatformsResponse,
    BatchPlatformRequest,
    PlatformListRequest,
    PlatformListResponse,
)


class Platform(OzonORDClient):
    """Класс для работы с площадками в API Ozon ORD."""

    @classmethod
    def register_or_update_platform(
        cls, platform_data: PlatformData
    ) -> PlatformResponse:
        """Регистрация или обновление данных площадки."""
        endpoint = "/api/external/platform"
        response = cls.request("POST", endpoint, data=platform_data.model_dump())
        return PlatformResponse.model_validate_json(response)

    @classmethod
    def register_or_update_multiple_platforms(
        cls, platforms_data: BatchPlatformRequest
    ) -> PlatformsResponse:
        """Регистрация или обновление данных для нескольких площадок."""
        endpoint = "/api/external/platform/batch"
        response = cls.request("POST", endpoint, data=platforms_data.model_dump())
        return PlatformsResponse.model_validate_json(response)

    @classmethod
    def get_platform_info(cls, externalPlatformId: str) -> PlatformResponse:
        """Получение информации о площадке."""
        endpoint = f"/api/external/platform/{externalPlatformId}"
        response = cls.request("GET", endpoint)
        return PlatformResponse.model_validate_json(response)

    @classmethod
    def get_platform_list(
        cls, request_data: PlatformListRequest
    ) -> PlatformListResponse:
        """Получение списка площадок."""
        endpoint = "/api/external/platform/list"
        response = cls.request("POST", endpoint, data=request_data.model_dump())
        return PlatformListResponse.model_validate_json(response)
