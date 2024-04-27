from ozon_ord.client import OzonORDClient
from ozon_ord.platform import Platform
from ozon_ord.models import (
    PlatformData,
    BatchPlatformRequest,
    PlatformRequest,
    PlatformListRequest,
    PlatformCursor,
    UpdatedAt,
)


OzonORDClient.set_environment(environment="TEST")


# Регистрация или обновление данных площадки
platform_data = PlatformData(
    appName="Example App-88",
    externalPlatformId="example_id_88",
    platformType="PLATFORM_TYPE_SITE",
    url="http://example.com/download-88",
    comment="Example comment for testing1",
)

response = Platform.register_or_update_platform(platform_data)
print(response)

# Регистрация или обновление данных для нескольких площадок
platforms_data = BatchPlatformRequest(
    platforms=[
        PlatformRequest(
            appName="Example App One",
            externalPlatformId="example_id_12",
            platformType="PLATFORM_TYPE_SITE",
            url="http://example.com/app_one",
            comment="Example comment for app one",
        ),
        PlatformRequest(
            appName="Example App Two",
            externalPlatformId="example_id_13",
            platformType="PLATFORM_TYPE_SITE",
            url="http://example.com/app_two",
            comment="Example comment for app two",
        ),
        PlatformRequest(
            appName="Example App 34",
            externalPlatformId="example_id_34",
            platformType="PLATFORM_TYPE_SITE",
            url="http://example.com/app_one",
            comment="Example comment for app one",
        ),
    ]
)

response = Platform.register_or_update_multiple_platforms(platforms_data)
print(response)


# Информация о площадке
externalPlatformId = "bc0a64fe-34b8-445b-bcf4-c7d457090a41"
response = Platform.get_platform_info(externalPlatformId)
print(response)


# Список площадок
request_data = PlatformListRequest(
    cursor=PlatformCursor(
        externalId="",
        updatedAt={},
    ),
    orderBy="ASC",
    pageSize=0,
)

response = Platform.get_platform_list(request_data)
print(response)
