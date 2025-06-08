# accounting_sh.TransfersApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_transfer**](TransfersApi.md#add_transfer) | **POST** /transfers | Add a transfer
[**delete_transfer**](TransfersApi.md#delete_transfer) | **DELETE** /transfers/{uuid} | Delete a transfer
[**get_transfer**](TransfersApi.md#get_transfer) | **GET** /transfers/{uuid} | Get a transfer
[**list_transfers**](TransfersApi.md#list_transfers) | **GET** /transfers | List company&#39;s transfers
[**update_transfer**](TransfersApi.md#update_transfer) | **PUT** /transfers/{uuid} | Update a transfer


# **add_transfer**
> add_transfer(add_transfer_request)

Add a transfer

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_transfer_request = accounting_sh.AddTransferRequest() # AddTransferRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Add a transfer
    api_response = accounting.transfers_api.add_transfer(add_transfer_request)
    print("The response of TransfersApi->add_transfer:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransfersApi->add_transfer: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_transfer_request** | [**AddTransferRequest**](AddTransferRequest.md)|  | 

### Return type

[**AddTransfer200Response**](AddTransfer200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_transfer**
> delete_transfer(uuid)

Delete a transfer

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The transfer uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete a transfer
    api_response = accounting.transfers_api.delete_transfer(uuid)
    print("The response of TransfersApi->delete_transfer:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransfersApi->delete_transfer: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The transfer uuid | 

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

# **get_transfer**
> get_transfer(uuid)

Get a transfer

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The transfer uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a transfer
    api_response = accounting.transfers_api.get_transfer(uuid)
    print("The response of TransfersApi->get_transfer:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransfersApi->get_transfer: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The transfer uuid | 

### Return type

[**AddTransfer200Response**](AddTransfer200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transfers**
> list_transfers(fields=fields, page=page, per_page=per_page)

List company's transfers

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
    # List company's transfers
    api_response = accounting.transfers_api.list_transfers(fields=fields, page=page, per_page=per_page)
    print("The response of TransfersApi->list_transfers:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransfersApi->list_transfers: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| A comma separated list of fields requested in the response | [optional] 
 **page** | **str**| The response page | [optional] 
 **per_page** | **str**| The number of items per page | [optional] 

### Return type

[**ListTransfers200Response**](ListTransfers200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_transfer**
> update_transfer(uuid, add_transfer_request)

Update a transfer

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The transfer uuid
add_transfer_request = accounting_sh.AddTransferRequest() # AddTransferRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a transfer
    api_response = accounting.transfers_api.update_transfer(uuid, add_transfer_request)
    print("The response of TransfersApi->update_transfer:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransfersApi->update_transfer: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The transfer uuid | 
 **add_transfer_request** | [**AddTransferRequest**](AddTransferRequest.md)|  | 

### Return type

[**AddTransfer200Response**](AddTransfer200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

