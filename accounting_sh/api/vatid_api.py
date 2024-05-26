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


class VATIDApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, accounting) -> None:
        self.accounting = accounting

    def add_company_vat_id(
        self,
        add_company_vat_id_request: dict,
        uuid: str = None,
    ) -> Any | None:
        """Add a company's Vat Id


        :param add_company_vat_id_request: (required)
        :type add_company_vat_id_request: AddCompanyVatIdRequest
        :param uuid: The company uuid
        :type uuid: str
        :return: Returns a dict containing the API Response.
        """  # noqa: E501

        path = "/companies/{uuid}/vat"
        query_params = {}
        kwargs = {"files": {}, "data": {}, "json": {}}

        if uuid is not None:
            path = path.replace("{" + "uuid" + "}", uuid)
        if add_company_vat_id_request is not None:
            kwargs["json"] = add_company_vat_id_request

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

    def delete_company_vat_id(
        self,
        key: str,
        uuid: str = None,
    ) -> Any | None:
        """Delete a company's Vat Id


        :param key: The VAT ID uuid (required)
        :type key: str
        :param uuid: The company uuid
        :type uuid: str
        :return: Returns a dict containing the API Response.
        """  # noqa: E501

        path = "/companies/{uuid}/vat/{key}"
        query_params = {}
        kwargs = {"files": {}, "data": {}, "json": {}}

        if uuid is not None:
            path = path.replace("{" + "uuid" + "}", uuid)
        if key is not None:
            path = path.replace("{" + "key" + "}", key)

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

    def get_company_vat_id(
        self,
        key: str,
        uuid: str = None,
    ) -> Any | None:
        """Get a company's Vat Id


        :param key: The VAT ID uuid (required)
        :type key: str
        :param uuid: The company uuid
        :type uuid: str
        :return: Returns a dict containing the API Response.
        """  # noqa: E501

        path = "/companies/{uuid}/vat/{key}"
        query_params = {}
        kwargs = {"files": {}, "data": {}, "json": {}}

        if uuid is not None:
            path = path.replace("{" + "uuid" + "}", uuid)
        if key is not None:
            path = path.replace("{" + "key" + "}", key)

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

    def list_company_vat_id(
        self,
        fields: str = None,
        page: str = None,
        per_page: str = None,
        uuid: str = None,
    ) -> Any | None:
        """List company's Vat Id


        :param fields: A comma separated list of fields requested in the response
        :type fields: str
        :param page: The response page
        :type page: str
        :param per_page: The number of items per page
        :type per_page: str
        :param uuid: The company uuid
        :type uuid: str
        :return: Returns a dict containing the API Response.
        """  # noqa: E501

        path = "/companies/{uuid}/vat"
        query_params = {}
        kwargs = {"files": {}, "data": {}, "json": {}}

        if uuid is not None:
            path = path.replace("{" + "uuid" + "}", uuid)
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

    def update_company_vat_id(
        self,
        key: str,
        add_company_vat_id_request: dict,
        uuid: str = None,
    ) -> Any | None:
        """Update a company's Vat Id


        :param key: The VAT ID uuid (required)
        :type key: str
        :param add_company_vat_id_request: (required)
        :type add_company_vat_id_request: AddCompanyVatIdRequest
        :param uuid: The company uuid
        :type uuid: str
        :return: Returns a dict containing the API Response.
        """  # noqa: E501

        path = "/companies/{uuid}/vat/{key}"
        query_params = {}
        kwargs = {"files": {}, "data": {}, "json": {}}

        if uuid is not None:
            path = path.replace("{" + "uuid" + "}", uuid)
        if key is not None:
            path = path.replace("{" + "key" + "}", key)
        if add_company_vat_id_request is not None:
            kwargs["json"] = add_company_vat_id_request

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