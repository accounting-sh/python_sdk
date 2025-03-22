# coding: utf-8

"""
Accounting API


The version of the OpenAPI document: 8.0.6
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import warnings
from json import dumps
from typing import Any, Dict, List, Optional, Tuple, Union
from urllib.parse import urlencode

from typing_extensions import Annotated


class AuthApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, accounting) -> None:
        self.accounting = accounting

    def auth_init(self, **kwargs) -> Any | None:
        """Init authentication process


        :return: Returns a dict containing the API Response.
        """  # noqa: E501

        path = "/auth/init"
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

    def login(self, login_request: dict, **kwargs) -> Any | None:
        """Login user


        :param login_request: (required)
        :type login_request: LoginRequest
        :return: Returns a dict containing the API Response.
        """  # noqa: E501

        path = "/auth/login"
        query_params = {}
        kwargs = kwargs | {"files": {}, "data": {}, "json": {}}

        if login_request is not None:
            kwargs["json"] = login_request

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

    def logout(self, **kwargs) -> Any | None:
        """Logout current user


        :return: Returns a dict containing the API Response.
        """  # noqa: E501

        path = "/auth/logout"
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

    def switch_company(self, switch_company_request: dict, **kwargs) -> Any | None:
        """Switch to a different company


        :param switch_company_request: (required)
        :type switch_company_request: SwitchCompanyRequest
        :return: Returns a dict containing the API Response.
        """  # noqa: E501

        path = "/auth/switch"
        query_params = {}
        kwargs = kwargs | {"files": {}, "data": {}, "json": {}}

        if switch_company_request is not None:
            kwargs["json"] = switch_company_request

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
