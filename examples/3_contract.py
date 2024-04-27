from ozon_ord.client import OzonORDClient
from ozon_ord.contract import Contract
from ozon_ord.models import (
    ContractData,
    ContractsListRequest,
    ExternalCursorContract,
)

OzonORDClient.set_environment(environment="TEST")

# Регистрация или обновление данных договора
contract_data = ContractData(
    actionType="ACTION_TYPE_CONCLUSION",
    contractNumber="343111",
    contractDate="2024-01-01",
    contractType="CONTRACT_TYPE_SERVICE",
    externalContractId="doc-123456789",
    externalOrganisationCustomerId="12345",
    externalOrganisationPerformerId="4888933",
    subjectType="SUBJECT_TYPE_DISTRIBUTION",
    price="5000",
    withNds=True,
)
response = Contract.register_or_update_contract(contract_data)
print(response)

# Информация о договоре
externalContractId = "doc-123456789"
response = Contract.get_contract_info(externalContractId)
print(response)


# Список договоров
request_data = ContractsListRequest(
    cursor=ExternalCursorContract(externalId="", updatedAt={}),
    externalContractIds=[],
    gtExternalContractId="",
    orderBy="ASC",
    pageSize=50,
)

response = Contract.get_contracts_list(request_data)
print(response)
