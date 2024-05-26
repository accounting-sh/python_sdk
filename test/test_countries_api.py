# coding: utf-8

"""
    Accounting API


    The version of the OpenAPI document: VERSION_HERE
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
from urllib.parse import urljoin

import requests_mock

from accounting_sh.accounting import Accounting
from accounting_sh.api.countries_api import CountriesApi


class TestCountriesApi(unittest.TestCase):
    """CountriesApi unit test stubs"""

    """
    def setUp(self) -> None:
        accounting = Accounting("fake-token")
        self.api = accounting.countries_api

    def tearDown(self) -> None:
        pass
    """

    @requests_mock.Mocker()
    def test_get_translated_countries(self, m) -> None:
        """Test case for get_translated_countries

        Get translated list of countries
        """
        path = urljoin("https://api.accounting.sh", "/countries/{lang}")
        path = path.replace("{" + "lang" + "}", "lang_example")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.countries_api.get_translated_countries(
                "lang_example",
            )
            is not None
        )


if __name__ == "__main__":
    unittest.main()