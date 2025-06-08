# accounting_sh.ExportApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_exports**](ExportApi.md#list_exports) | **GET** /export | List company&#39;s exports
[**request_export**](ExportApi.md#request_export) | **POST** /export | Request an export


# **list_exports**
> list_exports(fields=fields, page=page, per_page=per_page)

List company's exports

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
    # List company's exports
    api_response = accounting.export_api.list_exports(fields=fields, page=page, per_page=per_page)
    print("The response of ExportApi->list_exports:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportApi->list_exports: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| A comma separated list of fields requested in the response | [optional] 
 **page** | **str**| The response page | [optional] 
 **per_page** | **str**| The number of items per page | [optional] 

### Return type

[**ListExports200Response**](ListExports200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_export**
> request_export(request_export_request)

Request an export

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

request_export_request = accounting_sh.RequestExportRequest() # RequestExportRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Request an export
    api_response = accounting.export_api.request_export(request_export_request)
    print("The response of ExportApi->request_export:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportApi->request_export: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_export_request** | [**RequestExportRequest**](RequestExportRequest.md)|  | 

### Return type

[**DeleteAccountConnection200Response**](DeleteAccountConnection200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**400** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

