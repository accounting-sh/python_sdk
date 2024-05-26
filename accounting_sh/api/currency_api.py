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


class CurrencyApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, accounting) -> None:
        self.accounting = accounting

    def get_exchange_rate(
        self,
        var_from: str,
        to: str,
    ) -> Any | None:
        """Get the latest currency exchange rate


        :param var_from: The currency to convert from (required)
        :type var_from: str
        :param to: The currency to convert to (required)
        :type to: str
        :return: Returns a dict containing the API Response.
        """  # noqa: E501

        path = "/currency/{from}/{to}"
        query_params = {}
        kwargs = {"files": {}, "data": {}, "json": {}}

        if var_from is not None:
            path = path.replace("{" + "from" + "}", var_from)
        if to is not None:
            path = path.replace("{" + "to" + "}", to)

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
