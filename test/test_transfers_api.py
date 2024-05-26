# coding: utf-8

"""
    Accounting API


    The version of the OpenAPI document: VERSION_HERE
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
from urllib.parse import urljoin

import requests_mock

from accounting_sh.accounting import Accounting
from accounting_sh.api.transfers_api import TransfersApi


class TestTransfersApi(unittest.TestCase):
    """TransfersApi unit test stubs"""

    """
    def setUp(self) -> None:
        accounting = Accounting("fake-token")
        self.api = accounting.transfers_api

    def tearDown(self) -> None:
        pass
    """

    @requests_mock.Mocker()
    def test_add_transfer(self, m) -> None:
        """Test case for add_transfer

        Add a transfer
        """
        path = urljoin("https://api.accounting.sh", "/transfers")
        m.request("POST", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.transfers_api.add_transfer(
                {},
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_delete_transfer(self, m) -> None:
        """Test case for delete_transfer

        Delete a transfer
        """
        path = urljoin("https://api.accounting.sh", "/transfers/{uuid}")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("DELETE", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.transfers_api.delete_transfer(
                "uuid_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_get_transfer(self, m) -> None:
        """Test case for get_transfer

        Get a transfer
        """
        path = urljoin("https://api.accounting.sh", "/transfers/{uuid}")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.transfers_api.get_transfer(
                "uuid_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_list_transfers(self, m) -> None:
        """Test case for list_transfers

        List company's transfers
        """
        path = urljoin("https://api.accounting.sh", "/transfers")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.transfers_api.list_transfers(
                "fields_example",
                "page_example",
                "per_page_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_update_transfer(self, m) -> None:
        """Test case for update_transfer

        Update a transfer
        """
        path = urljoin("https://api.accounting.sh", "/transfers/{uuid}")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("PUT", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.transfers_api.update_transfer(
                "uuid_example",
                {},
            )
            is not None
        )


if __name__ == "__main__":
    unittest.main()
