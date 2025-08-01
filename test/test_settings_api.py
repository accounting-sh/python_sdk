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
from accounting_sh.api.settings_api import SettingsApi


class TestSettingsApi(unittest.TestCase):
    """SettingsApi unit test stubs"""

    """
    def setUp(self) -> None:
        accounting = Accounting("fake-token")
        self.api = accounting.settings_api

    def tearDown(self) -> None:
        pass
    """

    @requests_mock.Mocker()
    def test_get_settings(self, m) -> None:
        """Test case for get_settings

        Get a company's settings
        """
        path = urljoin("https://api.accounting.sh", "/companies/{uuid}/settings/{key}")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        path = path.replace("{" + "key" + "}", "key_example")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.settings_api.get_settings(
                "uuid_example",
                "key_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_list_settings(self, m) -> None:
        """Test case for list_settings

        List company's settings
        """
        path = urljoin("https://api.accounting.sh", "/companies/{uuid}/settings")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.settings_api.list_settings(
                "fields_example",
                "page_example",
                "per_page_example",
                "uuid_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_update_settings(self, m) -> None:
        """Test case for update_settings

        Update a company's settings
        """
        path = urljoin("https://api.accounting.sh", "/companies/{uuid}/settings/{key}")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        path = path.replace("{" + "key" + "}", "key_example")
        m.request("PUT", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.settings_api.update_settings(
                "uuid_example",
                "key_example",
                {},
            )
            is not None
        )


if __name__ == "__main__":
    unittest.main()
