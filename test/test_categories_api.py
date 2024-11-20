# coding: utf-8

"""
    Accounting API


    The version of the OpenAPI document: 7.5.10
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
from urllib.parse import urljoin

import requests_mock

from accounting_sh.accounting import Accounting
from accounting_sh.api.categories_api import CategoriesApi


class TestCategoriesApi(unittest.TestCase):
    """CategoriesApi unit test stubs"""

    """
    def setUp(self) -> None:
        accounting = Accounting("fake-token")
        self.api = accounting.categories_api

    def tearDown(self) -> None:
        pass
    """

    @requests_mock.Mocker()
    def test_add_category(self, m) -> None:
        """Test case for add_category

        Add a category
        """
        path = urljoin("https://api.accounting.sh", "/categories")
        m.request("POST", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.categories_api.add_category(
                {},
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_delete_category(self, m) -> None:
        """Test case for delete_category

        Delete a category
        """
        path = urljoin("https://api.accounting.sh", "/categories/{uuid}")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("DELETE", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.categories_api.delete_category(
                "uuid_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_get_category(self, m) -> None:
        """Test case for get_category

        Get a category
        """
        path = urljoin("https://api.accounting.sh", "/categories/{uuid}")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.categories_api.get_category(
                "uuid_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_list_categories(self, m) -> None:
        """Test case for list_categories

        List company's categories
        """
        path = urljoin("https://api.accounting.sh", "/categories")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.categories_api.list_categories(
                "fields_example",
                "page_example",
                "per_page_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_update_category(self, m) -> None:
        """Test case for update_category

        Update a category
        """
        path = urljoin("https://api.accounting.sh", "/categories/{uuid}")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("PUT", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.categories_api.update_category(
                "uuid_example",
                {},
            )
            is not None
        )


if __name__ == "__main__":
    unittest.main()
