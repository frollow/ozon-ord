from ozon_ord.client import OzonORDClient
from ozon_ord.organisation import Organisation
from ozon_ord.models import (
    OrganisationData,
    AddOrganisationPlatformRequest,
    ExternalOrganisationPlatform,
    OrganisationListRequest,
    ExternalCursorOrg,
)

OzonORDClient.set_environment(environment="TEST")

# Регистрация или обновление данных контрагента
organisation_data = OrganisationData(
    externalOrganisationId="12345",
    fullOpf="ООО 'Ромашка'",
    inn="8806046968",
    isOpc=False,
    isPp=False,
    legalAddress={
        "address": "123456, Москва, ул. Пушкина, д. Колотушкина",
        "locality": "Москва",
        "postcode": "123456",
    },
    legalType="LEGAL_TYPE_LEGAL",
    postAddress={
        "address": "123456, Москва, ул. Солнечная, д. 1",
        "locality": "Москва",
        "postcode": "654321",
    },
)

response = Organisation.register_or_update_organisation(organisation_data)
print(response)

organisation_data = OrganisationData(
    externalOrganisationId="4888933",
    fullOpf="ООО 'Техника'",
    inn="3728614192",
    isOpc=False,
    isPp=False,
    legalAddress={
        "address": "123456, Москва, ул. Пушкина, д. Колотушкина 2",
        "locality": "Москва",
        "postcode": "123456",
    },
    legalType="LEGAL_TYPE_LEGAL",
    postAddress={
        "address": "123456, Москва, ул. Солнечная, д. 3",
        "locality": "Москва",
        "postcode": "654321",
    },
)

response = Organisation.register_or_update_organisation(organisation_data)
print(response)


# Информация о контрагенте
externalOrganisationId = "12345"
response = Organisation.get_organisation_info(externalOrganisationId)
print(response)

# Добавление площадки к контрагенту
platform_data = AddOrganisationPlatformRequest(
    platform=[
        ExternalOrganisationPlatform(
            externalPlatformId="example_id_88", isPlatformOwner=False
        ),
        # Добавить больше площадок при необходимости
    ]
)

externalOrganisationId = "12345"
response = Organisation.add_platforms_to_organisation(
    externalOrganisationId, platform_data
)
print(response)


# Список контрагентов
request_data = OrganisationListRequest(
    cursor=ExternalCursorOrg(externalId="", updatedAt={}),
    externalOrganisationIds=[],
    gtExternalOrganisationId="",
    orderBy="DESC",
    pageSize=50,
)
response = Organisation.get_organisation_list(request_data)
print(response)
