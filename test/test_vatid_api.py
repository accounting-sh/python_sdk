# coding: utf-8

"""
    Accounting API


    The version of the OpenAPI document: 7.5.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
from urllib.parse import urljoin

import requests_mock

from accounting_sh.accounting import Accounting
from accounting_sh.api.vatid_api import VATIDApi


class TestVATIDApi(unittest.TestCase):
    """VATIDApi unit test stubs"""

    """
    def setUp(self) -> None:
        accounting = Accounting("fake-token")
        self.api = accounting.vatid_api

    def tearDown(self) -> None:
        pass
    """

    @requests_mock.Mocker()
    def test_add_company_vat_id(self, m) -> None:
        """Test case for add_company_vat_id

        Add a company's Vat Id
        """
        path = urljoin("https://api.accounting.sh", "/companies/{uuid}/vat")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("POST", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.vatid_api.add_company_vat_id(
                {},
                "uuid_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_delete_company_vat_id(self, m) -> None:
        """Test case for delete_company_vat_id

        Delete a company's Vat Id
        """
        path = urljoin("https://api.accounting.sh", "/companies/{uuid}/vat/{key}")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        path = path.replace("{" + "key" + "}", "key_example")
        m.request("DELETE", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.vatid_api.delete_company_vat_id(
                "key_example",
                "uuid_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_get_company_vat_id(self, m) -> None:
        """Test case for get_company_vat_id

        Get a company's Vat Id
        """
        path = urljoin("https://api.accounting.sh", "/companies/{uuid}/vat/{key}")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        path = path.replace("{" + "key" + "}", "key_example")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.vatid_api.get_company_vat_id(
                "key_example",
                "uuid_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_list_company_vat_id(self, m) -> None:
        """Test case for list_company_vat_id

        List company's Vat Id
        """
        path = urljoin("https://api.accounting.sh", "/companies/{uuid}/vat")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.vatid_api.list_company_vat_id(
                "fields_example",
                "page_example",
                "per_page_example",
                "uuid_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_update_company_vat_id(self, m) -> None:
        """Test case for update_company_vat_id

        Update a company's Vat Id
        """
        path = urljoin("https://api.accounting.sh", "/companies/{uuid}/vat/{key}")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        path = path.replace("{" + "key" + "}", "key_example")
        m.request("PUT", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.vatid_api.update_company_vat_id(
                "key_example",
                {},
                "uuid_example",
            )
            is not None
        )


if __name__ == "__main__":
    unittest.main()
