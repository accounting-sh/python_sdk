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


class NotificationApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, accounting) -> None:
        self.accounting = accounting

    def list_notification_preferences(self, notification: str, **kwargs) -> Any | None:
        """List notification preferences


        :param notification: The notification name (required)
        :type notification: str
        :return: Returns a dict containing the API Response.
        """  # noqa: E501

        path = "/notifications/preferences/{notification}"
        query_params = {}
        kwargs = kwargs | {"files": {}, "data": {}, "json": {}}

        if notification is not None:
            path = path.replace("{" + "notification" + "}", notification)

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

    def list_notifications(
        self, fields: str = None, page: str = None, per_page: str = None, **kwargs
    ) -> Any | None:
        """List company's notifications


        :param fields: A comma separated list of fields requested in the response
        :type fields: str
        :param page: The response page
        :type page: str
        :param per_page: The number of items per page
        :type per_page: str
        :return: Returns a dict containing the API Response.
        """  # noqa: E501

        path = "/notifications"
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

    def send_notification(
        self, send_notification_request: dict, **kwargs
    ) -> Any | None:
        """Send a notification


        :param send_notification_request: (required)
        :type send_notification_request: SendNotificationRequest
        :return: Returns a dict containing the API Response.
        """  # noqa: E501

        path = "/notifications/send"
        query_params = {}
        kwargs = kwargs | {"files": {}, "data": {}, "json": {}}

        if send_notification_request is not None:
            kwargs["json"] = send_notification_request

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

    def update_notification_preferences(
        self, notification: str, update_notification_preferences_request: dict, **kwargs
    ) -> Any | None:
        """Update notification preferences


        :param notification: The notification name (required)
        :type notification: str
        :param update_notification_preferences_request: (required)
        :type update_notification_preferences_request: UpdateNotificationPreferencesRequest
        :return: Returns a dict containing the API Response.
        """  # noqa: E501

        path = "/notifications/preferences/{notification}"
        query_params = {}
        kwargs = kwargs | {"files": {}, "data": {}, "json": {}}

        if notification is not None:
            path = path.replace("{" + "notification" + "}", notification)
        if update_notification_preferences_request is not None:
            kwargs["json"] = update_notification_preferences_request

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
