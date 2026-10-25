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

Add a transfer. Send the resource fields in the request body; the response contains the saved record. Requires at least one permission: `add.transfer`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_transfer_request = accounting_sh.AddTransferRequest() # AddTransferRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

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
 **add_transfer_request** | [**AddTransferRequest**](AddTransferRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**AddTransfer200Response**](AddTransfer200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**400** | The request failed validation or could not be processed. Inspect errors, correct the input, and try again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_transfer**
> delete_transfer(uuid)

Delete a transfer

Delete a transfer. This action deletes the selected record. Review references to it before deletion. Requires at least one permission: `delete.transfer`.

### Example

* Bearer (API key) Authentication (bearer):

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

# **get_transfer**
> get_transfer(uuid)

Get a transfer

Get a transfer. Use the identifier returned by the corresponding list or create operation. Requires at least one permission: `view.transfer`.

### Example

* Bearer (API key) Authentication (bearer):

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
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transfers**
> list_transfers(fields=fields, page=page, per_page=per_page, order_by=order_by)

List company's transfers

List company's transfers. Retrieve records using the query parameters below. Requires at least one permission: `list.transfers`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = 'uuid,from,to,amount' # str | Comma-separated fields to include in each record. Default fields: uuid, from, to, amount. (optional)
page = 1 # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10 # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = 'created_at:desc' # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's transfers
    api_response = accounting.transfers_api.list_transfers(fields=fields, page=page, per_page=per_page, order_by=order_by)
    print("The response of TransfersApi->list_transfers:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransfersApi->list_transfers: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Comma-separated fields to include in each record. Default fields: uuid, from, to, amount. | [optional] 
 **page** | **int**| Page number, starting at 1. Values below 1 are treated as 1. | [optional] [default to 1]
 **per_page** | **int**| Records per page. The server caps page size to 100. Values below 1 use that maximum. | [optional] [default to 10]
 **order_by** | **str**| Sort by a supported field and direction, using field:asc or field:desc. | [optional] 

### Return type

[**ListTransfers200Response**](ListTransfers200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_transfer**
> update_transfer(uuid, add_transfer_request)

Update a transfer

Update a transfer. Send the fields accepted by this operation in the request body. Requires at least one permission: `edit.transfer`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The transfer uuid
add_transfer_request = accounting_sh.AddTransferRequest() # AddTransferRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

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
 **add_transfer_request** | [**AddTransferRequest**](AddTransferRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**AddTransfer200Response**](AddTransfer200Response.md)

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

