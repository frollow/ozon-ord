import unittest
import json
from unittest.mock import patch
from ozon_ord.invoice import Invoice
from ozon_ord.models import (
    InvoiceRequestData,
    ExternalContract,
    InvoiceResponse,
    InvoiceFilter,
    InvoiceCursor,
)


class TestInvoice(unittest.TestCase):
    @patch("ozon_ord.invoice.Invoice.request")
    def test_register_or_update_invoice(self, mock_request):
        invoice_data = InvoiceRequestData(
            clientRole="ORGANISATION_ROLE_RD",
            contractorRole="ORGANISATION_ROLE_RR",
            contracts=[
                ExternalContract(
                    externalContractId="doc-123456789", price="7000", withNds=True
                )
            ],
            endDate="2024-04-24",
            externalContractId="doc-123456789",
            externalInvoiceId="33399",
            invoiceDate="2024-04-21",
            invoiceNumber="n-rr-11",
            price="7000",
            startDate="2024-04-22",
            withNds=True,
        )
        mock_response = json.dumps(
            {
                "invoice": {
                    "invoiceId": "33399",
                    "invoiceNumber": "n-rr-11",
                    "invoiceDate": "2024-04-21",
                    "startDate": "2024-04-22",
                    "endDate": "2024-04-24",
                    "price": "7000",
                    "withNds": True,
                    "externalInvoiceId": "33399",
                    "externalContractId": "doc-123456789",
                    "clientRole": "ORGANISATION_ROLE_RD",
                    "contractorRole": "ORGANISATION_ROLE_RR",
                    "contracts": [
                        {
                            "externalContractId": "doc-123456789",
                            "price": "7000",
                            "withNds": True,
                        }
                    ],
                }
            }
        )
        mock_request.return_value = mock_response
        response = Invoice.register_or_update_invoice(invoice_data)
        mock_request.assert_called_once_with(
            "POST", "/api/external/v2/invoice", data=invoice_data.model_dump()
        )
        self.assertEqual(response.invoice.invoiceId, "33399")

    @patch("ozon_ord.invoice.Invoice.request")
    def test_get_invoice_info(self, mock_request):
        mock_response = {
            "invoice": {
                "invoiceId": "33399",
                "clientRole": "ORGANISATION_ROLE_RD",
                "contractorRole": "ORGANISATION_ROLE_RR",
                "invoiceDate": "2024-04-21",
                "invoiceNumber": "n-rr-11",
                "startDate": "2024-04-22",
                "endDate": "2024-04-24",
                "price": "7000",
                "withNds": True,
                "externalContractId": "doc-123456789",
                "externalInvoiceId": "33399",
                "contracts": [
                    {
                        "externalContractId": "doc-123456789",
                        "price": "7000",
                        "withNds": True,
                        "contractId": "123",
                    }
                ],
                "createdAt": "2024-04-22T06:04:44.692124Z",
                "createdBy": None,
                "editedAt": "2024-04-22T06:08:58.711137Z",
                "editedBy": None,
            }
        }
        json_response = json.dumps(mock_response)
        mock_request.return_value = json_response
        response = Invoice.get_invoice_info("33399")
        mock_request.assert_called_once_with("GET", "/api/external/v2/invoice/33399")
        self.assertIsInstance(response, InvoiceResponse)
        self.assertEqual(response.invoice.invoiceId, "33399")
        self.assertEqual(response.invoice.clientRole, "ORGANISATION_ROLE_RD")

    @patch("ozon_ord.invoice.Invoice.request")
    def test_get_invoice_list(self, mock_request):
        filter_data = InvoiceFilter(
            cursor=InvoiceCursor(externalId="last_seen_id"), orderBy="ASC", pageSize=10
        )
        mock_response_json = json.dumps(
            {
                "invoice": [
                    {
                        "invoiceId": "33399",
                        "clientRole": "ORGANISATION_ROLE_RD",
                        "contractorRole": "ORGANISATION_ROLE_RR",
                        "contracts": [
                            {
                                "externalContractId": "doc-123456789",
                                "price": "7000",
                                "withNds": True,
                            }
                        ],
                        "endDate": "2024-04-24",
                        "externalContractId": "doc-123456789",
                        "externalInvoiceId": "33399",
                        "invoiceDate": "2024-04-21",
                        "invoiceNumber": "n-rr-11",
                        "price": "7000",
                        "startDate": "2024-04-22",
                        "withNds": True,
                        "createdAt": "2024-04-22T06:04:44.692124Z",
                        "editedAt": "2024-04-22T06:08:58.711137Z",
                        "createdBy": None,
                        "editedBy": None,
                        "violation": ["None"],
                        "comment": "",
                    }
                ]
            }
        )
        mock_request.return_value = mock_response_json
        response = Invoice.get_invoice_list(filter_data)
        mock_request.assert_called_once_with(
            "POST", "/api/external/v2/invoice/list", data=filter_data.model_dump()
        )
        self.assertEqual(len(response.invoice), 1)
        self.assertEqual(response.invoice[0].invoiceId, "33399")


if __name__ == "__main__":
    unittest.main()
