from .client import OzonORDClient
from .models import (
    ContractResponse,
    ContractData,
    ContractsListRequest,
    ContractsListResponse,
)


class Contract(OzonORDClient):
    """Класс для работы с договорами в API Ozon ORD."""

    @classmethod
    def register_or_update_contract(
        cls, contract_data: ContractData
    ) -> ContractResponse:
        """Регистрация или обновление данных договора."""
        endpoint = "/api/external/contract"
        response = cls.request("POST", endpoint, data=contract_data.model_dump())
        return ContractResponse.model_validate_json(response)

    @classmethod
    def get_contract_info(cls, externalContractId: str) -> ContractResponse:
        """Получение информации о договоре по идентификатору."""
        endpoint = f"/api/external/contract/{externalContractId}"
        response = cls.request("GET", endpoint)
        return ContractResponse.model_validate_json(response)

    @classmethod
    def get_contracts_list(
        cls, request_data: ContractsListRequest
    ) -> ContractsListResponse:
        """Получает список договоров по заданным критериям."""
        endpoint = "/api/ord-api/api/external/contract/list"
        response = cls.request("POST", endpoint, data=request_data.model_dump())
        return ContractsListResponse.model_validate_json(response)
