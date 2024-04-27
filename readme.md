# Ozon ОРД API - Python

Клиент для взаимодействия с системой управления рекламными данными Ozon ОРД через API.

**Что представляет собой Ozon ОРД API**
Ozon ОРД API — это программный интерфейс, предназначенный для передачи данных между системой поставщика данных и Ozon.

Используя функции Ozon ОРД API, можно осуществлять регистрацию, обновление и получение информации о договорах, креативах, документах, контрагентах и рекламных площадках.

## Установка

### C помощью pip

1. Установите pip
2. Выполните команду

```
pip install ozon-ord
```

## Начало работы

1. Установите данные для конфигурации

**Для тестового окружения (если используете [Ozon ОРД Sandbox](https://ord-sandbox.ozon.ru)):**

```
from ozon_ord import Config, OzonORDClient

_environment="TEST"
OzonORDClient.set_environment(environment=_environment)
Config.set_api_key(key="api_key", environment=_environment)
```

Замените api_key на значение полученное в профиле пользователя [Ozon ОРД Sandbox](https://ord-sandbox.ozon.ru/profile/api).

**Для продового окружения:**

```
from ozon_ord import Config, OzonORDClient

Config.set_api_key(key="api_key")
```

Достаточно указать только значение api_key. Скопируйте из профиля пользователя [Ozon ОРД](https://ord.ozon.ru/profile/api).

2. Вызовите необходимый метод API. [Документация Ozon ОРД](https://docs.ozon.ru/api/ord/).

## Примеры

### Работа с платформами

```
from ozon_ord import Config, OzonORDClient

from ozon_ord.platform import Platform
from ozon_ord.models import (
    PlatformData,
    BatchPlatformRequest,
    PlatformRequest,
    PlatformListRequest,
    PlatformCursor,
    UpdatedAt,
)


_environment="TEST"
OzonORDClient.set_environment(environment=_environment)
Config.set_api_key(key="api_key", environment=_environment)


# Регистрация или обновление данных площадки
platform_data = PlatformData(
    appName="Название площадки",
    externalPlatformId="example_id_88",
    platformType="PLATFORM_TYPE_SITE",
    url="http://example.com/",
    comment="Комментарий или описание",
)

response = Platform.register_or_update_platform(platform_data)
print(response)

# Регистрация или обновление данных для нескольких площадок
platforms_data = BatchPlatformRequest(
    platforms=[
        PlatformRequest(
            appName="Название площадки 1",
            externalPlatformId="example_id_12",
            platformType="PLATFORM_TYPE_SITE",
            url="http://example.com/app_one",
            comment="Example comment for app one",
        ),
        PlatformRequest(
            appName="Название площадки 2",
            externalPlatformId="example_id_13",
            platformType="PLATFORM_TYPE_SITE",
            url="http://example.com/app_two",
            comment="Комментарий или описание 1",
        ),
        PlatformRequest(
            appName="Example App 34",
            externalPlatformId="example_id_34",
            platformType="PLATFORM_TYPE_SITE",
            url="http://example.com/app_one",
            comment="Комментарий или описание 2",
        ),
    ]
)

response = Platform.register_or_update_multiple_platforms(platforms_data)
print(response)


# Информация о площадке
externalPlatformId = "example_id_12"
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
```

### Другие примеры

Другие примеры вы найдете в папке **"examples"**.
