# accounting_sh.NotificationTypesApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_notification_type**](NotificationTypesApi.md#add_notification_type) | **POST** /notifications/types | Add a notification type
[**delete_notification_type**](NotificationTypesApi.md#delete_notification_type) | **DELETE** /notifications/types/{uuid} | Delete a notification type
[**get_notification_type**](NotificationTypesApi.md#get_notification_type) | **GET** /notifications/types/{uuid} | Get a notification type
[**list_notification_types**](NotificationTypesApi.md#list_notification_types) | **GET** /notifications/types | List company&#39;s notification types
[**update_notification_type**](NotificationTypesApi.md#update_notification_type) | **PUT** /notifications/types/{uuid} | Update a notification type


# **add_notification_type**
> add_notification_type(add_notification_type_request)

Add a notification type

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_notification_type_request = accounting_sh.AddNotificationTypeRequest() # AddNotificationTypeRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Add a notification type
    api_response = accounting.notification_types_api.add_notification_type(add_notification_type_request)
    print("The response of NotificationTypesApi->add_notification_type:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationTypesApi->add_notification_type: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_notification_type_request** | [**AddNotificationTypeRequest**](AddNotificationTypeRequest.md)|  | 

### Return type

[**AddNotificationType200Response**](AddNotificationType200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_notification_type**
> delete_notification_type(uuid)

Delete a notification type

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The notification type uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete a notification type
    api_response = accounting.notification_types_api.delete_notification_type(uuid)
    print("The response of NotificationTypesApi->delete_notification_type:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationTypesApi->delete_notification_type: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The notification type uuid | 

### Return type

[**DeleteAccountConnection200Response**](DeleteAccountConnection200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_type**
> get_notification_type(uuid)

Get a notification type

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The notification type uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a notification type
    api_response = accounting.notification_types_api.get_notification_type(uuid)
    print("The response of NotificationTypesApi->get_notification_type:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationTypesApi->get_notification_type: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The notification type uuid | 

### Return type

[**AddNotificationType200Response**](AddNotificationType200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_notification_types**
> list_notification_types(fields=fields, page=page, per_page=per_page)

List company's notification types

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
    # List company's notification types
    api_response = accounting.notification_types_api.list_notification_types(fields=fields, page=page, per_page=per_page)
    print("The response of NotificationTypesApi->list_notification_types:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationTypesApi->list_notification_types: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| A comma separated list of fields requested in the response | [optional] 
 **page** | **str**| The response page | [optional] 
 **per_page** | **str**| The number of items per page | [optional] 

### Return type

[**ListNotificationTypes200Response**](ListNotificationTypes200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_notification_type**
> update_notification_type(uuid, add_notification_type_request)

Update a notification type

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The notification type uuid
add_notification_type_request = accounting_sh.AddNotificationTypeRequest() # AddNotificationTypeRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a notification type
    api_response = accounting.notification_types_api.update_notification_type(uuid, add_notification_type_request)
    print("The response of NotificationTypesApi->update_notification_type:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationTypesApi->update_notification_type: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The notification type uuid | 
 **add_notification_type_request** | [**AddNotificationTypeRequest**](AddNotificationTypeRequest.md)|  | 

### Return type

[**AddNotificationType200Response**](AddNotificationType200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

