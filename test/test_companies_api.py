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
from accounting_sh.api.companies_api import CompaniesApi


class TestCompaniesApi(unittest.TestCase):
    """CompaniesApi unit test stubs"""

    """
    def setUp(self) -> None:
        accounting = Accounting("fake-token")
        self.api = accounting.companies_api

    def tearDown(self) -> None:
        pass
    """

    @requests_mock.Mocker()
    def test_add_company(self, m) -> None:
        """Test case for add_company

        Add a company
        """
        path = urljoin("https://api.accounting.sh", "/companies")
        m.request("POST", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.companies_api.add_company(
                {},
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_delete_company(self, m) -> None:
        """Test case for delete_company

        Delete a company
        """
        path = urljoin("https://api.accounting.sh", "/companies/{uuid}")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("DELETE", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.companies_api.delete_company(
                "uuid_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_get_company(self, m) -> None:
        """Test case for get_company

        Get a company
        """
        path = urljoin("https://api.accounting.sh", "/companies/{uuid}")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.companies_api.get_company(
                "uuid_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_get_company_customization(self, m) -> None:
        """Test case for get_company_customization

        Get a company's customization parameters
        """
        path = urljoin("https://api.accounting.sh", "/companies/{uuid}/customization")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.companies_api.get_company_customization(
                "uuid_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_get_company_feature_set(self, m) -> None:
        """Test case for get_company_feature_set

        List a company's feature set
        """
        path = urljoin("https://api.accounting.sh", "/companies/{uuid}/features")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.companies_api.get_company_feature_set(
                "uuid_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_list_companies(self, m) -> None:
        """Test case for list_companies

        List companies on this instance
        """
        path = urljoin("https://api.accounting.sh", "/companies")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.companies_api.list_companies(
                "fields_example",
                "page_example",
                "per_page_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_update_company(self, m) -> None:
        """Test case for update_company

        Update a company
        """
        path = urljoin("https://api.accounting.sh", "/companies/{uuid}")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("PUT", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.companies_api.update_company(
                "uuid_example",
                {},
            )
            is not None
        )


if __name__ == "__main__":
    unittest.main()
