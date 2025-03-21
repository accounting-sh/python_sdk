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


class BillsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, accounting) -> None:
        self.accounting = accounting

    def add_bill(self, add_bill_request: dict, **kwargs) -> Any | None:
        """Add a bill


        :param add_bill_request: (required)
        :type add_bill_request: AddBillRequest
        :return: Returns a dict containing the API Response.
        """  # noqa: E501

        path = "/expenses/bills"
        query_params = {}
        kwargs = kwargs | {"files": {}, "data": {}, "json": {}}

        if add_bill_request is not None:
            kwargs["json"] = add_bill_request

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

    def add_bill_payment(
        self, uuid: str, add_bill_payment_request: dict, **kwargs
    ) -> Any | None:
        """Add a bill payment


        :param uuid: The bill uuid (required)
        :type uuid: str
        :param add_bill_payment_request: (required)
        :type add_bill_payment_request: AddBillPaymentRequest
        :return: Returns a dict containing the API Response.
        """  # noqa: E501

        path = "/expenses/bills/{uuid}/payments"
        query_params = {}
        kwargs = kwargs | {"files": {}, "data": {}, "json": {}}

        if uuid is not None:
            path = path.replace("{" + "uuid" + "}", uuid)
        if add_bill_payment_request is not None:
            kwargs["json"] = add_bill_payment_request

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

    def delete_bill(self, uuid: str, **kwargs) -> Any | None:
        """Delete a bill


        :param uuid: The bill uuid (required)
        :type uuid: str
        :return: Returns a dict containing the API Response.
        """  # noqa: E501

        path = "/expenses/bills/{uuid}"
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

    def get_bill(self, uuid: str, **kwargs) -> Any | None:
        """Get a bill


        :param uuid: The bill uuid (required)
        :type uuid: str
        :return: Returns a dict containing the API Response.
        """  # noqa: E501

        path = "/expenses/bills/{uuid}"
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

    def get_bill_document(self, uuid: str, **kwargs) -> Any | None:
        """Get a bill in PDF

        This endpoint generate a bill in PDF if `selfbilling` is set to true

        :param uuid: The invoice uuid (required)
        :type uuid: str
        :return: Returns a dict containing the API Response.
        """  # noqa: E501

        path = "/expenses/bills/{uuid}/document"
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

    def list_bills(
        self, fields: str = None, page: str = None, per_page: str = None, **kwargs
    ) -> Any | None:
        """List company's bills


        :param fields: A comma separated list of fields requested in the response
        :type fields: str
        :param page: The response page
        :type page: str
        :param per_page: The number of items per page
        :type per_page: str
        :return: Returns a dict containing the API Response.
        """  # noqa: E501

        path = "/expenses/bills"
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

    def update_bill(self, uuid: str, add_bill_request: dict, **kwargs) -> Any | None:
        """Update a bill


        :param uuid: The bill uuid (required)
        :type uuid: str
        :param add_bill_request: (required)
        :type add_bill_request: AddBillRequest
        :return: Returns a dict containing the API Response.
        """  # noqa: E501

        path = "/expenses/bills/{uuid}"
        query_params = {}
        kwargs = kwargs | {"files": {}, "data": {}, "json": {}}

        if uuid is not None:
            path = path.replace("{" + "uuid" + "}", uuid)
        if add_bill_request is not None:
            kwargs["json"] = add_bill_request

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

    def update_bill_payment(
        self, uuid: str, payment: str, add_bill_payment_request: dict, **kwargs
    ) -> Any | None:
        """Update a bill payment


        :param uuid: The bill uuid (required)
        :type uuid: str
        :param payment: The bill payment uuid (required)
        :type payment: str
        :param add_bill_payment_request: (required)
        :type add_bill_payment_request: AddBillPaymentRequest
        :return: Returns a dict containing the API Response.
        """  # noqa: E501

        path = "/expenses/bills/{uuid}/payments/{payment}"
        query_params = {}
        kwargs = kwargs | {"files": {}, "data": {}, "json": {}}

        if uuid is not None:
            path = path.replace("{" + "uuid" + "}", uuid)
        if payment is not None:
            path = path.replace("{" + "payment" + "}", payment)
        if add_bill_payment_request is not None:
            kwargs["json"] = add_bill_payment_request

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
