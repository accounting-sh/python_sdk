# accounting_sh.AccountConnectionsApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_account_connection**](AccountConnectionsApi.md#delete_account_connection) | **DELETE** /accounts/{uuid}/connect | Delete an account&#39;s connection
[**list_account_connections**](AccountConnectionsApi.md#list_account_connections) | **GET** /accounts/{uuid}/connect | List account&#39;s connections
[**list_banks**](AccountConnectionsApi.md#list_banks) | **GET** /accounts/{uuid}/connect/banks | List available bank connections


# **delete_account_connection**
> delete_account_connection(uuid)

Delete an account's connection

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The account uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete an account's connection
    api_response = accounting.account_connections_api.delete_account_connection(uuid)
    print("The response of AccountConnectionsApi->delete_account_connection:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountConnectionsApi->delete_account_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The account uuid | 

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

# **list_account_connections**
> list_account_connections(uuid, fields=fields, page=page, per_page=per_page)

List account's connections

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The account uuid
fields = 'fields_example' # str | A comma separated list of fields requested in the response (optional)
page = 'page_example' # str | The response page (optional)
per_page = 'per_page_example' # str | The number of items per page (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List account's connections
    api_response = accounting.account_connections_api.list_account_connections(uuid, fields=fields, page=page, per_page=per_page)
    print("The response of AccountConnectionsApi->list_account_connections:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountConnectionsApi->list_account_connections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The account uuid | 
 **fields** | **str**| A comma separated list of fields requested in the response | [optional] 
 **page** | **str**| The response page | [optional] 
 **per_page** | **str**| The number of items per page | [optional] 

### Return type

[**ListAccountConnections200Response**](ListAccountConnections200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_banks**
> list_banks(uuid, country=country)

List available bank connections

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The account uuid
country = 'country_example' # str | A two letter country code, if none are specified, the company's country is used (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List available bank connections
    api_response = accounting.account_connections_api.list_banks(uuid, country=country)
    print("The response of AccountConnectionsApi->list_banks:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountConnectionsApi->list_banks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The account uuid | 
 **country** | **str**| A two letter country code, if none are specified, the company&#39;s country is used | [optional] 

### Return type

[**ListBanks200Response**](ListBanks200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

