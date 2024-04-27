from ozon_ord.client import OzonORDClient
from ozon_ord.creative import Creative
from ozon_ord.models import (
    CreativeData,
    UrlListData,
    ExternalMediaData,
    ExternalMediaFileRequest,
    CreativesListRequest,
    ExternalCursorCreative,
)

OzonORDClient.set_environment(environment="TEST")

# Регистрация или обновление данных креатива (версия 2)
# Текстовый блок, без прикрепленных файлов
creative_data = CreativeData(
    title="Заголовок для креатива",
    advObjectType="ADV_OBJECT_TYPE_TEXT_BLOCK",
    description="Описание нового креатива.",
    externalContractIds=["doc-123456789"],
    externalCreativeId="creative-id-99988898",
    geoTargets=[],
    isSocialAdv=False,
    isNative=False,
    mediaData=[ExternalMediaData(text="Текстовый контент для креатива")],
    okvedCodes=["60.10"],
    paymentType="PAYMENT_TYPE_CPM",
    urlList=[
        UrlListData(url="https://example.com/target-1"),
        UrlListData(url="https://example.com/target-2"),
    ],
)

response = Creative.register_or_update_creative(creative_data)
print(response)


# Регистрация или обновление данных креатива (версия 2)
# Баннер с файлом

creative_data = CreativeData(
    title="Заголовок для баннера с файлом",
    advObjectType="ADV_OBJECT_TYPE_BANNER",
    description="Описание нового креатива.",
    externalContractIds=["doc-123456789"],
    externalCreativeId="creative-id-121",
    geoTargets=[],
    isSocialAdv=False,
    isNative=False,
    mediaData=[
        ExternalMediaData(
            description="Описание для файла",
            file=ExternalMediaFileRequest(
                id="403553",  # Получаем id заранее, необходимо выполнить метод /api/external/file/{bucket}
            ),
        )
    ],
    okvedCodes=["60.10"],
    paymentType="PAYMENT_TYPE_CPM",
    urlList=[
        UrlListData(url="https://example.com/target-1"),
        UrlListData(url="https://example.com/target-2"),
    ],
)

response = Creative.register_or_update_creative(creative_data)
print(response)


# Регистрация или обновление данных креатива (версия 2)
# Текстово-графический блок с файлом

creative_data = CreativeData(
    title="Заголовок для текстово-графического блока с файлом",
    advObjectType="ADV_OBJECT_TYPE_TEXT_GRAPHIC_BLOCK",
    description="Описание нового креатива.",
    externalContractIds=["doc-123456789"],
    externalCreativeId="creative-id-124",
    geoTargets=[],
    isSocialAdv=False,
    isNative=False,
    mediaData=[
        ExternalMediaData(
            description="Описание для файла",
            text="Текстовая часть рекламного блока",
            file=ExternalMediaFileRequest(
                id="403591",  # Получаем id заранее, необходимо выполнить метод /api/external/file/{bucket}
            ),
        )
    ],
    okvedCodes=["60.10"],
    paymentType="PAYMENT_TYPE_CPM",
    urlList=[
        UrlListData(url="https://example.com/target-1"),
        UrlListData(url="https://example.com/target-2"),
    ],
)

response = Creative.register_or_update_creative(creative_data)
print(response)


# Информация о креативе
externalCreativeId = "creative-id-99988898"
response = Creative.get_creative_info(externalCreativeId)
print(response)


# Список креативов
request_data = CreativesListRequest(
    cursor=ExternalCursorCreative(externalId="", updatedAt={}),
    orderBy="ASC",
    pageSize=10,
)

response = Creative.get_creatives_list(request_data)
print(response)
