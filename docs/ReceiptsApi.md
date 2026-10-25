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

Add a receipt. Send the resource fields in the request body; the response contains the saved record. Requires at least one permission: `add.receipt`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_receipt_request = accounting_sh.AddReceiptRequest() # AddReceiptRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

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
 **add_receipt_request** | [**AddReceiptRequest**](AddReceiptRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**AddReceipt200Response**](AddReceipt200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**400** | The request failed validation or could not be processed. Inspect errors, correct the input, and try again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_receipt**
> delete_receipt(uuid)

Delete a receipt

Delete a receipt. This action deletes the selected record. Review references to it before deletion. Requires at least one permission: `receipt.delete`.

### Example

* Bearer (API key) Authentication (bearer):

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

# **get_receipt**
> get_receipt(uuid)

Get a receipt

Get a receipt. Use the identifier returned by the corresponding list or create operation. Requires at least one permission: `view.receipt`.

### Example

* Bearer (API key) Authentication (bearer):

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
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_receipt_document**
> get_receipt_document(uuid)

Get a receipt in PDF

Retrieve the generated PDF for this record. HTTP 200 returns application/pdf. If generation is still pending, HTTP 202 returns JSON with success=false and an explanation; retry later. Requires at least one permission: `regenerate.receipt`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The receipt uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a receipt in PDF
    api_response = accounting.receipts_api.get_receipt_document(uuid)
    print("The response of ReceiptsApi->get_receipt_document:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceiptsApi->get_receipt_document: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The receipt uuid | 

### Return type

**bytearray**

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Generated PDF document. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |
**202** | Background work is pending. Inspect the JSON response before retrying. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_receipts**
> list_receipts(fields=fields, page=page, per_page=per_page, order_by=order_by)

List company's receipts

List company's receipts. Retrieve records using the query parameters below. Requires at least one permission: `list.receipts`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = 'uuid,for,from,receipt_number' # str | Comma-separated fields to include in each record. Default fields: uuid, for, from, receipt_number. (optional)
page = 1 # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10 # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = 'created_at:desc' # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's receipts
    api_response = accounting.receipts_api.list_receipts(fields=fields, page=page, per_page=per_page, order_by=order_by)
    print("The response of ReceiptsApi->list_receipts:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceiptsApi->list_receipts: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Comma-separated fields to include in each record. Default fields: uuid, for, from, receipt_number. | [optional] 
 **page** | **int**| Page number, starting at 1. Values below 1 are treated as 1. | [optional] [default to 1]
 **per_page** | **int**| Records per page. The server caps page size to 100. Values below 1 use that maximum. | [optional] [default to 10]
 **order_by** | **str**| Sort by a supported field and direction, using field:asc or field:desc. | [optional] 

### Return type

[**ListReceipts200Response**](ListReceipts200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_receipt**
> update_receipt(uuid, update_receipt_request)

Update a receipt

Update a receipt. Send the fields accepted by this operation in the request body. Requires at least one permission: `edit.receipt`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The receipt uuid
update_receipt_request = accounting_sh.UpdateReceiptRequest() # UpdateReceiptRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a receipt
    api_response = accounting.receipts_api.update_receipt(uuid, update_receipt_request)
    print("The response of ReceiptsApi->update_receipt:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceiptsApi->update_receipt: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The receipt uuid | 
 **update_receipt_request** | [**UpdateReceiptRequest**](UpdateReceiptRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**AddReceipt200Response**](AddReceipt200Response.md)

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

