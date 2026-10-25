# accounting_sh.SettingsApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_settings**](SettingsApi.md#get_settings) | **GET** /companies/{uuid}/settings/{key} | Get a company&#39;s settings
[**list_settings**](SettingsApi.md#list_settings) | **GET** /companies/{uuid}/settings | List company&#39;s settings
[**update_settings**](SettingsApi.md#update_settings) | **PUT** /companies/{uuid}/settings/{key} | Update a company&#39;s settings


# **get_settings**
> get_settings(uuid, key)

Get a company's settings

Get a company's settings. Use the parameters and response fields below for this operation. Requires at least one permission: `view.company.settings`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The company uuid
key = 'key_example' # str | The setting key

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a company's settings
    api_response = accounting.settings_api.get_settings(uuid, key)
    print("The response of SettingsApi->get_settings:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->get_settings: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The company uuid | 
 **key** | **str**| The setting key | 

### Return type

[**GetSettings200Response**](GetSettings200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_settings**
> list_settings(uuid, fields=fields, page=page, per_page=per_page, order_by=order_by)

List company's settings

List company's settings. Retrieve records using the query parameters below. Requires at least one permission: `list.company.settings`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The company uuid
fields = 'uuid,key,value' # str | Comma-separated fields to include in each record. Default fields: uuid, key, value. (optional)
page = 1 # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10 # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = 'created_at:desc' # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's settings
    api_response = accounting.settings_api.list_settings(uuid, fields=fields, page=page, per_page=per_page, order_by=order_by)
    print("The response of SettingsApi->list_settings:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->list_settings: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The company uuid | 
 **fields** | **str**| Comma-separated fields to include in each record. Default fields: uuid, key, value. | [optional] 
 **page** | **int**| Page number, starting at 1. Values below 1 are treated as 1. | [optional] [default to 1]
 **per_page** | **int**| Records per page. The server caps page size to 100. Values below 1 use that maximum. | [optional] [default to 10]
 **order_by** | **str**| Sort by a supported field and direction, using field:asc or field:desc. | [optional] 

### Return type

[**ListSettings200Response**](ListSettings200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_settings**
> update_settings(uuid, key, update_settings_request)

Update a company's settings

Update a company's settings. Send the fields accepted by this operation in the request body. Requires at least one permission: `edit.company.settings`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The company uuid
key = 'key_example' # str | The setting key
update_settings_request = accounting_sh.UpdateSettingsRequest() # UpdateSettingsRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a company's settings
    api_response = accounting.settings_api.update_settings(uuid, key, update_settings_request)
    print("The response of SettingsApi->update_settings:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->update_settings: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The company uuid | 
 **key** | **str**| The setting key | 
 **update_settings_request** | [**UpdateSettingsRequest**](UpdateSettingsRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**GetSettings200Response**](GetSettings200Response.md)

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

