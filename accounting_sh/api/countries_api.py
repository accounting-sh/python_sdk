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


class CountriesApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, accounting) -> None:
        self.accounting = accounting

    def get_translated_countries(self, lang: str, **kwargs) -> Any | None:
        """Get translated list of countries


        :param lang: The target language (required)
        :type lang: str
        :return: Returns a dict containing the API Response.
        """  # noqa: E501

        path = "/countries/{lang}"
        query_params = {}
        kwargs = kwargs | {"files": {}, "data": {}, "json": {}}

        if lang is not None:
            path = path.replace("{" + "lang" + "}", lang)

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
