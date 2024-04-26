from .client import OzonORDClient
from .models import (
    OrganisationData,
    OrganisationResponse,
    AddOrganisationPlatformRequest,
    OrganisationListRequest,
    OrganisationListResponse,
)


class Organisation(OzonORDClient):
    """Класс для работы с контрагентами в API Ozon ORD."""

    @classmethod
    def register_or_update_organisation(
        cls, organisation_data: OrganisationData
    ) -> OrganisationResponse:
        """Регистрация или обновление данных контрагента."""
        endpoint = "/api/external/organisation"
        response = cls.request("POST", endpoint, data=organisation_data.model_dump())
        return OrganisationResponse.model_validate_json(response)

    @classmethod
    def get_organisation_info(cls, externalOrganisationId: str) -> OrganisationResponse:
        """Получение информации о контрагенте по его идентификатору."""
        endpoint = f"/api/external/organisation/{externalOrganisationId}"
        response = cls.request("GET", endpoint)
        return OrganisationResponse.model_validate_json(response)

    @classmethod
    def add_platforms_to_organisation(
        cls, externalOrganisationId: str, platform_data: AddOrganisationPlatformRequest
    ) -> dict:
        """Добавление площадок к контрагенту."""
        endpoint = f"/api/external/organisation/{externalOrganisationId}/platform"
        response = cls.request("POST", endpoint, data=platform_data.model_dump())
        return response

    @classmethod
    def get_organisation_list(
        cls, request_data: OrganisationListRequest
    ) -> OrganisationListResponse:
        """Метод для получения списка контрагентов с фильтрацией и пагинацией."""
        endpoint = "/api/external/organisation/list"
        response = cls.request("POST", endpoint, data=request_data.model_dump())
        return OrganisationListResponse.model_validate_json(response)
