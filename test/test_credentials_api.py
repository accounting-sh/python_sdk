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
from accounting_sh.api.credentials_api import CredentialsApi


class TestCredentialsApi(unittest.TestCase):
    """CredentialsApi unit test stubs"""

    """
    def setUp(self) -> None:
        accounting = Accounting("fake-token")
        self.api = accounting.credentials_api

    def tearDown(self) -> None:
        pass
    """

    @requests_mock.Mocker()
    def test_add_credential(self, m) -> None:
        """Test case for add_credential

        Add a credential
        """
        path = urljoin("https://api.accounting.sh", "/credentials")
        m.request("POST", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.credentials_api.add_credential(
                {},
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_delete_credential(self, m) -> None:
        """Test case for delete_credential

        Delete a credential
        """
        path = urljoin("https://api.accounting.sh", "/credentials/{uuid}")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("DELETE", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.credentials_api.delete_credential(
                "uuid_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_get_credential(self, m) -> None:
        """Test case for get_credential

        Get a credential
        """
        path = urljoin("https://api.accounting.sh", "/credentials/{uuid}")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.credentials_api.get_credential(
                "uuid_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_list_credentials(self, m) -> None:
        """Test case for list_credentials

        List company's credentials
        """
        path = urljoin("https://api.accounting.sh", "/credentials")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.credentials_api.list_credentials(
                "fields_example",
                "page_example",
                "per_page_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_list_permissions(self, m) -> None:
        """Test case for list_permissions

        List available permissions
        """
        path = urljoin("https://api.accounting.sh", "/credentials/permissions")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert accounting.credentials_api.list_permissions() is not None

    @requests_mock.Mocker()
    def test_me(self, m) -> None:
        """Test case for me

        Get current credential informations
        """
        path = urljoin("https://api.accounting.sh", "/me")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert accounting.credentials_api.me() is not None

    @requests_mock.Mocker()
    def test_update_credential(self, m) -> None:
        """Test case for update_credential

        Update a credential
        """
        path = urljoin("https://api.accounting.sh", "/credentials/{uuid}")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("PUT", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.credentials_api.update_credential(
                "uuid_example",
                {},
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_userveria(self, m) -> None:
        """Test case for userveria

        Exchange a my stantabcorp (userveria) token for an Accounting Token
        """
        path = urljoin("https://api.accounting.sh", "/userveria")
        m.request("POST", path)
        accounting = Accounting("fake-token")
        assert accounting.credentials_api.userveria() is not None


if __name__ == "__main__":
    unittest.main()
