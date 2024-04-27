from ozon_ord.client import OzonORDClient
from ozon_ord.invoice import Invoice
from ozon_ord.models import (
    InvoiceRequestData,
    ExternalContract,
    InvoiceFilter,
    InvoiceCursor,
    CreativeLinkRequest,
    CreativeLinkItem,
    CreativeUnlinkRequest,
    CreativeUnlinkItem,
    CreativeInvoiceLinkQuery,
)

OzonORDClient.set_environment(environment="TEST")

# Зарегистрировать или обновить данные акта (версия 2)
invoice_data = InvoiceRequestData(
    clientRole="ORGANISATION_ROLE_RD",
    contractorRole="ORGANISATION_ROLE_RR",
    contracts=[
        ExternalContract(externalContractId="doc-123456789", price="7000", withNds=True)
    ],
    endDate="2024-04-24",
    externalContractId="doc-123456789",
    externalInvoiceId="33399",
    invoiceDate="2024-04-21",
    invoiceNumber="n-rr-11",
    price="7000",
    startDate="2024-04-22",
    violation=["None"],
    withNds=True,
    comment="",
)

response = Invoice.register_or_update_invoice(invoice_data)
print(response)

# Информация об акте (версия 2)
external_invoice_id = "33399"
response = Invoice.get_invoice_info(external_invoice_id)
print(response)

# Список актов
filter_data = InvoiceFilter(
    cursor=InvoiceCursor(externalId="", updatedAt={}), orderBy="ASC", pageSize=10
)

response = Invoice.get_invoice_list(filter_data)
print(response)


# Добавить креативы к детализации акта
link_data = CreativeLinkRequest(
    items=[
        CreativeLinkItem(
            externalContractId="doc-123456789",
            externalCreativeIds=["creative-id-99988899"],
            externalInvoiceId="33399",
        )
    ]
)

response = Invoice.link_creatives_to_invoice(link_data)
print(response)


# Удалить все креативы из детализации акта
unlink_data = CreativeUnlinkRequest(
    items=[
        CreativeUnlinkItem(
            deleteAllCreatives=True,
            externalContractId="doc-123456789",
            externalInvoiceId="33399",
        )
    ]
)

response = Invoice.unlink_creatives_from_invoice(unlink_data)
print(response)

# Удалить креативы из детализации акта
unlink_data = CreativeUnlinkRequest(
    items=[
        CreativeUnlinkItem(
            deleteAllCreatives=False,
            externalCreativeIds=["creative-id-99988899"],
            externalContractId="doc-123456789",
            externalInvoiceId="33399",
        )
    ]
)

response = Invoice.unlink_creatives_from_invoice(unlink_data)
print(response)


# Список связей между креативами и детализациями актов
query_params = CreativeInvoiceLinkQuery(
    externalInvoiceIds=["creative-id-99988899"], pageSize=20, cursor="0"
)

response = Invoice.get_creative_invoice_links(query_params)
print(response)
