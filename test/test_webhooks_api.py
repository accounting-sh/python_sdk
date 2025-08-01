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
from accounting_sh.api.webhooks_api import WebhooksApi


class TestWebhooksApi(unittest.TestCase):
    """WebhooksApi unit test stubs"""

    """
    def setUp(self) -> None:
        accounting = Accounting("fake-token")
        self.api = accounting.webhooks_api

    def tearDown(self) -> None:
        pass
    """

    @requests_mock.Mocker()
    def test_add_webhook(self, m) -> None:
        """Test case for add_webhook

        Add a webhook
        """
        path = urljoin("https://api.accounting.sh", "/webhooks")
        m.request("POST", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.webhooks_api.add_webhook(
                {},
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_delete_webhook(self, m) -> None:
        """Test case for delete_webhook

        Delete a webhook
        """
        path = urljoin("https://api.accounting.sh", "/webhooks/{uuid}")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("DELETE", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.webhooks_api.delete_webhook(
                "uuid_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_get_webhook(self, m) -> None:
        """Test case for get_webhook

        Get a webhook
        """
        path = urljoin("https://api.accounting.sh", "/webhooks/{uuid}")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.webhooks_api.get_webhook(
                "uuid_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_get_webhook_history(self, m) -> None:
        """Test case for get_webhook_history

        Get webhook's history
        """
        path = urljoin("https://api.accounting.sh", "/webhooks/{uuid}/history")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.webhooks_api.get_webhook_history(
                "uuid_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_list_webhook_events(self, m) -> None:
        """Test case for list_webhook_events

        List available webhook events
        """
        path = urljoin("https://api.accounting.sh", "/webhooks/events")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert accounting.webhooks_api.list_webhook_events() is not None

    @requests_mock.Mocker()
    def test_list_webhooks(self, m) -> None:
        """Test case for list_webhooks

        List company's webhooks
        """
        path = urljoin("https://api.accounting.sh", "/webhooks")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.webhooks_api.list_webhooks(
                "fields_example",
                "page_example",
                "per_page_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_update_webhook(self, m) -> None:
        """Test case for update_webhook

        Update a webhook
        """
        path = urljoin("https://api.accounting.sh", "/webhooks/{uuid}")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("PUT", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.webhooks_api.update_webhook(
                {},
                "uuid_example",
            )
            is not None
        )


if __name__ == "__main__":
    unittest.main()
