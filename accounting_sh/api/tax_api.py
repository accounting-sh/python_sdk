# coding: utf-8

"""
Accounting API


The version of the OpenAPI document: 8.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import warnings
from json import dumps
from typing import Any, Dict, List, Optional, Tuple, Union
from urllib.parse import urlencode

from typing_extensions import Annotated


class TaxApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, accounting) -> None:
        self.accounting = accounting

    def get_tax_rate(self, country: str, **kwargs) -> Any | None:
        """Get the latest tax rate for a country


        :param country: The country (required)
        :type country: str
        :return: Returns a dict containing the API Response.
        """  # noqa: E501

        path = "/tax/{country}"
        query_params = {}
        kwargs = kwargs | {"files": {}, "data": {}, "json": {}}

        if country is not None:
            path = path.replace("{" + "country" + "}", country)

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

    def verify_vat_id(self, number: str, **kwargs) -> Any | None:
        """Verify a VAT ID


        :param number: The VAT ID (required)
        :type number: str
        :return: Returns a dict containing the API Response.
        """  # noqa: E501

        path = "/vat/verify/{number}"
        query_params = {}
        kwargs = kwargs | {"files": {}, "data": {}, "json": {}}

        if number is not None:
            path = path.replace("{" + "number" + "}", number)

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
