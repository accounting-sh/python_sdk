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
from accounting_sh.api.payments_api import PaymentsApi


class TestPaymentsApi(unittest.TestCase):
    """PaymentsApi unit test stubs"""

    """
    def setUp(self) -> None:
        accounting = Accounting("fake-token")
        self.api = accounting.payments_api

    def tearDown(self) -> None:
        pass
    """

    @requests_mock.Mocker()
    def test_add_payment(self, m) -> None:
        """Test case for add_payment

        Add a payment
        """
        path = urljoin("https://api.accounting.sh", "/expenses/payments")
        m.request("POST", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.payments_api.add_payment(
                {},
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_delete_payment(self, m) -> None:
        """Test case for delete_payment

        Delete a payment
        """
        path = urljoin("https://api.accounting.sh", "/expenses/payments/{uuid}")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("DELETE", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.payments_api.delete_payment(
                "uuid_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_get_payment(self, m) -> None:
        """Test case for get_payment

        Get a payment
        """
        path = urljoin("https://api.accounting.sh", "/expenses/payments/{uuid}")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.payments_api.get_payment(
                "uuid_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_list_payments(self, m) -> None:
        """Test case for list_payments

        List company's payments
        """
        path = urljoin("https://api.accounting.sh", "/expenses/payments")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.payments_api.list_payments(
                "fields_example",
                "page_example",
                "per_page_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_update_payment(self, m) -> None:
        """Test case for update_payment

        Update a payment
        """
        path = urljoin("https://api.accounting.sh", "/expenses/payments/{uuid}")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("PUT", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.payments_api.update_payment(
                "uuid_example",
                {},
            )
            is not None
        )


if __name__ == "__main__":
    unittest.main()