# accounting_sh.ReceiptsApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_receipt**](ReceiptsApi.md#add_receipt) | **POST** /receipts | Add a receipt
[**delete_receipt**](ReceiptsApi.md#delete_receipt) | **DELETE** /receipts/{uuid} | Delete a receipt
[**get_receipt**](ReceiptsApi.md#get_receipt) | **GET** /receipts/{uuid} | Get a receipt
[**get_receipt_document**](ReceiptsApi.md#get_receipt_document) | **GET** /receipts/{uuid}/document | Get a receipt in PDF
[**list_receipts**](ReceiptsApi.md#list_receipts) | **GET** /receipts | List company&#39;s receipts
[**update_receipt**](ReceiptsApi.md#update_receipt) | **PUT** /receipts/{uuid} | Update a receipt


# **add_receipt**
> add_receipt(add_receipt_request)

Add a receipt

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_receipt_request = accounting_sh.AddReceiptRequest() # AddReceiptRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Add a receipt
    api_response = accounting.receipts_api.add_receipt(add_receipt_request)
    print("The response of ReceiptsApi->add_receipt:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceiptsApi->add_receipt: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_receipt_request** | [**AddReceiptRequest**](AddReceiptRequest.md)|  | 

### Return type

[**AddReceipt200Response**](AddReceipt200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_receipt**
> delete_receipt(uuid)

Delete a receipt

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The receipt uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete a receipt
    api_response = accounting.receipts_api.delete_receipt(uuid)
    print("The response of ReceiptsApi->delete_receipt:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceiptsApi->delete_receipt: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The receipt uuid | 

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

# **get_receipt**
> get_receipt(uuid)

Get a receipt

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The receipt uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a receipt
    api_response = accounting.receipts_api.get_receipt(uuid)
    print("The response of ReceiptsApi->get_receipt:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceiptsApi->get_receipt: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The receipt uuid | 

### Return type

[**AddReceipt200Response**](AddReceipt200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_receipt_document**
> get_receipt_document(uuid)

Get a receipt in PDF

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The receipt uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a receipt in PDF
   accounting.receipts_api.get_receipt_document(uuid)
except ApiException as e:
    print("Exception when calling ReceiptsApi->get_receipt_document: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The receipt uuid | 

### Return type

void (empty response body)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_receipts**
> list_receipts(fields=fields, page=page, per_page=per_page)

List company's receipts

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
    # List company's receipts
    api_response = accounting.receipts_api.list_receipts(fields=fields, page=page, per_page=per_page)
    print("The response of ReceiptsApi->list_receipts:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceiptsApi->list_receipts: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| A comma separated list of fields requested in the response | [optional] 
 **page** | **str**| The response page | [optional] 
 **per_page** | **str**| The number of items per page | [optional] 

### Return type

[**ListReceipts200Response**](ListReceipts200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_receipt**
> update_receipt(uuid, add_receipt_request)

Update a receipt

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The receipt uuid
add_receipt_request = accounting_sh.AddReceiptRequest() # AddReceiptRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a receipt
    api_response = accounting.receipts_api.update_receipt(uuid, add_receipt_request)
    print("The response of ReceiptsApi->update_receipt:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceiptsApi->update_receipt: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The receipt uuid | 
 **add_receipt_request** | [**AddReceiptRequest**](AddReceiptRequest.md)|  | 

### Return type

[**AddReceipt200Response**](AddReceipt200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

