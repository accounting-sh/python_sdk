# coding: utf-8

"""
Accounting API


The version of the OpenAPI document: 7.5.11
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import warnings
from json import dumps
from typing import Any, Dict, List, Optional, Tuple, Union
from urllib.parse import urlencode

from typing_extensions import Annotated


class OAuthConfigApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, accounting) -> None:
        self.accounting = accounting

    def add_o_auth_configuration(
        self, add_o_auth_configuration_request: dict, **kwargs
    ) -> Any | None:
        """Add an OAuth configuration


        :param add_o_auth_configuration_request: (required)
        :type add_o_auth_configuration_request: AddOAuthConfigurationRequest
        :return: Returns a dict containing the API Response.
        """  # noqa: E501

        path = "/oauth"
        query_params = {}
        kwargs = kwargs | {"files": {}, "data": {}, "json": {}}

        if add_o_auth_configuration_request is not None:
            kwargs["json"] = add_o_auth_configuration_request

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

    def delete_o_auth_configuration(self, uuid: str, **kwargs) -> Any | None:
        """Delete an oauth configuration


        :param uuid: The oauth configuration uuid (required)
        :type uuid: str
        :return: Returns a dict containing the API Response.
        """  # noqa: E501

        path = "/oauth/{uuid}"
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

    def get_o_auth_configuration(self, uuid: str, **kwargs) -> Any | None:
        """Get an OAuth configuration


        :param uuid: The oauth configuration uuid (required)
        :type uuid: str
        :return: Returns a dict containing the API Response.
        """  # noqa: E501

        path = "/oauth/{uuid}"
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

    def list_o_auth_configurations(
        self, fields: str = None, page: str = None, per_page: str = None, **kwargs
    ) -> Any | None:
        """List company's oauth configurations


        :param fields: A comma separated list of fields requested in the response
        :type fields: str
        :param page: The response page
        :type page: str
        :param per_page: The number of items per page
        :type per_page: str
        :return: Returns a dict containing the API Response.
        """  # noqa: E501

        path = "/oauth"
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

    def list_providers(self, **kwargs) -> Any | None:
        """List available providers


        :return: Returns a dict containing the API Response.
        """  # noqa: E501

        path = "/oauth/providers"
        query_params = {}
        kwargs = kwargs | {"files": {}, "data": {}, "json": {}}

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

    def update_o_auth_configuration(
        self, uuid: str, add_o_auth_configuration_request: dict, **kwargs
    ) -> Any | None:
        """Update an oauth configuration


        :param uuid: The oauth configuration uuid (required)
        :type uuid: str
        :param add_o_auth_configuration_request: (required)
        :type add_o_auth_configuration_request: AddOAuthConfigurationRequest
        :return: Returns a dict containing the API Response.
        """  # noqa: E501

        path = "/oauth/{uuid}"
        query_params = {}
        kwargs = kwargs | {"files": {}, "data": {}, "json": {}}

        if uuid is not None:
            path = path.replace("{" + "uuid" + "}", uuid)
        if add_o_auth_configuration_request is not None:
            kwargs["json"] = add_o_auth_configuration_request

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
