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
from accounting_sh.api.logs_api import LogsApi


class TestLogsApi(unittest.TestCase):
    """LogsApi unit test stubs"""

    """
    def setUp(self) -> None:
        accounting = Accounting("fake-token")
        self.api = accounting.logs_api

    def tearDown(self) -> None:
        pass
    """

    @requests_mock.Mocker()
    def test_logs(self, m) -> None:
        """Test case for logs

        List company's logs
        """
        path = urljoin("https://api.accounting.sh", "/logs")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.logs_api.logs(
                "fields_example",
                "page_example",
                "per_page_example",
                "channel_example",
                "level_example",
                "resource_example",
                "before_example",
                "after_example",
                "format_example",
            )
            is not None
        )


if __name__ == "__main__":
    unittest.main()
