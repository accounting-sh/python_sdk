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

### Example


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
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_settings**
> list_settings(fields=fields, page=page, per_page=per_page, uuid=uuid)

List company's settings

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = 'fields_example' # str | A comma separated list of fields requested in the response (optional)
page = 'page_example' # str | The response page (optional)
per_page = 'per_page_example' # str | The number of items per page (optional)
uuid = 'uuid_example' # str | The company uuid (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's settings
    api_response = accounting.settings_api.list_settings(fields=fields, page=page, per_page=per_page, uuid=uuid)
    print("The response of SettingsApi->list_settings:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->list_settings: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| A comma separated list of fields requested in the response | [optional] 
 **page** | **str**| The response page | [optional] 
 **per_page** | **str**| The number of items per page | [optional] 
 **uuid** | **str**| The company uuid | [optional] 

### Return type

[**ListSettings200Response**](ListSettings200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_settings**
> update_settings(uuid, key, update_settings_request)

Update a company's settings

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The company uuid
key = 'key_example' # str | The setting key
update_settings_request = accounting_sh.UpdateSettingsRequest() # UpdateSettingsRequest | 

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
 **update_settings_request** | [**UpdateSettingsRequest**](UpdateSettingsRequest.md)|  | 

### Return type

[**GetSettings200Response**](GetSettings200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

