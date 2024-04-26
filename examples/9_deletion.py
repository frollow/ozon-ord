from ozon_ord.deletion import Deletion
from ozon_ord.models import DeleteOperationRequest, DeleteItemRequest

# Создать запрос на удаление
delete_request = DeleteOperationRequest(
    item=DeleteItemRequest(
        externalObjectId="stat789", objectType="DELETE_OPERATION_OBJECT_TYPE_STATISTIC"
    )
)

response = Deletion.create_delete_operation(delete_request)
print(response)


# Получить количество вложенных объектов (статистики)
request_item = DeleteOperationRequest(
    item=DeleteItemRequest(
        externalObjectId="stat789",
        objectType="DELETE_OPERATION_OBJECT_TYPE_STATISTIC",
    )
)

response = Deletion.get_entity_count(request_item)
print(response)

# Получить количество вложенных объектов (договора)
request_item = DeleteOperationRequest(
    item=DeleteItemRequest(
        externalObjectId="doc-123456789",
        objectType="DELETE_OPERATION_OBJECT_TYPE_CONTRACT",
    )
)

response = Deletion.get_entity_count(request_item)
print(response)

# Список связанных сущностей
request_data = DeleteItemRequest(
    externalObjectId="doc-123456789", objectType="DELETE_OPERATION_OBJECT_TYPE_CONTRACT"
)

response = Deletion.get_related_entities(request_data)
print(response)
