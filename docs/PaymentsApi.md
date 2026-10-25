# accounting_sh.PaymentsApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_payment**](PaymentsApi.md#add_payment) | **POST** /expenses/payments | Add a payment
[**delete_payment**](PaymentsApi.md#delete_payment) | **DELETE** /expenses/payments/{uuid} | Delete a payment
[**get_payment**](PaymentsApi.md#get_payment) | **GET** /expenses/payments/{uuid} | Get a payment
[**list_payments**](PaymentsApi.md#list_payments) | **GET** /expenses/payments | List company&#39;s payments
[**update_payment**](PaymentsApi.md#update_payment) | **PUT** /expenses/payments/{uuid} | Update a payment


# **add_payment**
> add_payment(add_payment_request)

Add a payment

Add a payment. Send the resource fields in the request body; the response contains the saved record. Requires at least one permission: `add.payment`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_payment_request = accounting_sh.AddPaymentRequest() # AddPaymentRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Add a payment
    api_response = accounting.payments_api.add_payment(add_payment_request)
    print("The response of PaymentsApi->add_payment:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->add_payment: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_payment_request** | [**AddPaymentRequest**](AddPaymentRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**AddPayment200Response**](AddPayment200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**400** | The request failed validation or could not be processed. Inspect errors, correct the input, and try again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_payment**
> delete_payment(uuid)

Delete a payment

Delete a payment. This action deletes the selected record. Review references to it before deletion. Requires at least one permission: `delete.payment`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The payment uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete a payment
    api_response = accounting.payments_api.delete_payment(uuid)
    print("The response of PaymentsApi->delete_payment:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->delete_payment: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The payment uuid | 

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

# **get_payment**
> get_payment(uuid)

Get a payment

Get a payment. Use the identifier returned by the corresponding list or create operation. Requires at least one permission: `view.payment`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The payment uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a payment
    api_response = accounting.payments_api.get_payment(uuid)
    print("The response of PaymentsApi->get_payment:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->get_payment: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The payment uuid | 

### Return type

[**AddPayment200Response**](AddPayment200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_payments**
> list_payments(fields=fields, page=page, per_page=per_page, order_by=order_by)

List company's payments

List company's payments. Retrieve records using the query parameters below. Requires at least one permission: `list.payments`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = 'uuid,amount,currency,contact' # str | Comma-separated fields to include in each record. Default fields: uuid, amount, currency, contact. (optional)
page = 1 # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10 # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = 'created_at:desc' # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's payments
    api_response = accounting.payments_api.list_payments(fields=fields, page=page, per_page=per_page, order_by=order_by)
    print("The response of PaymentsApi->list_payments:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->list_payments: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Comma-separated fields to include in each record. Default fields: uuid, amount, currency, contact. | [optional] 
 **page** | **int**| Page number, starting at 1. Values below 1 are treated as 1. | [optional] [default to 1]
 **per_page** | **int**| Records per page. The server caps page size to 100. Values below 1 use that maximum. | [optional] [default to 10]
 **order_by** | **str**| Sort by a supported field and direction, using field:asc or field:desc. | [optional] 

### Return type

[**ListPayments200Response**](ListPayments200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_payment**
> update_payment(uuid, add_payment_request)

Update a payment

Update a payment. Send the fields accepted by this operation in the request body. Requires at least one permission: `edit.payment`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The payment uuid
add_payment_request = accounting_sh.AddPaymentRequest() # AddPaymentRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a payment
    api_response = accounting.payments_api.update_payment(uuid, add_payment_request)
    print("The response of PaymentsApi->update_payment:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->update_payment: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The payment uuid | 
 **add_payment_request** | [**AddPaymentRequest**](AddPaymentRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**AddPayment200Response**](AddPayment200Response.md)

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

