import unittest
import json
from unittest.mock import patch
from ozon_ord.contract import Contract
from ozon_ord.models import (
    ContractData,
    ContractResponse,
    ContractDetails,
    ContractsListRequest,
    ExternalCursorContract,
    ContractsListResponse,
)


class TestContract(unittest.TestCase):
    @patch("ozon_ord.contract.Contract.request")
    def test_register_or_update_contract(self, mock_request):
        mock_response_json = """
        {
          "contract": {
            "actionType": "ACTION_TYPE_CONCLUSION",
            "additionalContractNumber": "123",
            "additionalContractNumberDate": "2021-01-01",
            "agentActingForPublisher": true,
            "contractDate": "2024-01-01",
            "contractId": "123456789",
            "contractNumber": "343111",
            "contractType": "CONTRACT_TYPE_SERVICE",
            "createdAt": "2024-01-01T00:00:00Z",
            "createdBy": {"email": "example@example.com", "id": "1", "name": "John Doe"},
            "editedAt": "2024-01-02T00:00:00Z",
            "editedBy": {"email": "example@example.com", "id": "1", "name": "John Doe"},
            "externalContractId": "doc-123456789",
            "externalOrganisationCustomerId": "12345",
            "externalOrganisationPerformerId": "4888933",
            "externalParentId": "parent123",
            "isCreativeReporter": true,
            "price": "5000",
            "subjectType": "SUBJECT_TYPE_DISTRIBUTION",
            "updatedAt": "2024-01-01T00:00:00Z",
            "withNds": true,
            "comment": "No comments"
          },
          "error": null
        }
        """
        mock_request.return_value = mock_response_json
        contract_data = ContractData(
            actionType="ACTION_TYPE_CONCLUSION",
            contractDate="2024-01-01",
            contractType="CONTRACT_TYPE_SERVICE",
            externalContractId="doc-123456789",
            externalOrganisationCustomerId="12345",
            externalOrganisationPerformerId="4888933",
            subjectType="SUBJECT_TYPE_DISTRIBUTION",
            withNds=True,
        )
        response = Contract.register_or_update_contract(contract_data)
        self.assertIsInstance(response, ContractResponse)
        self.assertEqual(response.contract.contractId, "123456789")
        self.assertEqual(response.error, None)
        mock_request.assert_called_once()

    @patch("ozon_ord.contract.Contract.request")
    def test_get_contract_info(self, mock_request):
        mock_response = json.dumps(
            {
                "contract": {
                    "actionType": "ACTION_TYPE_CONCLUSION",
                    "additionalContractNumber": "123",
                    "additionalContractNumberDate": "2021-01-01",
                    "agentActingForPublisher": True,
                    "contractDate": "2024-01-01",
                    "contractId": "doc-123456789",
                    "contractNumber": "343111",
                    "contractType": "CONTRACT_TYPE_SERVICE",
                    "createdAt": "2024-01-01T00:00:00Z",
                    "createdBy": {
                        "email": "example@example.com",
                        "id": "1",
                        "name": "John Doe",
                    },
                    "editedAt": "2024-01-02T00:00:00Z",
                    "editedBy": {
                        "email": "example@example.com",
                        "id": "2",
                        "name": "Jane Doe",
                    },
                    "externalContractId": "doc-123456789",
                    "externalOrganisationCustomerId": "12345",
                    "externalOrganisationPerformerId": "4888933",
                    "externalParentId": "parent123",
                    "isCreativeReporter": True,
                    "price": "5000",
                    "subjectType": "SUBJECT_TYPE_DISTRIBUTION",
                    "updatedAt": "2024-01-02T00:00:00Z",
                    "withNds": True,
                    "comment": "No comments",
                },
                "error": None,
            }
        )
        mock_request.return_value = mock_response
        response = Contract.get_contract_info("doc-123456789")
        self.assertIsInstance(response, ContractResponse)
        self.assertIsInstance(response.contract, ContractDetails)
        self.assertEqual(response.contract.contractId, "doc-123456789")
        self.assertIsNone(response.error)
        mock_request.assert_called_once_with(
            "GET", "/api/external/contract/doc-123456789"
        )

    @patch("ozon_ord.contract.Contract.request")
    def test_get_contracts_list(self, mock_request):
        mock_response = """
        {
            "contract": [
                {
                    "contractId": "doc-123456789",
                    "actionType": "ACTION_TYPE_CONCLUSION",
                    "contractDate": "2024-01-01",
                    "contractType": "CONTRACT_TYPE_SERVICE",
                    "externalContractId": "doc-123456789",
                    "externalOrganisationCustomerId": "12345",
                    "externalOrganisationPerformerId": "4888933",
                    "subjectType": "SUBJECT_TYPE_DISTRIBUTION",
                    "withNds": true,
                    "contractNumber": "123",
                    "additionalContractNumber": null,
                    "additionalContractNumberDate": null,
                    "agentActingForPublisher": false,
                    "createdAt": "2024-01-02T14:15:22Z",
                    "createdBy": null,
                    "editedAt": "2024-01-03T14:15:22Z",
                    "editedBy": null,
                    "externalParentId": null,
                    "isCreativeReporter": false,
                    "price": "1000",
                    "updatedAt": "2024-01-04T14:15:22Z",
                    "comment": "Test contract"
                }
            ],
            "error": null
        }
        """
        mock_request.return_value = mock_response
        request_data = ContractsListRequest(
            cursor=ExternalCursorContract(externalId="", updatedAt={}),
            externalContractIds=[],
            gtExternalContractId="",
            orderBy="ASC",
            pageSize=50,
        )
        response = Contract.get_contracts_list(request_data)
        self.assertIsInstance(response, ContractsListResponse)
        self.assertIsNone(response.error)
        self.assertEqual(len(response.contract), 1)
        self.assertIsInstance(response.contract[0], ContractDetails)
        self.assertEqual(response.contract[0].contractId, "doc-123456789")
        mock_request.assert_called_once_with(
            "POST",
            "/api/ord-api/api/external/contract/list",
            data=request_data.model_dump(),
        )


if __name__ == "__main__":
    unittest.main()
