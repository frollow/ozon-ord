from .client import OzonORDClient
from .models import (
    InvoiceRequestData,
    InvoiceResponse,
    InvoiceFilter,
    InvoiceListResponse,
    CreativeLinkRequest,
    CreativeUnlinkRequest,
    CreativeInvoiceLinkQuery,
    CreativeInvoiceLinksResponse,
)


class Invoice(OzonORDClient):
    """Класс для работы с актами в API Ozon ORD."""

    @classmethod
    def register_or_update_invoice(
        cls, invoice_data: InvoiceRequestData
    ) -> InvoiceResponse:
        """Добавление или обновление данных акта."""
        endpoint = "/api/external/v2/invoice"
        response = cls.request("POST", endpoint, data=invoice_data.model_dump())
        return InvoiceResponse.model_validate_json(response)

    @classmethod
    def get_invoice_info(cls, externalInvoiceId: str) -> InvoiceResponse:
        """Получение информации об акте по его идентификатору."""
        endpoint = f"/api/external/v2/invoice/{externalInvoiceId}"
        response = cls.request("GET", endpoint)
        return InvoiceResponse.model_validate_json(response)

    @classmethod
    def get_invoice_list(cls, filter_data: InvoiceFilter) -> InvoiceListResponse:
        """Получение списка актов по заданным фильтрам."""
        endpoint = "/api/external/v2/invoice/list"
        response = cls.request("POST", endpoint, data=filter_data.model_dump())
        return InvoiceListResponse.model_validate_json(response)

    @classmethod
    def link_creatives_to_invoice(cls, link_data: CreativeLinkRequest) -> dict:
        """Добавление креативов к акту."""
        endpoint = "/api/external/v3/invoice/creative/link"
        response = cls.request("POST", endpoint, data=link_data.model_dump())
        return response

    @classmethod
    def unlink_creatives_from_invoice(cls, unlink_data: CreativeUnlinkRequest) -> dict:
        """Удаление креативов из акта."""
        endpoint = "/api/external/v3/invoice/creative/unlink"
        response = cls.request("POST", endpoint, data=unlink_data.model_dump())
        return response

    @classmethod
    def get_creative_invoice_links(
        cls, query_params: CreativeInvoiceLinkQuery
    ) -> CreativeInvoiceLinksResponse:
        """Получение списка связей между креативами и детализациями актов."""
        endpoint = "/api/external/v3/invoice/creative"
        response = cls.request("GET", endpoint, data=query_params.model_dump())
        return CreativeInvoiceLinksResponse.model_validate_json(response)
