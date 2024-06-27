# coding: utf-8

"""
    Accounting API


    The version of the OpenAPI document: 7.3.11
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
from urllib.parse import urljoin

import requests_mock

from accounting_sh.accounting import Accounting
from accounting_sh.api.currency_api import CurrencyApi


class TestCurrencyApi(unittest.TestCase):
    """CurrencyApi unit test stubs"""

    """
    def setUp(self) -> None:
        accounting = Accounting("fake-token")
        self.api = accounting.currency_api

    def tearDown(self) -> None:
        pass
    """

    @requests_mock.Mocker()
    def test_get_exchange_rate(self, m) -> None:
        """Test case for get_exchange_rate

        Get the latest currency exchange rate
        """
        path = urljoin("https://api.accounting.sh", "/currency/{from}/{to}")
        path = path.replace("{" + "from" + "}", "var_from_example")
        path = path.replace("{" + "to" + "}", "to_example")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.currency_api.get_exchange_rate(
                "var_from_example",
                "to_example",
            )
            is not None
        )


if __name__ == "__main__":
    unittest.main()
