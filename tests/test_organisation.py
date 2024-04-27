import unittest
import json
from unittest.mock import patch
from ozon_ord.organisation import Organisation
from ozon_ord.models import (
    OrganisationData,
    OrganisationResponse,
    AddOrganisationPlatformRequest,
    OrganisationListRequest,
    OrganisationListResponse,
    Address,
    LegalType,
    ExternalOrganisationPlatform,
)


class TestOzonORDClient(unittest.TestCase):
    @patch("ozon_ord.organisation.Organisation.request")
    def test_register_or_update_organisation(self, mock_request):
        mock_request.return_value = json.dumps(
            {
                "organisation": {
                    "externalOrganisationId": "12345",
                    "fullOpf": "ООО 'Ромашка'",
                    "inn": "8806046968",
                    "isOpc": False,
                    "isPp": False,
                    "legalAddress": {
                        "address": "123456, Москва, ул. Пушкина, д. Колотушкина",
                        "locality": "Москва",
                        "postcode": "123456",
                    },
                    "legalType": "LEGAL_TYPE_LEGAL",
                    "postAddress": {
                        "address": "654321, Москва, ул. Солнечная, д. 1",
                        "locality": "Москва",
                        "postcode": "654321",
                    },
                },
                "error": None,
            }
        )
        organisation_data = OrganisationData(
            externalOrganisationId="12345",
            fullOpf="ООО 'Ромашка'",
            inn="8806046968",
            isOpc=False,
            isPp=False,
            legalAddress=Address(
                address="123456, Москва, ул. Пушкина, д. Колотушкина",
                locality="Москва",
                postcode="123456",
            ),
            legalType=LegalType.LEGAL_TYPE_LEGAL,
            postAddress=Address(
                address="654321, Москва, ул. Солнечная, д. 1",
                locality="Москва",
                postcode="654321",
            ),
        )
        response = Organisation.register_or_update_organisation(organisation_data)
        self.assertIsInstance(response, OrganisationResponse)
        self.assertEqual(response.organisation.externalOrganisationId, "12345")
        self.assertIsNone(response.error)

    @patch("ozon_ord.organisation.Organisation.request")
    def test_get_organisation_info(self, mock_request):
        mock_request.return_value = """{
            "organisation": {
                "externalOrganisationId": "12345",
                "fullOpf": "ООО 'Ромашка'",
                "inn": "8806046968",
                "isOpc": false,
                "isPp": false,
                "legalAddress": {
                    "address": "123456, Москва, ул. Пушкина, д. Колотушкина",
                    "locality": "Москва",
                    "postcode": "123456"
                },
                "legalType": "LEGAL_TYPE_LEGAL",
                "postAddress": {
                    "address": "654321, Москва, ул. Солнечная, д. 1",
                    "locality": "Москва",
                    "postcode": "654321"
                }
            },
            "error": null
        }"""
        response = Organisation.get_organisation_info("12345")
        self.assertIsInstance(response, OrganisationResponse)
        self.assertEqual(response.organisation.externalOrganisationId, "12345")
        self.assertEqual(response.organisation.inn, "8806046968")
        self.assertEqual(response.organisation.legalType, "LEGAL_TYPE_LEGAL")
        self.assertIsNone(response.error)
        self.assertEqual(
            response.organisation.legalAddress.address,
            "123456, Москва, ул. Пушкина, д. Колотушкина",
        )
        self.assertEqual(
            response.organisation.postAddress.address,
            "654321, Москва, ул. Солнечная, д. 1",
        )

    @patch("ozon_ord.organisation.Organisation.request")
    def test_add_platforms_to_organisation(self, mock_request):
        mock_request.return_value = {}
        platform_data = AddOrganisationPlatformRequest(
            platform=[
                ExternalOrganisationPlatform(
                    externalPlatformId="plat123", isPlatformOwner=True
                )
            ]
        )
        externalOrganisationId = "org123"
        response = Organisation.add_platforms_to_organisation(
            externalOrganisationId, platform_data
        )
        self.assertIsInstance(response, dict)

    @patch("ozon_ord.organisation.Organisation.request")
    def test_get_organisation_list(self, mock_request):
        mock_request.return_value = '{"organisation": [], "error": null}'
        request_data = OrganisationListRequest(
            cursor={"externalId": "", "updatedAt": {}},
            externalOrganisationIds=[],
            gtExternalOrganisationId="",
            orderBy="DESC",
            pageSize=50,
        )
        response = Organisation.get_organisation_list(request_data)
        self.assertIsInstance(response, OrganisationListResponse)
        self.assertEqual(len(response.organisation), 0)


if __name__ == "__main__":
    unittest.main()
