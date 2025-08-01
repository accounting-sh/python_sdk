# coding: utf-8

"""
Accounting API


The version of the OpenAPI document: 8.3.3
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


import unittest
from urllib.parse import urljoin

import requests_mock

from accounting_sh.accounting import Accounting
from accounting_sh.api.search_api import SearchApi


class TestSearchApi(unittest.TestCase):
    """SearchApi unit test stubs"""

    """
    def setUp(self) -> None:
        accounting = Accounting("fake-token")
        self.api = accounting.search_api

    def tearDown(self) -> None:
        pass
    """

    @requests_mock.Mocker()
    def test_search(self, m) -> None:
        """Test case for search

        Search
        """
        path = urljoin("https://api.accounting.sh", "/search")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.search_api.search(
                "q_example",
                "exclude_example",
                "only_example",
            )
            is not None
        )


if __name__ == "__main__":
    unittest.main()
