# accounting_sh.NotificationApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_notification_preferences**](NotificationApi.md#list_notification_preferences) | **GET** /notifications/preferences/{notification} | List notification preferences
[**list_notifications**](NotificationApi.md#list_notifications) | **GET** /notifications | List company&#39;s notifications
[**send_notification**](NotificationApi.md#send_notification) | **POST** /notifications/send | Send a notification
[**update_notification_preferences**](NotificationApi.md#update_notification_preferences) | **PUT** /notifications/preferences/{notification} | Update notification preferences


# **list_notification_preferences**
> list_notification_preferences(notification)

List notification preferences

List notification preferences. Use the parameters and response fields below for this operation. Requires at least one permission: `manage.notification_preferences`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

notification = 'notification_example' # str | The notification name

accounting = accounting_sh.Accounting("access_token")
try:
    # List notification preferences
    api_response = accounting.notification_api.list_notification_preferences(notification)
    print("The response of NotificationApi->list_notification_preferences:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->list_notification_preferences: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification** | **str**| The notification name | 

### Return type

[**ListNotificationPreferences200Response**](ListNotificationPreferences200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_notifications**
> list_notifications(fields=fields, page=page, per_page=per_page, order_by=order_by)

List company's notifications

List company's notifications. Retrieve records using the query parameters below. Requires at least one permission: `list_notification`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = 'uuid,notification' # str | Comma-separated fields to include in each record. Default fields: uuid, notification. (optional)
page = 1 # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10 # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = 'created_at:desc' # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's notifications
    api_response = accounting.notification_api.list_notifications(fields=fields, page=page, per_page=per_page, order_by=order_by)
    print("The response of NotificationApi->list_notifications:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->list_notifications: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Comma-separated fields to include in each record. Default fields: uuid, notification. | [optional] 
 **page** | **int**| Page number, starting at 1. Values below 1 are treated as 1. | [optional] [default to 1]
 **per_page** | **int**| Records per page. The server caps page size to 100. Values below 1 use that maximum. | [optional] [default to 10]
 **order_by** | **str**| Sort by a supported field and direction, using field:asc or field:desc. | [optional] 

### Return type

[**ListNotifications200Response**](ListNotifications200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_notification**
> send_notification(send_notification_request)

Send a notification

Send a notification using the supplied delivery options. This action can contact recipients; avoid automatic retries. Requires at least one permission: `send_notification`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

send_notification_request = accounting_sh.SendNotificationRequest() # SendNotificationRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Send a notification
    api_response = accounting.notification_api.send_notification(send_notification_request)
    print("The response of NotificationApi->send_notification:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->send_notification: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_notification_request** | [**SendNotificationRequest**](SendNotificationRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**ImportAccountTransactions202Response**](ImportAccountTransactions202Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**400** | The request failed validation or could not be processed. Inspect errors, correct the input, and try again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_notification_preferences**
> update_notification_preferences(notification, update_notification_preferences_request)

Update notification preferences

Update notification preferences. Send the fields accepted by this operation in the request body. Omitted optional fields retain their existing values. Requires at least one permission: `manage.notification_preferences`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

notification = 'notification_example' # str | The notification name
update_notification_preferences_request = accounting_sh.UpdateNotificationPreferencesRequest() # UpdateNotificationPreferencesRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update notification preferences
    api_response = accounting.notification_api.update_notification_preferences(notification, update_notification_preferences_request)
    print("The response of NotificationApi->update_notification_preferences:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->update_notification_preferences: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification** | **str**| The notification name | 
 **update_notification_preferences_request** | [**UpdateNotificationPreferencesRequest**](UpdateNotificationPreferencesRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**ListNotificationPreferences200Response**](ListNotificationPreferences200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

