# coding: utf-8

"""
    Accounting API


    The version of the OpenAPI document: 7.3.11
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from json import dumps
from typing import Any, Dict, List, Optional, Tuple, Union
from urllib.parse import urlencode

from typing_extensions import Annotated


class CompanyStatisticsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, accounting) -> None:
        self.accounting = accounting

    def get_statistics(
        self, uuid: str, start: str = None, end: str = None, **kwargs
    ) -> Any | None:
        """Get company's statistic


        :param uuid: The company uuid (required)
        :type uuid: str
        :param start: Start date
        :type start: str
        :param end: End date
        :type end: str
        :return: Returns a dict containing the API Response.
        """  # noqa: E501

        path = "/companies/{uuid}/statistics/period"
        query_params = {}
        kwargs = kwargs | {"files": {}, "data": {}, "json": {}}

        if uuid is not None:
            path = path.replace("{" + "uuid" + "}", uuid)
        if start is not None:

            query_params["start"] = start

        if end is not None:

            query_params["end"] = end

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
