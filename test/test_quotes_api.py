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
from accounting_sh.api.quotes_api import QuotesApi


class TestQuotesApi(unittest.TestCase):
    """QuotesApi unit test stubs"""

    """
    def setUp(self) -> None:
        accounting = Accounting("fake-token")
        self.api = accounting.quotes_api

    def tearDown(self) -> None:
        pass
    """

    @requests_mock.Mocker()
    def test_add_quote(self, m) -> None:
        """Test case for add_quote

        Add a quote
        """
        path = urljoin("https://api.accounting.sh", "/quotes")
        m.request("POST", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.quotes_api.add_quote(
                {},
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_delete_quote(self, m) -> None:
        """Test case for delete_quote

        Delete a quote
        """
        path = urljoin("https://api.accounting.sh", "/quotes/{uuid}")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("DELETE", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.quotes_api.delete_quote(
                "uuid_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_get_quote(self, m) -> None:
        """Test case for get_quote

        Get a quote
        """
        path = urljoin("https://api.accounting.sh", "/quotes/{uuid}")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.quotes_api.get_quote(
                "uuid_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_get_quote_document(self, m) -> None:
        """Test case for get_quote_document

        Get a quote in PDF
        """
        path = urljoin("https://api.accounting.sh", "/quotes/{uuid}/document")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.quotes_api.get_quote_document(
                "uuid_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_list_quotes(self, m) -> None:
        """Test case for list_quotes

        List company's quotes
        """
        path = urljoin("https://api.accounting.sh", "/quotes")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.quotes_api.list_quotes(
                "fields_example",
                "page_example",
                "per_page_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_update_quote(self, m) -> None:
        """Test case for update_quote

        Update a quote
        """
        path = urljoin("https://api.accounting.sh", "/quotes/{uuid}")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("PUT", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.quotes_api.update_quote(
                "uuid_example",
                {},
            )
            is not None
        )


if __name__ == "__main__":
    unittest.main()
