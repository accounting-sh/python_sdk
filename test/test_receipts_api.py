# coding: utf-8

"""
    Accounting API


    The version of the OpenAPI document: 7.5.8
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
from urllib.parse import urljoin

import requests_mock

from accounting_sh.accounting import Accounting
from accounting_sh.api.receipts_api import ReceiptsApi


class TestReceiptsApi(unittest.TestCase):
    """ReceiptsApi unit test stubs"""

    """
    def setUp(self) -> None:
        accounting = Accounting("fake-token")
        self.api = accounting.receipts_api

    def tearDown(self) -> None:
        pass
    """

    @requests_mock.Mocker()
    def test_add_receipt(self, m) -> None:
        """Test case for add_receipt

        Add a receipt
        """
        path = urljoin("https://api.accounting.sh", "/receipts")
        m.request("POST", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.receipts_api.add_receipt(
                {},
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_delete_receipt(self, m) -> None:
        """Test case for delete_receipt

        Delete a receipt
        """
        path = urljoin("https://api.accounting.sh", "/receipts/{uuid}")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("DELETE", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.receipts_api.delete_receipt(
                "uuid_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_get_receipt(self, m) -> None:
        """Test case for get_receipt

        Get a receipt
        """
        path = urljoin("https://api.accounting.sh", "/receipts/{uuid}")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.receipts_api.get_receipt(
                "uuid_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_get_receipt_document(self, m) -> None:
        """Test case for get_receipt_document

        Get a receipt in PDF
        """
        path = urljoin("https://api.accounting.sh", "/receipts/{uuid}/document")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.receipts_api.get_receipt_document(
                "uuid_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_list_receipts(self, m) -> None:
        """Test case for list_receipts

        List company's receipts
        """
        path = urljoin("https://api.accounting.sh", "/receipts")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.receipts_api.list_receipts(
                "fields_example",
                "page_example",
                "per_page_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_update_receipt(self, m) -> None:
        """Test case for update_receipt

        Update a receipt
        """
        path = urljoin("https://api.accounting.sh", "/receipts/{uuid}")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("PUT", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.receipts_api.update_receipt(
                "uuid_example",
                {},
            )
            is not None
        )


if __name__ == "__main__":
    unittest.main()
