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
from accounting_sh.api.contacts_api import ContactsApi


class TestContactsApi(unittest.TestCase):
    """ContactsApi unit test stubs"""

    """
    def setUp(self) -> None:
        accounting = Accounting("fake-token")
        self.api = accounting.contacts_api

    def tearDown(self) -> None:
        pass
    """

    @requests_mock.Mocker()
    def test_add_contact(self, m) -> None:
        """Test case for add_contact

        Create a new contact
        """
        path = urljoin("https://api.accounting.sh", "/contacts")
        m.request("POST", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.contacts_api.add_contact(
                {},
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_delete_contact(self, m) -> None:
        """Test case for delete_contact

        Delete a contact
        """
        path = urljoin("https://api.accounting.sh", "/contacts/{uuid}")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("DELETE", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.contacts_api.delete_contact(
                "uuid_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_get_contact(self, m) -> None:
        """Test case for get_contact

        Retrieve a contact
        """
        path = urljoin("https://api.accounting.sh", "/contacts/{uuid}")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.contacts_api.get_contact(
                "uuid_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_list_contact_bills(self, m) -> None:
        """Test case for list_contact_bills

        List a contact's bills
        """
        path = urljoin("https://api.accounting.sh", "/contacts/{uuid}/bills")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.contacts_api.list_contact_bills(
                "uuid_example",
                "fields_example",
                "page_example",
                "per_page_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_list_contact_invoices(self, m) -> None:
        """Test case for list_contact_invoices

        List a contact's invoices
        """
        path = urljoin("https://api.accounting.sh", "/contacts/{uuid}/invoices")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.contacts_api.list_contact_invoices(
                "uuid_example",
                "fields_example",
                "page_example",
                "per_page_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_list_contacts(self, m) -> None:
        """Test case for list_contacts

        List company's contacts
        """
        path = urljoin("https://api.accounting.sh", "/contacts")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.contacts_api.list_contacts(
                "fields_example",
                "page_example",
                "per_page_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_update_contact(self, m) -> None:
        """Test case for update_contact

        Update a contact
        """
        path = urljoin("https://api.accounting.sh", "/contact/{uuid}")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("PUT", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.contacts_api.update_contact(
                "uuid_example",
                {},
            )
            is not None
        )


if __name__ == "__main__":
    unittest.main()
