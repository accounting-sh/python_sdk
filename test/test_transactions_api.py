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
from accounting_sh.api.transactions_api import TransactionsApi


class TestTransactionsApi(unittest.TestCase):
    """TransactionsApi unit test stubs"""

    """
    def setUp(self) -> None:
        accounting = Accounting("fake-token")
        self.api = accounting.transactions_api

    def tearDown(self) -> None:
        pass
    """

    @requests_mock.Mocker()
    def test_add_link(self, m) -> None:
        """Test case for add_link

        Add a new transaction link
        """
        path = urljoin("https://api.accounting.sh", "/transactions/{uuid}/links")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("POST", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.transactions_api.add_link(
                {},
                "uuid_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_add_transaction(self, m) -> None:
        """Test case for add_transaction

        Add a transaction
        """
        path = urljoin("https://api.accounting.sh", "/transactions")
        m.request("POST", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.transactions_api.add_transaction(
                {},
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_add_transaction_code(self, m) -> None:
        """Test case for add_transaction_code

        Add a transaction's code
        """
        path = urljoin("https://api.accounting.sh", "/transactions/{uuid}/codes")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("POST", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.transactions_api.add_transaction_code(
                "uuid_example",
                {},
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_delete_link(self, m) -> None:
        """Test case for delete_link

        Delete a transaction link
        """
        path = urljoin(
            "https://api.accounting.sh", "/transactions/{uuid}/links/{link_uuid}"
        )
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        path = path.replace("{" + "link_uuid" + "}", "link_uuid_example")
        m.request("DELETE", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.transactions_api.delete_link(
                "uuid_example",
                "link_uuid_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_delete_transaction(self, m) -> None:
        """Test case for delete_transaction

        Delete a transaction
        """
        path = urljoin("https://api.accounting.sh", "/transactions/{uuid}")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("DELETE", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.transactions_api.delete_transaction(
                "uuid_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_delete_transaction_code(self, m) -> None:
        """Test case for delete_transaction_code

        Delete a transaction's code
        """
        path = urljoin("https://api.accounting.sh", "/transactions/{uuid}/codes/{code}")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        path = path.replace("{" + "code" + "}", "code_example")
        m.request("DELETE", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.transactions_api.delete_transaction_code(
                "uuid_example",
                "code_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_get_transaction(self, m) -> None:
        """Test case for get_transaction

        Get a transaction
        """
        path = urljoin("https://api.accounting.sh", "/transactions/{uuid}")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.transactions_api.get_transaction(
                "uuid_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_import_transactions(self, m) -> None:
        """Test case for import_transactions

        Import transactions - INTERNAL
        """
        path = urljoin("https://api.accounting.sh", "/transactions/import")
        m.request("POST", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.transactions_api.import_transactions(
                {},
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_ledger(self, m) -> None:
        """Test case for ledger

        List company's transactions and transfers
        """
        path = urljoin("https://api.accounting.sh", "/transactions/ledger")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.transactions_api.ledger(
                "fields_example",
                "page_example",
                "per_page_example",
                "account_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_list_links(self, m) -> None:
        """Test case for list_links

        List a transaction links
        """
        path = urljoin("https://api.accounting.sh", "/transactions/{uuid}/links")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.transactions_api.list_links(
                "fields_example",
                "page_example",
                "per_page_example",
                "uuid_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_list_transaction_codes(self, m) -> None:
        """Test case for list_transaction_codes

        List transaction's codes
        """
        path = urljoin("https://api.accounting.sh", "/transactions/{uuid}/codes")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.transactions_api.list_transaction_codes(
                "uuid_example",
                "fields_example",
                "page_example",
                "per_page_example",
                "account_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_list_transactions(self, m) -> None:
        """Test case for list_transactions

        List company's transactions
        """
        path = urljoin("https://api.accounting.sh", "/transactions")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.transactions_api.list_transactions(
                "fields_example",
                "page_example",
                "per_page_example",
                "account_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_update_link(self, m) -> None:
        """Test case for update_link

        Update a transaction link
        """
        path = urljoin(
            "https://api.accounting.sh", "/transactions/{uuid}/links/{link_uuid}"
        )
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        path = path.replace("{" + "link_uuid" + "}", "link_uuid_example")
        m.request("PUT", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.transactions_api.update_link(
                {},
                "uuid_example",
                "link_uuid_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_update_transaction(self, m) -> None:
        """Test case for update_transaction

        Update a transaction
        """
        path = urljoin("https://api.accounting.sh", "/transactions/{uuid}")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("PUT", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.transactions_api.update_transaction(
                "uuid_example",
                {},
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_update_transaction_code(self, m) -> None:
        """Test case for update_transaction_code

        Update a transaction's code
        """
        path = urljoin("https://api.accounting.sh", "/transactions/{uuid}/codes")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("PUT", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.transactions_api.update_transaction_code(
                "uuid_example",
                {},
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_view_link(self, m) -> None:
        """Test case for view_link

        View a transaction link
        """
        path = urljoin(
            "https://api.accounting.sh", "/transactions/{uuid}/links/{link_uuid}"
        )
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        path = path.replace("{" + "link_uuid" + "}", "link_uuid_example")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.transactions_api.view_link(
                "uuid_example",
                "link_uuid_example",
            )
            is not None
        )


if __name__ == "__main__":
    unittest.main()
