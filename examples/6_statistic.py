from ozon_ord.statistic import Statistic
from ozon_ord.models import (
    StatisticList,
    ExternalExtStatistic,
    StatisticListRequest,
    ExternalCursorStatistic,
)

# Добавить статистику (и изменить)
statistics_data = StatisticList(
    statistics=[
        ExternalExtStatistic(
            dateEndFact="2022-01-01",
            dateEndPlan="2022-01-02",
            dateStartFact="2022-01-01",
            dateStartPlan="2022-01-02",
            externalCreativeId="creative-id-121",
            externalPlatformId="example_id_88",
            externalStatisticId="stat78933",
            moneySpent="100",
            unitCost="10",
            viewsCountByFact="1000",
            viewsCountByInvoice="950",
            withNds=True,
            comment="Initial load",
        )
    ]
)

response = Statistic.add_statistics(statistics_data)
print(response)


# Список статистик
request_data = StatisticListRequest(
    cursor=ExternalCursorStatistic(externalId="", updatedAt={}),
    # externalContractIds=["contract1", "contract2"],
    orderBy="ASC",
    pageSize=20,
)

response = Statistic.get_statistic_list(request_data)
print(response)


# Информация о статистике
externalStatisticId = "stat78933"
response = Statistic.get_statistic_info(externalStatisticId)
print(response)
