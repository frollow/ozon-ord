from ozon_ord.notification import Notification
from ozon_ord.models import NotificationQueryParams

# Ошибки валидации
query_params = NotificationQueryParams(pageSize=20, gtNotificationId="0")

response = Notification.get_error_list(query_params)
print(response)
