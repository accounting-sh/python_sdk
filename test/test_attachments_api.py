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
from accounting_sh.api.attachments_api import AttachmentsApi


class TestAttachmentsApi(unittest.TestCase):
    """AttachmentsApi unit test stubs"""

    """
    def setUp(self) -> None:
        accounting = Accounting("fake-token")
        self.api = accounting.attachments_api

    def tearDown(self) -> None:
        pass
    """

    @requests_mock.Mocker()
    def test_add_attachment(self, m) -> None:
        """Test case for add_attachment

        Add an attachment
        """
        path = urljoin("https://api.accounting.sh", "/attachments")
        m.request("POST", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.attachments_api.add_attachment(
                {},
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_delete_attachment(self, m) -> None:
        """Test case for delete_attachment

        Delete an attachment
        """
        path = urljoin("https://api.accounting.sh", "/attachments/{uuid}")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("DELETE", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.attachments_api.delete_attachment(
                "uuid_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_get_attachment(self, m) -> None:
        """Test case for get_attachment

        Get an attachment
        """
        path = urljoin("https://api.accounting.sh", "/attachments/{uuid}")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.attachments_api.get_attachment(
                "uuid_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_list_attachments(self, m) -> None:
        """Test case for list_attachments

        List company's attachments
        """
        path = urljoin("https://api.accounting.sh", "/attachments")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.attachments_api.list_attachments(
                "fields_example",
                "page_example",
                "per_page_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_retrieve_attachments(self, m) -> None:
        """Test case for retrieve_attachments

        List company's attachments link to resource
        """
        path = urljoin("https://api.accounting.sh", "/attachments/resource/{resource}")
        path = path.replace("{" + "resource" + "}", "resource_example")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.attachments_api.retrieve_attachments(
                "resource_example",
                "fields_example",
                "page_example",
                "per_page_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_update_attachment(self, m) -> None:
        """Test case for update_attachment

        Update an attachment
        """
        path = urljoin("https://api.accounting.sh", "/attachments/{uuid}")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("PUT", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.attachments_api.update_attachment(
                "uuid_example",
                {},
            )
            is not None
        )


if __name__ == "__main__":
    unittest.main()
