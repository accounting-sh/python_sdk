# coding: utf-8

"""
Accounting API


The version of the OpenAPI document: 8.3.3
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import warnings
from json import dumps
from typing import Any, Dict, List, Optional, Tuple, Union
from urllib.parse import urlencode

from typing_extensions import Annotated


class SearchApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, accounting) -> None:
        self.accounting = accounting

    def search(
        self, q: str, exclude: str = None, only: str = None, **kwargs
    ) -> Any | None:
        """Search


        :param q: Query string (required)
        :type q: str
        :param exclude: Exclude specific types. This is a comma separated list.
        :type exclude: str
        :param only: Perfom search only on those types. This is a comma separated list.
        :type only: str
        :return: Returns a dict containing the API Response.
        """  # noqa: E501

        path = "/search"
        query_params = {}
        kwargs = kwargs | {"files": {}, "data": {}, "json": {}}

        if q is not None:

            query_params["q"] = q

        if exclude is not None:

            query_params["exclude"] = exclude

        if only is not None:

            query_params["only"] = only

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
