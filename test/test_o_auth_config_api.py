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
from accounting_sh.api.o_auth_config_api import OAuthConfigApi


class TestOAuthConfigApi(unittest.TestCase):
    """OAuthConfigApi unit test stubs"""

    """
    def setUp(self) -> None:
        accounting = Accounting("fake-token")
        self.api = accounting.o_auth_config_api

    def tearDown(self) -> None:
        pass
    """

    @requests_mock.Mocker()
    def test_add_o_auth_configuration(self, m) -> None:
        """Test case for add_o_auth_configuration

        Add an OAuth configuration
        """
        path = urljoin("https://api.accounting.sh", "/oauth")
        m.request("POST", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.o_auth_config_api.add_o_auth_configuration(
                {},
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_delete_o_auth_configuration(self, m) -> None:
        """Test case for delete_o_auth_configuration

        Delete an oauth configuration
        """
        path = urljoin("https://api.accounting.sh", "/oauth/{uuid}")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("DELETE", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.o_auth_config_api.delete_o_auth_configuration(
                "uuid_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_get_o_auth_configuration(self, m) -> None:
        """Test case for get_o_auth_configuration

        Get an OAuth configuration
        """
        path = urljoin("https://api.accounting.sh", "/oauth/{uuid}")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.o_auth_config_api.get_o_auth_configuration(
                "uuid_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_list_o_auth_configurations(self, m) -> None:
        """Test case for list_o_auth_configurations

        List company's oauth configurations
        """
        path = urljoin("https://api.accounting.sh", "/oauth")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.o_auth_config_api.list_o_auth_configurations(
                "fields_example",
                "page_example",
                "per_page_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_list_providers(self, m) -> None:
        """Test case for list_providers

        List available providers
        """
        path = urljoin("https://api.accounting.sh", "/oauth/providers")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert accounting.o_auth_config_api.list_providers() is not None

    @requests_mock.Mocker()
    def test_update_o_auth_configuration(self, m) -> None:
        """Test case for update_o_auth_configuration

        Update an oauth configuration
        """
        path = urljoin("https://api.accounting.sh", "/oauth/{uuid}")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("PUT", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.o_auth_config_api.update_o_auth_configuration(
                "uuid_example",
                {},
            )
            is not None
        )


if __name__ == "__main__":
    unittest.main()
