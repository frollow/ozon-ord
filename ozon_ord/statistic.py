from .client import OzonORDClient
from .models import (
    StatisticList,
    ExternalExtUpsertStatisticResponse,
    StatisticListRequest,
    StatisticListResponse,
    StatisticResponse,
)


class Statistic(OzonORDClient):
    """Класс для работы со статистикой в API Ozon ORD."""

    @classmethod
    def add_statistics(cls, statistics_data: StatisticList) -> dict:
        """Добавление статистики."""
        endpoint = "/api/external/v2/statistic"
        response = cls.request("POST", endpoint, data=statistics_data.model_dump())
        return ExternalExtUpsertStatisticResponse.model_validate_json(response)

    @classmethod
    def get_statistic_list(cls, request_data: StatisticListRequest):
        """Получение списка статистик."""
        endpoint = "/api/external/v2/statistic/list"
        response = cls.request("POST", endpoint, data=request_data.model_dump())
        return StatisticListResponse.model_validate_json(response)

    @classmethod
    def get_statistic_info(cls, external_statistic_id: str):
        """Получение детальной информации о статистике."""
        endpoint = f"/api/external/v2/statistic/{external_statistic_id}"
        response = cls.request("GET", endpoint)
        return StatisticResponse.model_validate_json(response)
