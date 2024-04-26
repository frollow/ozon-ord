import unittest
from unittest.mock import patch, Mock
from ozon_ord.dictionary import Dictionary
from ozon_ord.models import (
    BankDictionaryRequest,
    CountryDictionaryRequest,
    FiasDictionaryRequest,
    FiasInfo,
    OkvedDictionaryRequest,
)


class TestDictionary(unittest.TestCase):
    @patch("ozon_ord.dictionary.Dictionary.request")
    def test_get_bank_info(self, mock_request):
        mock_response = Mock()
        mock_response.json.return_value = [
            {
                "address": "Some Address",
                "bik": "044525999",
                "correspondent_account": "30101810400000000225",
                "country": "RU",
                "name": "Bank Name",
            }
        ]
        mock_request.return_value = mock_response
        request_data = BankDictionaryRequest(search="044525999", pageSize=1)
        response = Dictionary.get_bank_info(request_data)
        self.assertEqual(response[0].bik, "044525999")
        self.assertEqual(response[0].name, "Bank Name")
        self.assertEqual(response[0].address, "Some Address")
        self.assertEqual(response[0].country, "RU")

    @patch("ozon_ord.dictionary.Dictionary.request")
    def test_get_country_info(self, mock_request):
        mock_response = Mock()
        mock_response.json.return_value = [
            {
                "country": "Russia",
                "oksmNumber": "643",
                "shortName": "RU",
            },
            {
                "country": "United States",
                "oksmNumber": "840",
                "shortName": "US",
            },
        ]
        mock_request.return_value = mock_response
        request_data = CountryDictionaryRequest(search="RU")
        response = Dictionary.get_country_info(request_data)
        self.assertEqual(len(response), 2)
        self.assertEqual(response[0].country, "Russia")
        self.assertEqual(response[0].oksmNumber, "643")
        self.assertEqual(response[0].shortName, "RU")
        self.assertEqual(response[1].country, "United States")
        self.assertEqual(response[1].oksmNumber, "840")
        self.assertEqual(response[1].shortName, "US")

    @patch("ozon_ord.dictionary.Dictionary.request")
    def test_get_fias_info(self, mock_request):
        mock_response = Mock()
        mock_response.json.return_value = [
            {
                "guid": "1f1f96b3-f3f4-462c-92f9-62ec62f84100",
                "id": "100",
                "level": "2",
                "name": "Some District",
                "parentId": "1",
                "path": "Region > District",
                "type": "district",
            }
        ]
        mock_request.return_value = mock_response
        request_data = FiasDictionaryRequest(search="Some District", pageSize=1)
        response = Dictionary.get_fias_info(request_data)
        self.assertEqual(len(response), 1)
        self.assertIsInstance(response[0], FiasInfo)
        self.assertEqual(response[0].id, "100")
        self.assertEqual(response[0].name, "Some District")
        self.assertEqual(response[0].path, "Region > District")
        self.assertEqual(response[0].level, "2")
        self.assertEqual(response[0].parentId, "1")
        self.assertEqual(response[0].type, "district")

    @patch("ozon_ord.dictionary.Dictionary.request")
    def test_get_okved_info(self, mock_request):
        # Setup the mock response object
        mock_response = Mock()
        mock_response.json.return_value = [
            {"code": "98.10", "name": "Pet Care Services"},
            {"code": "62.01", "name": "Computer Programming Services"},
        ]
        mock_request.return_value = mock_response

        # Instantiate a request object with test parameters
        request_data = OkvedDictionaryRequest(search="98.10")

        # Call the method under test
        response = Dictionary.get_okved_info(request_data)

        # Assertions to verify the behavior of the method
        self.assertIsInstance(response, list)
        self.assertEqual(len(response), 2)
        self.assertEqual(response[0].code, "98.10")
        self.assertEqual(response[0].name, "Pet Care Services")
        self.assertEqual(response[1].code, "62.01")
        self.assertEqual(response[1].name, "Computer Programming Services")


if __name__ == "__main__":
    unittest.main()
