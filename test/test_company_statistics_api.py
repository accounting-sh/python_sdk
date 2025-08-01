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
from accounting_sh.api.company_statistics_api import CompanyStatisticsApi


class TestCompanyStatisticsApi(unittest.TestCase):
    """CompanyStatisticsApi unit test stubs"""

    """
    def setUp(self) -> None:
        accounting = Accounting("fake-token")
        self.api = accounting.company_statistics_api

    def tearDown(self) -> None:
        pass
    """

    @requests_mock.Mocker()
    def test_get_statistics(self, m) -> None:
        """Test case for get_statistics

        Get company's statistic
        """
        path = urljoin(
            "https://api.accounting.sh", "/companies/{uuid}/statistics/period"
        )
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.company_statistics_api.get_statistics(
                "uuid_example",
                "start_example",
                "end_example",
            )
            is not None
        )


if __name__ == "__main__":
    unittest.main()
