# accounting_sh.BillsApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_bill**](BillsApi.md#add_bill) | **POST** /expenses/bills | Add a bill
[**add_bill_payment**](BillsApi.md#add_bill_payment) | **POST** /expenses/bills/{uuid}/payments | Add a bill payment
[**delete_bill**](BillsApi.md#delete_bill) | **DELETE** /expenses/bills/{uuid} | Delete a bill
[**get_bill**](BillsApi.md#get_bill) | **GET** /expenses/bills/{uuid} | Get a bill
[**get_bill_document**](BillsApi.md#get_bill_document) | **GET** /expenses/bills/{uuid}/document | Get a bill in PDF
[**list_bills**](BillsApi.md#list_bills) | **GET** /expenses/bills | List company&#39;s bills
[**update_bill**](BillsApi.md#update_bill) | **PUT** /expenses/bills/{uuid} | Update a bill
[**update_bill_payment**](BillsApi.md#update_bill_payment) | **PUT** /expenses/bills/{uuid}/payments/{payment} | Update a bill payment


# **add_bill**
> add_bill(add_bill_request)

Add a bill

Add a bill. Send the resource fields in the request body; the response contains the saved record. Requires at least one permission: `add.bill`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_bill_request = accounting_sh.AddBillRequest() # AddBillRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Add a bill
    api_response = accounting.bills_api.add_bill(add_bill_request)
    print("The response of BillsApi->add_bill:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillsApi->add_bill: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_bill_request** | [**AddBillRequest**](AddBillRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**AddBill200Response**](AddBill200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**400** | The request failed validation or could not be processed. Inspect errors, correct the input, and try again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_bill_payment**
> add_bill_payment(uuid, add_bill_payment_request)

Add a bill payment

Add a bill payment. Use the parameters and response fields below for this operation. Requires at least one permission: `add.invoice.payment`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The bill uuid
add_bill_payment_request = accounting_sh.AddBillPaymentRequest() # AddBillPaymentRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Add a bill payment
    api_response = accounting.bills_api.add_bill_payment(uuid, add_bill_payment_request)
    print("The response of BillsApi->add_bill_payment:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillsApi->add_bill_payment: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The bill uuid | 
 **add_bill_payment_request** | [**AddBillPaymentRequest**](AddBillPaymentRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**GetBill200Response**](GetBill200Response.md)

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

# **delete_bill**
> delete_bill(uuid)

Delete a bill

Delete a bill. This action deletes the selected record. Review references to it before deletion. Requires at least one permission: `delete.bill`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The bill uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete a bill
    api_response = accounting.bills_api.delete_bill(uuid)
    print("The response of BillsApi->delete_bill:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillsApi->delete_bill: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The bill uuid | 

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

# **get_bill**
> get_bill(uuid)

Get a bill

Get a bill. Use the identifier returned by the corresponding list or create operation. Requires at least one permission: `view.bill`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The bill uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a bill
    api_response = accounting.bills_api.get_bill(uuid)
    print("The response of BillsApi->get_bill:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillsApi->get_bill: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The bill uuid | 

### Return type

[**GetBill200Response**](GetBill200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bill_document**
> get_bill_document(uuid)

Get a bill in PDF

Retrieve the generated PDF for this record. HTTP 200 returns application/pdf. If generation is still pending, HTTP 202 returns JSON with success=false and an explanation; retry later. Requires at least one permission: `regenerate.invoice`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The invoice uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a bill in PDF
    api_response = accounting.bills_api.get_bill_document(uuid)
    print("The response of BillsApi->get_bill_document:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillsApi->get_bill_document: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The invoice uuid | 

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

# **list_bills**
> list_bills(fields=fields, page=page, per_page=per_page, order_by=order_by)

List company's bills

List company's bills. Retrieve records using the query parameters below. Requires at least one permission: `list.bills`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = 'uuid,contact,bill_number,status' # str | Comma-separated fields to include in each record. Default fields: uuid, contact, bill_number, status. (optional)
page = 1 # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10 # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = 'created_at:desc' # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's bills
    api_response = accounting.bills_api.list_bills(fields=fields, page=page, per_page=per_page, order_by=order_by)
    print("The response of BillsApi->list_bills:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillsApi->list_bills: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Comma-separated fields to include in each record. Default fields: uuid, contact, bill_number, status. | [optional] 
 **page** | **int**| Page number, starting at 1. Values below 1 are treated as 1. | [optional] [default to 1]
 **per_page** | **int**| Records per page. The server caps page size to 100. Values below 1 use that maximum. | [optional] [default to 10]
 **order_by** | **str**| Sort by a supported field and direction, using field:asc or field:desc. | [optional] 

### Return type

[**ListBills200Response**](ListBills200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bill**
> update_bill(uuid, update_bill_request)

Update a bill

Update a bill. Send the fields accepted by this operation in the request body. Requires at least one permission: `edit.bill`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The bill uuid
update_bill_request = accounting_sh.UpdateBillRequest() # UpdateBillRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a bill
    api_response = accounting.bills_api.update_bill(uuid, update_bill_request)
    print("The response of BillsApi->update_bill:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillsApi->update_bill: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The bill uuid | 
 **update_bill_request** | [**UpdateBillRequest**](UpdateBillRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**GetBill200Response**](GetBill200Response.md)

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

# **update_bill_payment**
> update_bill_payment(uuid, payment, add_bill_payment_request)

Update a bill payment

Update a bill payment. Send the fields accepted by this operation in the request body. Requires at least one permission: `edit.invoice.revenues`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The bill uuid
payment = 'payment_example' # str | The bill payment uuid
add_bill_payment_request = accounting_sh.AddBillPaymentRequest() # AddBillPaymentRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a bill payment
    api_response = accounting.bills_api.update_bill_payment(uuid, payment, add_bill_payment_request)
    print("The response of BillsApi->update_bill_payment:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillsApi->update_bill_payment: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The bill uuid | 
 **payment** | **str**| The bill payment uuid | 
 **add_bill_payment_request** | [**AddBillPaymentRequest**](AddBillPaymentRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**GetBill200Response**](GetBill200Response.md)

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

