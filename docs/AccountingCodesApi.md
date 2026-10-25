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

Add an accounting code. Send the resource fields in the request body; the response contains the saved record. Requires at least one permission: `accounting_code.add`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_accounting_code_request = accounting_sh.AddAccountingCodeRequest() # AddAccountingCodeRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

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
 **add_accounting_code_request** | [**AddAccountingCodeRequest**](AddAccountingCodeRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**AddAccountingCode200Response**](AddAccountingCode200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**400** | The request failed validation or could not be processed. Inspect errors, correct the input, and try again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_accounting_code**
> delete_accounting_code(uuid)

Delete an accounting code

Delete an accounting code. This action deletes the selected record. Review references to it before deletion. Requires at least one permission: `accounting_code.delete`.

### Example

* Bearer (API key) Authentication (bearer):

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

# **get_accounting_code**
> get_accounting_code(uuid)

Get an accounting code

Get an accounting code. Use the identifier returned by the corresponding list or create operation. Requires at least one permission: `accounting_code.view`.

### Example

* Bearer (API key) Authentication (bearer):

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

[**AddAccountingCode200Response**](AddAccountingCode200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_accounting_codes**
> list_accounting_codes()

List company's accounting code

List company's accounting code. Retrieve records using the query parameters below. Requires at least one permission: `accounting_code.list`.

### Example

* Bearer (API key) Authentication (bearer):

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
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_accounting_code**
> update_accounting_code(uuid, add_accounting_code_request)

Update an accounting code

Update an accounting code. Send the fields accepted by this operation in the request body. Requires at least one permission: `accounting_code.edit`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The accounting code uuid
add_accounting_code_request = accounting_sh.AddAccountingCodeRequest() # AddAccountingCodeRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

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
 **add_accounting_code_request** | [**AddAccountingCodeRequest**](AddAccountingCodeRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**AddAccountingCode200Response**](AddAccountingCode200Response.md)

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

