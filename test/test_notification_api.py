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
from accounting_sh.api.notification_api import NotificationApi


class TestNotificationApi(unittest.TestCase):
    """NotificationApi unit test stubs"""

    """
    def setUp(self) -> None:
        accounting = Accounting("fake-token")
        self.api = accounting.notification_api

    def tearDown(self) -> None:
        pass
    """

    @requests_mock.Mocker()
    def test_list_notification_preferences(self, m) -> None:
        """Test case for list_notification_preferences

        List notification preferences
        """
        path = urljoin(
            "https://api.accounting.sh", "/notifications/preferences/{notification}"
        )
        path = path.replace("{" + "notification" + "}", "notification_example")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.notification_api.list_notification_preferences(
                "notification_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_list_notifications(self, m) -> None:
        """Test case for list_notifications

        List company's notifications
        """
        path = urljoin("https://api.accounting.sh", "/notifications")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.notification_api.list_notifications(
                "fields_example",
                "page_example",
                "per_page_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_send_notification(self, m) -> None:
        """Test case for send_notification

        Send a notification
        """
        path = urljoin("https://api.accounting.sh", "/notifications/send")
        m.request("POST", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.notification_api.send_notification(
                {},
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_update_notification_preferences(self, m) -> None:
        """Test case for update_notification_preferences

        Update notification preferences
        """
        path = urljoin(
            "https://api.accounting.sh", "/notifications/preferences/{notification}"
        )
        path = path.replace("{" + "notification" + "}", "notification_example")
        m.request("PUT", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.notification_api.update_notification_preferences(
                "notification_example",
                {},
            )
            is not None
        )


if __name__ == "__main__":
    unittest.main()
