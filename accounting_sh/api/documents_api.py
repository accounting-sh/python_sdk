# coding: utf-8

"""
    Accounting API


    The version of the OpenAPI document: 7.5.10
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from json import dumps
from typing import Any, Dict, List, Optional, Tuple, Union
from urllib.parse import urlencode

from typing_extensions import Annotated


class DocumentsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, accounting) -> None:
        self.accounting = accounting

    def cancel_review(self, uuid: str, **kwargs) -> Any | None:
        """Cancel document review


        :param uuid: The document uuid (required)
        :type uuid: str
        :return: Returns a dict containing the API Response.
        """  # noqa: E501

        path = "/documents/{uuid}/review"
        query_params = {}
        kwargs = kwargs | {"files": {}, "data": {}, "json": {}}

        if uuid is not None:
            path = path.replace("{" + "uuid" + "}", uuid)

        if len(kwargs["data"]) == 0:
            del kwargs["data"]
        if len(kwargs["json"]) == 0:
            del kwargs["json"]
        if len(kwargs["files"]) == 0:
            del kwargs["files"]

        if len(query_params) > 0:
            query_params.update(
                {
                    k: dumps(v)
                    for k, v in query_params.items()
                    if isinstance(v, (bool, dict))
                }
            )
            path = path + "?" + urlencode(query_params, doseq=True)
        return self.accounting.request(method="DELETE", path=path, **kwargs)

    def delete_document(self, uuid: str, **kwargs) -> Any | None:
        """Delete a document


        :param uuid: The document uuid (required)
        :type uuid: str
        :return: Returns a dict containing the API Response.
        """  # noqa: E501

        path = "/documents/{uuid}"
        query_params = {}
        kwargs = kwargs | {"files": {}, "data": {}, "json": {}}

        if uuid is not None:
            path = path.replace("{" + "uuid" + "}", uuid)

        if len(kwargs["data"]) == 0:
            del kwargs["data"]
        if len(kwargs["json"]) == 0:
            del kwargs["json"]
        if len(kwargs["files"]) == 0:
            del kwargs["files"]

        if len(query_params) > 0:
            query_params.update(
                {
                    k: dumps(v)
                    for k, v in query_params.items()
                    if isinstance(v, (bool, dict))
                }
            )
            path = path + "?" + urlencode(query_params, doseq=True)
        return self.accounting.request(method="DELETE", path=path, **kwargs)

    def get_document(self, uuid: str, **kwargs) -> Any | None:
        """Get a document


        :param uuid: The document uuid (required)
        :type uuid: str
        :return: Returns a dict containing the API Response.
        """  # noqa: E501

        path = "/documents/{uuid}"
        query_params = {}
        kwargs = kwargs | {"files": {}, "data": {}, "json": {}}

        if uuid is not None:
            path = path.replace("{" + "uuid" + "}", uuid)

        if len(kwargs["data"]) == 0:
            del kwargs["data"]
        if len(kwargs["json"]) == 0:
            del kwargs["json"]
        if len(kwargs["files"]) == 0:
            del kwargs["files"]

        if len(query_params) > 0:
            query_params.update(
                {
                    k: dumps(v)
                    for k, v in query_params.items()
                    if isinstance(v, (bool, dict))
                }
            )
            path = path + "?" + urlencode(query_params, doseq=True)
        return self.accounting.request(method="GET", path=path, **kwargs)

    def list_documents(
        self, fields: str = None, page: str = None, per_page: str = None, **kwargs
    ) -> Any | None:
        """List company's documents


        :param fields: A comma separated list of fields requested in the response
        :type fields: str
        :param page: The response page
        :type page: str
        :param per_page: The number of items per page
        :type per_page: str
        :return: Returns a dict containing the API Response.
        """  # noqa: E501

        path = "/documents"
        query_params = {}
        kwargs = kwargs | {"files": {}, "data": {}, "json": {}}

        if fields is not None:

            query_params["fields"] = fields

        if page is not None:

            query_params["page"] = page

        if per_page is not None:

            query_params["per_page"] = per_page

        if len(kwargs["data"]) == 0:
            del kwargs["data"]
        if len(kwargs["json"]) == 0:
            del kwargs["json"]
        if len(kwargs["files"]) == 0:
            del kwargs["files"]

        if len(query_params) > 0:
            query_params.update(
                {
                    k: dumps(v)
                    for k, v in query_params.items()
                    if isinstance(v, (bool, dict))
                }
            )
            path = path + "?" + urlencode(query_params, doseq=True)
        return self.accounting.request(method="GET", path=path, **kwargs)

    def process_document(self, uuid: str, **kwargs) -> Any | None:
        """Process a document


        :param uuid: The document uuid (required)
        :type uuid: str
        :return: Returns a dict containing the API Response.
        """  # noqa: E501

        path = "/documents/{uuid}/process"
        query_params = {}
        kwargs = kwargs | {"files": {}, "data": {}, "json": {}}

        if uuid is not None:
            path = path.replace("{" + "uuid" + "}", uuid)

        if len(kwargs["data"]) == 0:
            del kwargs["data"]
        if len(kwargs["json"]) == 0:
            del kwargs["json"]
        if len(kwargs["files"]) == 0:
            del kwargs["files"]

        if len(query_params) > 0:
            query_params.update(
                {
                    k: dumps(v)
                    for k, v in query_params.items()
                    if isinstance(v, (bool, dict))
                }
            )
            path = path + "?" + urlencode(query_params, doseq=True)
        return self.accounting.request(method="GET", path=path, **kwargs)

    def review_url(self, uuid: str, **kwargs) -> Any | None:
        """Get url to review a document


        :param uuid: The document uuid (required)
        :type uuid: str
        :return: Returns a dict containing the API Response.
        """  # noqa: E501

        path = "/documents/{uuid}/review"
        query_params = {}
        kwargs = kwargs | {"files": {}, "data": {}, "json": {}}

        if uuid is not None:
            path = path.replace("{" + "uuid" + "}", uuid)

        if len(kwargs["data"]) == 0:
            del kwargs["data"]
        if len(kwargs["json"]) == 0:
            del kwargs["json"]
        if len(kwargs["files"]) == 0:
            del kwargs["files"]

        if len(query_params) > 0:
            query_params.update(
                {
                    k: dumps(v)
                    for k, v in query_params.items()
                    if isinstance(v, (bool, dict))
                }
            )
            path = path + "?" + urlencode(query_params, doseq=True)
        return self.accounting.request(method="GET", path=path, **kwargs)

    def update_document(
        self, uuid: str, update_document_request: dict, **kwargs
    ) -> Any | None:
        """Update a document


        :param uuid: The document uuid (required)
        :type uuid: str
        :param update_document_request: (required)
        :type update_document_request: UpdateDocumentRequest
        :return: Returns a dict containing the API Response.
        """  # noqa: E501

        path = "/documents/{uuid}"
        query_params = {}
        kwargs = kwargs | {"files": {}, "data": {}, "json": {}}

        if uuid is not None:
            path = path.replace("{" + "uuid" + "}", uuid)
        if update_document_request is not None:
            kwargs["json"] = update_document_request

        if len(kwargs["data"]) == 0:
            del kwargs["data"]
        if len(kwargs["json"]) == 0:
            del kwargs["json"]
        if len(kwargs["files"]) == 0:
            del kwargs["files"]

        if len(query_params) > 0:
            query_params.update(
                {
                    k: dumps(v)
                    for k, v in query_params.items()
                    if isinstance(v, (bool, dict))
                }
            )
            path = path + "?" + urlencode(query_params, doseq=True)
        return self.accounting.request(method="PUT", path=path, **kwargs)

    def upload_document(self, name: str, file: bytearray, **kwargs) -> Any | None:
        """Upload a document


        :param name: (required)
        :type name: str
        :param file: (required)
        :type file: bytearray
        :return: Returns a dict containing the API Response.
        """  # noqa: E501

        path = "/documents"
        query_params = {}
        kwargs = kwargs | {"files": {}, "data": {}, "json": {}}

        if name is not None:
            kwargs["data"]["name"] = name
        if file is not None:
            kwargs["data"]["file"] = file

        if len(kwargs["data"]) == 0:
            del kwargs["data"]
        if len(kwargs["json"]) == 0:
            del kwargs["json"]
        if len(kwargs["files"]) == 0:
            del kwargs["files"]

        if len(query_params) > 0:
            query_params.update(
                {
                    k: dumps(v)
                    for k, v in query_params.items()
                    if isinstance(v, (bool, dict))
                }
            )
            path = path + "?" + urlencode(query_params, doseq=True)
        return self.accounting.request(method="POST", path=path, **kwargs)

    def view_document(self, uuid: str, **kwargs) -> Any | None:
        """View a document


        :param uuid: The document uuid (required)
        :type uuid: str
        :return: Returns a dict containing the API Response.
        """  # noqa: E501

        path = "/documents/{uuid}/view"
        query_params = {}
        kwargs = kwargs | {"files": {}, "data": {}, "json": {}}

        if uuid is not None:
            path = path.replace("{" + "uuid" + "}", uuid)

        if len(kwargs["data"]) == 0:
            del kwargs["data"]
        if len(kwargs["json"]) == 0:
            del kwargs["json"]
        if len(kwargs["files"]) == 0:
            del kwargs["files"]

        if len(query_params) > 0:
            query_params.update(
                {
                    k: dumps(v)
                    for k, v in query_params.items()
                    if isinstance(v, (bool, dict))
                }
            )
            path = path + "?" + urlencode(query_params, doseq=True)
        return self.accounting.request(method="GET", path=path, **kwargs)
