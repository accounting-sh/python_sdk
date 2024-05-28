# coding: utf-8

"""
    Accounting API


    The version of the OpenAPI document: 7.3.10
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
from urllib.parse import urljoin

import requests_mock

from accounting_sh.accounting import Accounting
from accounting_sh.api.tax_api import TaxApi


class TestTaxApi(unittest.TestCase):
    """TaxApi unit test stubs"""

    """
    def setUp(self) -> None:
        accounting = Accounting("fake-token")
        self.api = accounting.tax_api

    def tearDown(self) -> None:
        pass
    """

    @requests_mock.Mocker()
    def test_get_tax_rate(self, m) -> None:
        """Test case for get_tax_rate

        Get the latest tax rate for a country
        """
        path = urljoin("https://api.accounting.sh", "/tax/{country}")
        path = path.replace("{" + "country" + "}", "country_example")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.tax_api.get_tax_rate(
                "country_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_verify_vat_id(self, m) -> None:
        """Test case for verify_vat_id

        Verify a VAT ID
        """
        path = urljoin("https://api.accounting.sh", "/vat/verify/{number}")
        path = path.replace("{" + "number" + "}", "number_example")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.tax_api.verify_vat_id(
                "number_example",
            )
            is not None
        )


if __name__ == "__main__":
    unittest.main()
