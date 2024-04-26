from pydantic import TypeAdapter
from .client import OzonORDClient
from .models import (
    BankInfo,
    BankDictionaryRequest,
    CountryInfo,
    CountryDictionaryRequest,
    FiasInfo,
    FiasDictionaryRequest,
    OkvedInfo,
    OkvedDictionaryRequest,
)


class Dictionary(OzonORDClient):
    """Класс для работы со справочниками в API Ozon ORD."""

    @staticmethod
    def custom_list_adapter(response, pydentic_model):
        """Адаптер для преобразования списка данных JSON в список объектов Pydantic."""
        adapter = TypeAdapter(pydentic_model)
        return [adapter.validate_python(item) for item in response.json()]

    @staticmethod
    def full_endpoint(endpoint, request_data):
        """Метод добавляет query параметры к url."""
        query_string = "&".join(
            [
                f"{key}={value}"
                for key, value in request_data.query_data().items()
                if value is not None
            ]
        )
        return f"{endpoint}?{query_string}"

    @classmethod
    def get_bank_info(
        cls, request_data: BankDictionaryRequest, format: str = "application/json"
    ) -> list:
        """Метод для получения данных из справочника Банка России."""
        endpoint = "/api/external/dict/bank"
        headers = {"Accept": format}
        full_endpoint = cls.full_endpoint(endpoint, request_data)
        response = cls.request(
            "POST",
            full_endpoint,
            data=request_data.model_dump(),
            headers=headers,
            raw_response=True,
        )
        return cls.custom_list_adapter(response, BankInfo)

    @classmethod
    def get_country_info(
        cls, request_data: CountryDictionaryRequest, format: str = "application/json"
    ) -> list:
        """Метод для получения данных из cправочника идентификаторов стран ОКСМ"""
        endpoint = "/api/external/dict/oksm"
        headers = {"Accept": format}
        full_endpoint = cls.full_endpoint(endpoint, request_data)
        response = cls.request(
            "POST",
            full_endpoint,
            data=request_data.model_dump(),
            headers=headers,
            raw_response=True,
        )
        return cls.custom_list_adapter(response, CountryInfo)

    @classmethod
    def get_fias_info(
        cls, request_data: FiasDictionaryRequest, format: str = "application/json"
    ) -> list:
        """Метод для получения данных об объектах на территории России. ФИАС"""
        endpoint = "/api/external/dict/fias"
        headers = {"Accept": format}
        full_endpoint = cls.full_endpoint(endpoint, request_data)
        response = cls.request(
            "POST",
            full_endpoint,
            data=request_data.model_dump(),
            headers=headers,
            raw_response=True,
        )
        return cls.custom_list_adapter(response, FiasInfo)

    @classmethod
    def get_okved_info(
        cls, request_data: OkvedDictionaryRequest, format: str = "application/json"
    ) -> list:
        """Справочник по видам экономической деятельности (ОКВЭД)"""
        endpoint = "/api/external/dict/okved"
        headers = {"Accept": format}
        full_endpoint = cls.full_endpoint(endpoint, request_data)
        response = cls.request(
            "POST",
            full_endpoint,
            data=request_data.model_dump(),
            headers=headers,
            raw_response=True,
        )
        return cls.custom_list_adapter(response, OkvedInfo)
