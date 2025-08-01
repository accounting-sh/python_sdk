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
from accounting_sh.api.documents_api import DocumentsApi


class TestDocumentsApi(unittest.TestCase):
    """DocumentsApi unit test stubs"""

    """
    def setUp(self) -> None:
        accounting = Accounting("fake-token")
        self.api = accounting.documents_api

    def tearDown(self) -> None:
        pass
    """

    @requests_mock.Mocker()
    def test_cancel_review(self, m) -> None:
        """Test case for cancel_review

        Cancel document review
        """
        path = urljoin("https://api.accounting.sh", "/documents/{uuid}/review")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("DELETE", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.documents_api.cancel_review(
                "uuid_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_delete_document(self, m) -> None:
        """Test case for delete_document

        Delete a document
        """
        path = urljoin("https://api.accounting.sh", "/documents/{uuid}")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("DELETE", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.documents_api.delete_document(
                "uuid_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_get_document(self, m) -> None:
        """Test case for get_document

        Get a document
        """
        path = urljoin("https://api.accounting.sh", "/documents/{uuid}")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.documents_api.get_document(
                "uuid_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_list_documents(self, m) -> None:
        """Test case for list_documents

        List company's documents
        """
        path = urljoin("https://api.accounting.sh", "/documents")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.documents_api.list_documents(
                "fields_example",
                "page_example",
                "per_page_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_process_document(self, m) -> None:
        """Test case for process_document

        Process a document
        """
        path = urljoin("https://api.accounting.sh", "/documents/{uuid}/process")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.documents_api.process_document(
                "uuid_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_review_url(self, m) -> None:
        """Test case for review_url

        Get url to review a document
        """
        path = urljoin("https://api.accounting.sh", "/documents/{uuid}/review")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.documents_api.review_url(
                "uuid_example",
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_update_document(self, m) -> None:
        """Test case for update_document

        Update a document
        """
        path = urljoin("https://api.accounting.sh", "/documents/{uuid}")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("PUT", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.documents_api.update_document(
                "uuid_example",
                {},
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_upload_document(self, m) -> None:
        """Test case for upload_document

        Upload a document
        """
        path = urljoin("https://api.accounting.sh", "/documents")
        m.request("POST", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.documents_api.upload_document(
                "name_example",
                None,
            )
            is not None
        )

    @requests_mock.Mocker()
    def test_view_document(self, m) -> None:
        """Test case for view_document

        View a document
        """
        path = urljoin("https://api.accounting.sh", "/documents/{uuid}/view")
        path = path.replace("{" + "uuid" + "}", "uuid_example")
        m.request("GET", path)
        accounting = Accounting("fake-token")
        assert (
            accounting.documents_api.view_document(
                "uuid_example",
            )
            is not None
        )


if __name__ == "__main__":
    unittest.main()
