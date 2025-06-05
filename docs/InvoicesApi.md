# accounting_sh.InvoicesApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_invoice**](InvoicesApi.md#add_invoice) | **POST** /incomes/invoices | Add an invoice
[**add_invoice_payment**](InvoicesApi.md#add_invoice_payment) | **POST** /incomes/invoices/{uuid}/payments | Add an invoice payment
[**delete_invoice**](InvoicesApi.md#delete_invoice) | **DELETE** /incomes/invoices/{uuid} | Delete an invoice
[**get_invoice**](InvoicesApi.md#get_invoice) | **GET** /incomes/invoices/{uuid} | Get an invoice
[**get_invoice_document**](InvoicesApi.md#get_invoice_document) | **GET** /incomes/invoices/{uuid}/document | Get an invoice in PDF
[**list_invoices**](InvoicesApi.md#list_invoices) | **GET** /incomes/invoices | List company&#39;s invoices
[**list_unpaid_invoices**](InvoicesApi.md#list_unpaid_invoices) | **GET** /incomes/invoices/unpaid | List company&#39;s unpaid invoices
[**update_invoice**](InvoicesApi.md#update_invoice) | **PUT** /incomes/invoices/{uuid} | Update an invoice
[**update_invoice_payment**](InvoicesApi.md#update_invoice_payment) | **PUT** /incomes/invoices/{uuid}/payments/{payment} | Update an invoice payment


# **add_invoice**
> add_invoice(add_invoice_request)

Add an invoice

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_invoice_request = accounting_sh.AddInvoiceRequest() # AddInvoiceRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Add an invoice
    api_response = accounting.invoices_api.add_invoice(add_invoice_request)
    print("The response of InvoicesApi->add_invoice:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->add_invoice: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_invoice_request** | [**AddInvoiceRequest**](AddInvoiceRequest.md)|  | 

### Return type

[**AddInvoice200Response**](AddInvoice200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_invoice_payment**
> add_invoice_payment(uuid, add_bill_payment_request)

Add an invoice payment

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The invoice uuid
add_bill_payment_request = accounting_sh.AddBillPaymentRequest() # AddBillPaymentRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Add an invoice payment
    api_response = accounting.invoices_api.add_invoice_payment(uuid, add_bill_payment_request)
    print("The response of InvoicesApi->add_invoice_payment:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->add_invoice_payment: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The invoice uuid | 
 **add_bill_payment_request** | [**AddBillPaymentRequest**](AddBillPaymentRequest.md)|  | 

### Return type

[**AddInvoicePayment200Response**](AddInvoicePayment200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_invoice**
> delete_invoice(uuid)

Delete an invoice

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The invoice uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete an invoice
    api_response = accounting.invoices_api.delete_invoice(uuid)
    print("The response of InvoicesApi->delete_invoice:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->delete_invoice: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The invoice uuid | 

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

# **get_invoice**
> get_invoice(uuid)

Get an invoice

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The invoice uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get an invoice
    api_response = accounting.invoices_api.get_invoice(uuid)
    print("The response of InvoicesApi->get_invoice:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_invoice: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The invoice uuid | 

### Return type

[**AddInvoice200Response**](AddInvoice200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_document**
> get_invoice_document(uuid)

Get an invoice in PDF

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The invoice uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get an invoice in PDF
   accounting.invoices_api.get_invoice_document(uuid)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_invoice_document: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The invoice uuid | 

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

# **list_invoices**
> list_invoices(fields=fields, page=page, per_page=per_page)

List company's invoices

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = 'fields_example' # str | A comma separated list of fields requested in the response (optional)
page = 'page_example' # str | The response page (optional)
per_page = 'per_page_example' # str | The number of items per page (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's invoices
    api_response = accounting.invoices_api.list_invoices(fields=fields, page=page, per_page=per_page)
    print("The response of InvoicesApi->list_invoices:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->list_invoices: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| A comma separated list of fields requested in the response | [optional] 
 **page** | **str**| The response page | [optional] 
 **per_page** | **str**| The number of items per page | [optional] 

### Return type

[**ListInvoices200Response**](ListInvoices200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_unpaid_invoices**
> list_unpaid_invoices()

List company's unpaid invoices

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint


accounting = accounting_sh.Accounting("access_token")
try:
    # List company's unpaid invoices
    api_response = accounting.invoices_api.list_unpaid_invoices()
    print("The response of InvoicesApi->list_unpaid_invoices:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->list_unpaid_invoices: %s\n" % e)

```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListUnpaidInvoices200Response**](ListUnpaidInvoices200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_invoice**
> update_invoice(uuid, add_invoice_request)

Update an invoice

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The invoice uuid
add_invoice_request = accounting_sh.AddInvoiceRequest() # AddInvoiceRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Update an invoice
    api_response = accounting.invoices_api.update_invoice(uuid, add_invoice_request)
    print("The response of InvoicesApi->update_invoice:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->update_invoice: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The invoice uuid | 
 **add_invoice_request** | [**AddInvoiceRequest**](AddInvoiceRequest.md)|  | 

### Return type

[**AddInvoice200Response**](AddInvoice200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_invoice_payment**
> update_invoice_payment(uuid, payment, add_bill_payment_request)

Update an invoice payment

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The invoice uuid
payment = 'payment_example' # str | The invoice payment uuid
add_bill_payment_request = accounting_sh.AddBillPaymentRequest() # AddBillPaymentRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Update an invoice payment
    api_response = accounting.invoices_api.update_invoice_payment(uuid, payment, add_bill_payment_request)
    print("The response of InvoicesApi->update_invoice_payment:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->update_invoice_payment: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The invoice uuid | 
 **payment** | **str**| The invoice payment uuid | 
 **add_bill_payment_request** | [**AddBillPaymentRequest**](AddBillPaymentRequest.md)|  | 

### Return type

[**AddInvoicePayment200Response**](AddInvoicePayment200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

