# coding: utf-8

"""
Accounting API


The version of the OpenAPI document: 7.5.11
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


import unittest
from urllib.parse import urljoin

import requests_mock

from accounting_sh.accounting import Accounting
from accounting_sh.api.export_api import ExportApi


class TestExportApi(unittest.TestCase):
    """ExportApi unit test stubs"""

    """
    def setUp(self) -> None:
        accounting = Accounting("fake-token")
        self.api = accounting.export_api

    def tearDown(self) -> None:
        pass
    """

    @requests_mock.Mocker()
    def test_list_exports(self, m) -> None:
        """Test case for list_exports

        List company's exports
        """
        path = urljoin("https://api.accounting.sh", "/export")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.export_api.list_exports(
                "fields_example",
                "page_example",
                "per_page_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_request_export(self, m) -> None:
        """Test case for request_export

        Request an export
        """
        path = urljoin("https://api.accounting.sh", "/export")
        m.request("POST", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.export_api.request_export(
                {},
            )
            is not None
        )


if __name__ == "__main__":
    unittest.main()
