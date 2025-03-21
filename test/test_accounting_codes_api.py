# coding: utf-8

"""
Accounting API


The version of the OpenAPI document: 8.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


import unittest
from urllib.parse import urljoin

import requests_mock

from accounting_sh.accounting import Accounting
from accounting_sh.api.accounting_codes_api import AccountingCodesApi


class TestAccountingCodesApi(unittest.TestCase):
    """AccountingCodesApi unit test stubs"""

    """
    def setUp(self) -> None:
        accounting = Accounting("fake-token")
        self.api = accounting.accounting_codes_api

    def tearDown(self) -> None:
        pass
    """

    @requests_mock.Mocker()
    def test_add_accounting_code(self, m) -> None:
        """Test case for add_accounting_code

        Add an accounting code
        """
        path = urljoin("https://api.accounting.sh", "/accounting/codes")
        m.request("POST", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.accounting_codes_api.add_accounting_code(
                {},
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_delete_accounting_code(self, m) -> None:
        """Test case for delete_accounting_code

        Delete an accounting code
        """
        path = urljoin("https://api.accounting.sh", "/accounting/codes/{uuid}")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("DELETE", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.accounting_codes_api.delete_accounting_code(
                "uuid_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_get_accounting_code(self, m) -> None:
        """Test case for get_accounting_code

        Get an accounting code
        """
        path = urljoin("https://api.accounting.sh", "/accounting/codes/{uuid}")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.accounting_codes_api.get_accounting_code(
                "uuid_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_list_accounting_codes(self, m) -> None:
        """Test case for list_accounting_codes

        List company's accounting code
        """
        path = urljoin("https://api.accounting.sh", "/accounting/codes")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert accounting.accounting_codes_api.list_accounting_codes() is not None

    @requests_mock.Mocker()
    def test_update_accounting_code(self, m) -> None:
        """Test case for update_accounting_code

        Update an accounting code
        """
        path = urljoin("https://api.accounting.sh", "/accounting/codes/{uuid}")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("PUT", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.accounting_codes_api.update_accounting_code(
                "uuid_example",
                {},
            )
            is not None
        )


if __name__ == "__main__":
    unittest.main()
