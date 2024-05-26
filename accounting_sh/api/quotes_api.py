# coding: utf-8

"""
    Accounting API


    The version of the OpenAPI document: VERSION_HERE
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from json import dumps
from typing import Any, Dict, List, Optional, Tuple, Union
from urllib.parse import urlencode

from typing_extensions import Annotated


class QuotesApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, accounting) -> None:
        self.accounting = accounting

    def add_quote(
        self,
        add_quote_request: dict,
    ) -> Any | None:
        """Add a quote


        :param add_quote_request: (required)
        :type add_quote_request: AddQuoteRequest
        :return: Returns a dict containing the API Response.
        """  # noqa: E501

        path = "/quotes"
        query_params = {}
        kwargs = {"files": {}, "data": {}, "json": {}}

        if add_quote_request is not None:
            kwargs["json"] = add_quote_request

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

    def delete_quote(
        self,
        uuid: str,
    ) -> Any | None:
        """Delete a quote


        :param uuid: The quote uuid (required)
        :type uuid: str
        :return: Returns a dict containing the API Response.
        """  # noqa: E501

        path = "/quotes/{uuid}"
        query_params = {}
        kwargs = {"files": {}, "data": {}, "json": {}}

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

    def get_quote(
        self,
        uuid: str,
    ) -> Any | None:
        """Get a quote


        :param uuid: The quote uuid (required)
        :type uuid: str
        :return: Returns a dict containing the API Response.
        """  # noqa: E501

        path = "/quotes/{uuid}"
        query_params = {}
        kwargs = {"files": {}, "data": {}, "json": {}}

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

    def get_quote_document(
        self,
        uuid: str,
    ) -> Any | None:
        """Get a quote in PDF


        :param uuid: The quote uuid (required)
        :type uuid: str
        :return: Returns a dict containing the API Response.
        """  # noqa: E501

        path = "/quotes/{uuid}/document"
        query_params = {}
        kwargs = {"files": {}, "data": {}, "json": {}}

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

    def list_quotes(
        self,
        fields: str = None,
        page: str = None,
        per_page: str = None,
    ) -> Any | None:
        """List company's quotes


        :param fields: A comma separated list of fields requested in the response
        :type fields: str
        :param page: The response page
        :type page: str
        :param per_page: The number of items per page
        :type per_page: str
        :return: Returns a dict containing the API Response.
        """  # noqa: E501

        path = "/quotes"
        query_params = {}
        kwargs = {"files": {}, "data": {}, "json": {}}

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

    def update_quote(
        self,
        uuid: str,
        add_quote_request: dict,
    ) -> Any | None:
        """Update a quote


        :param uuid: The quote uuid (required)
        :type uuid: str
        :param add_quote_request: (required)
        :type add_quote_request: AddQuoteRequest
        :return: Returns a dict containing the API Response.
        """  # noqa: E501

        path = "/quotes/{uuid}"
        query_params = {}
        kwargs = {"files": {}, "data": {}, "json": {}}

        if uuid is not None:
            path = path.replace("{" + "uuid" + "}", uuid)
        if add_quote_request is not None:
            kwargs["json"] = add_quote_request

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
