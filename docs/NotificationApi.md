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

### Example

* Bearer (Api Key) Authentication (bearer):

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
**200** | Success |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_notifications**
> list_notifications(fields=fields, page=page, per_page=per_page)

List company's notifications

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = 'fields_example' # str | A comma separated list of fields requested in the response (optional)
page = 'page_example' # str | The response page (optional)
per_page = 'per_page_example' # str | The number of items per page (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's notifications
    api_response = accounting.notification_api.list_notifications(fields=fields, page=page, per_page=per_page)
    print("The response of NotificationApi->list_notifications:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->list_notifications: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| A comma separated list of fields requested in the response | [optional] 
 **page** | **str**| The response page | [optional] 
 **per_page** | **str**| The number of items per page | [optional] 

### Return type

[**ListNotifications200Response**](ListNotifications200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_notification**
> send_notification(send_notification_request)

Send a notification

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

send_notification_request = accounting_sh.SendNotificationRequest() # SendNotificationRequest | 

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
 **send_notification_request** | [**SendNotificationRequest**](SendNotificationRequest.md)|  | 

### Return type

[**DeleteAccountConnection200Response**](DeleteAccountConnection200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_notification_preferences**
> update_notification_preferences(notification, update_notification_preferences_request)

Update notification preferences

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

notification = 'notification_example' # str | The notification name
update_notification_preferences_request = accounting_sh.UpdateNotificationPreferencesRequest() # UpdateNotificationPreferencesRequest | 

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
 **update_notification_preferences_request** | [**UpdateNotificationPreferencesRequest**](UpdateNotificationPreferencesRequest.md)|  | 

### Return type

[**ListNotificationPreferences200Response**](ListNotificationPreferences200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

