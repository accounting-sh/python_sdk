# coding: utf-8

"""
    Accounting API


    The version of the OpenAPI document: 7.5.10
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
from urllib.parse import urljoin

import requests_mock

from accounting_sh.accounting import Accounting
from accounting_sh.api.rossum_api import RossumApi


class TestRossumApi(unittest.TestCase):
    """RossumApi unit test stubs"""

    """
    def setUp(self) -> None:
        accounting = Accounting("fake-token")
        self.api = accounting.rossum_api

    def tearDown(self) -> None:
        pass
    """

    @requests_mock.Mocker()
    def test_list_reviews(self, m) -> None:
        """Test case for list_reviews

        List documents to be reviewes
        """
        path = urljoin("https://api.accounting.sh", "/external/rossum/reviews")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.rossum_api.list_reviews(
                "fields_example",
                "page_example",
                "per_page_example",
            )
            is not None
        )


if __name__ == "__main__":
    unittest.main()
