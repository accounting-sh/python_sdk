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

Add a notification type. Send the resource fields in the request body; the response contains the saved record. Requires at least one permission: `add.notification_type`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_notification_type_request = accounting_sh.AddNotificationTypeRequest() # AddNotificationTypeRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

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
 **add_notification_type_request** | [**AddNotificationTypeRequest**](AddNotificationTypeRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**AddNotificationType200Response**](AddNotificationType200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**400** | The request failed validation or could not be processed. Inspect errors, correct the input, and try again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_notification_type**
> delete_notification_type(uuid)

Delete a notification type

Delete a notification type. This action deletes the selected record. Review references to it before deletion. Requires at least one permission: `delete.notification_type`.

### Example

* Bearer (API key) Authentication (bearer):

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

[**ImportAccountTransactions202Response**](ImportAccountTransactions202Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_type**
> get_notification_type(uuid)

Get a notification type

Get a notification type. Use the identifier returned by the corresponding list or create operation. Requires at least one permission: `view.notification_type`.

### Example

* Bearer (API key) Authentication (bearer):

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
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_notification_types**
> list_notification_types(fields=fields, page=page, per_page=per_page, order_by=order_by)

List company's notification types

List company's notification types. Retrieve records using the query parameters below. Requires at least one permission: `list.notification_type`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = 'name,title,description,allowed_methods,internal' # str | Comma-separated fields to include in each record. Default fields: name, title, description, allowed_methods, internal. (optional)
page = 1 # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10 # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = 'created_at:desc' # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's notification types
    api_response = accounting.notification_types_api.list_notification_types(fields=fields, page=page, per_page=per_page, order_by=order_by)
    print("The response of NotificationTypesApi->list_notification_types:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationTypesApi->list_notification_types: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Comma-separated fields to include in each record. Default fields: name, title, description, allowed_methods, internal. | [optional] 
 **page** | **int**| Page number, starting at 1. Values below 1 are treated as 1. | [optional] [default to 1]
 **per_page** | **int**| Records per page. The server caps page size to 100. Values below 1 use that maximum. | [optional] [default to 10]
 **order_by** | **str**| Sort by a supported field and direction, using field:asc or field:desc. | [optional] 

### Return type

[**ListNotificationTypes200Response**](ListNotificationTypes200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_notification_type**
> update_notification_type(uuid, update_notification_type_request)

Update a notification type

Update a notification type. Send the fields accepted by this operation in the request body. Requires at least one permission: `edit.notification_type`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The notification type uuid
update_notification_type_request = accounting_sh.UpdateNotificationTypeRequest() # UpdateNotificationTypeRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a notification type
    api_response = accounting.notification_types_api.update_notification_type(uuid, update_notification_type_request)
    print("The response of NotificationTypesApi->update_notification_type:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationTypesApi->update_notification_type: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The notification type uuid | 
 **update_notification_type_request** | [**UpdateNotificationTypeRequest**](UpdateNotificationTypeRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**AddNotificationType200Response**](AddNotificationType200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |
**400** | The request failed validation or could not be processed. Inspect errors, correct the input, and try again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

