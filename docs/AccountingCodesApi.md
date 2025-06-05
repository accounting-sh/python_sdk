# accounting_sh.AccountingCodesApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_accounting_code**](AccountingCodesApi.md#add_accounting_code) | **POST** /accounting/codes | Add an accounting code
[**delete_accounting_code**](AccountingCodesApi.md#delete_accounting_code) | **DELETE** /accounting/codes/{uuid} | Delete an accounting code
[**get_accounting_code**](AccountingCodesApi.md#get_accounting_code) | **GET** /accounting/codes/{uuid} | Get an accounting code
[**list_accounting_codes**](AccountingCodesApi.md#list_accounting_codes) | **GET** /accounting/codes | List company&#39;s accounting code
[**update_accounting_code**](AccountingCodesApi.md#update_accounting_code) | **PUT** /accounting/codes/{uuid} | Update an accounting code


# **add_accounting_code**
> add_accounting_code(add_accounting_code_request)

Add an accounting code

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_accounting_code_request = accounting_sh.AddAccountingCodeRequest() # AddAccountingCodeRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Add an accounting code
    api_response = accounting.accounting_codes_api.add_accounting_code(add_accounting_code_request)
    print("The response of AccountingCodesApi->add_accounting_code:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingCodesApi->add_accounting_code: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_accounting_code_request** | [**AddAccountingCodeRequest**](AddAccountingCodeRequest.md)|  | 

### Return type

[**AddAccountingCode200Response**](AddAccountingCode200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_accounting_code**
> delete_accounting_code(uuid)

Delete an accounting code

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The accounting code uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete an accounting code
    api_response = accounting.accounting_codes_api.delete_accounting_code(uuid)
    print("The response of AccountingCodesApi->delete_accounting_code:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingCodesApi->delete_accounting_code: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The accounting code uuid | 

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

# **get_accounting_code**
> get_accounting_code(uuid)

Get an accounting code

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The accounting code uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get an accounting code
    api_response = accounting.accounting_codes_api.get_accounting_code(uuid)
    print("The response of AccountingCodesApi->get_accounting_code:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingCodesApi->get_accounting_code: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The accounting code uuid | 

### Return type

[**GetAccountingCode200Response**](GetAccountingCode200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_accounting_codes**
> list_accounting_codes()

List company's accounting code

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint


accounting = accounting_sh.Accounting("access_token")
try:
    # List company's accounting code
    api_response = accounting.accounting_codes_api.list_accounting_codes()
    print("The response of AccountingCodesApi->list_accounting_codes:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingCodesApi->list_accounting_codes: %s\n" % e)

```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListAccountingCodes200Response**](ListAccountingCodes200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_accounting_code**
> update_accounting_code(uuid, add_accounting_code_request)

Update an accounting code

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The accounting code uuid
add_accounting_code_request = accounting_sh.AddAccountingCodeRequest() # AddAccountingCodeRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Update an accounting code
    api_response = accounting.accounting_codes_api.update_accounting_code(uuid, add_accounting_code_request)
    print("The response of AccountingCodesApi->update_accounting_code:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingCodesApi->update_accounting_code: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The accounting code uuid | 
 **add_accounting_code_request** | [**AddAccountingCodeRequest**](AddAccountingCodeRequest.md)|  | 

### Return type

[**AddAccountingCode200Response**](AddAccountingCode200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

