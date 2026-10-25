# accounting_sh.InvoicesApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_invoice**](InvoicesApi.md#add_invoice) | **POST** /incomes/invoices | Add an invoice
[**add_invoice_payment**](InvoicesApi.md#add_invoice_payment) | **POST** /incomes/invoices/{uuid}/payments | Add an invoice payment
[**delete_invoice**](InvoicesApi.md#delete_invoice) | **DELETE** /incomes/invoices/{uuid} | Delete an invoice
[**get_invoice**](InvoicesApi.md#get_invoice) | **GET** /incomes/invoices/{uuid} | Get an invoice
[**get_invoice_document**](InvoicesApi.md#get_invoice_document) | **GET** /incomes/invoices/{uuid}/document | Get an invoice in PDF
[**get_invoice_issuance**](InvoicesApi.md#get_invoice_issuance) | **GET** /incomes/invoices/{uuid}/issuance | Retrieve the immutable source snapshot and original document fingerprints
[**list_invoices**](InvoicesApi.md#list_invoices) | **GET** /incomes/invoices | List company&#39;s invoices
[**list_unpaid_invoices**](InvoicesApi.md#list_unpaid_invoices) | **GET** /incomes/invoices/unpaid | List company&#39;s unpaid invoices
[**update_invoice**](InvoicesApi.md#update_invoice) | **PUT** /incomes/invoices/{uuid} | Update an invoice
[**update_invoice_payment**](InvoicesApi.md#update_invoice_payment) | **PUT** /incomes/invoices/{uuid}/payments/{payment} | Update an invoice payment


# **add_invoice**
> add_invoice(add_invoice_request)

Add an invoice

Create an invoice. Send status=draft to keep it editable with a temporary draft reference. The default status is received and triggers issuance, allocating a legal number and freezing invoice facts and original documents. French issuance requires resolved supply, buyer and VAT particulars. UK foreign-currency invoices retain sterling VAT conversion evidence. Requires at least one permission: `add.invoice`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_invoice_request = accounting_sh.AddInvoiceRequest() # AddInvoiceRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

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
 **add_invoice_request** | [**AddInvoiceRequest**](AddInvoiceRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**AddInvoice200Response**](AddInvoice200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**503** | Issuance, archival, persistence or required HMRC rate data is unavailable. Inspect errors before retrying. |  -  |
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**400** | The request failed validation or could not be processed. Inspect errors, correct the input, and try again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_invoice_payment**
> add_invoice_payment(uuid, add_bill_payment_request)

Add an invoice payment

Add an invoice payment. Use the parameters and response fields below for this operation. Requires at least one permission: `add.invoice.payment`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The invoice uuid
add_bill_payment_request = accounting_sh.AddBillPaymentRequest() # AddBillPaymentRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

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
 **add_bill_payment_request** | [**AddBillPaymentRequest**](AddBillPaymentRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**AddInvoice200Response**](AddInvoice200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**503** | Issuance, archival, persistence or required HMRC rate data is unavailable. Inspect errors before retrying. |  -  |
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |
**400** | The request failed validation or could not be processed. Inspect errors, correct the input, and try again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_invoice**
> delete_invoice(uuid)

Delete an invoice

Delete an unissued draft. Issued invoices cannot be deleted; use a credit note to correct them. Requires at least one permission: `invoice.delete`.

### Example

* Bearer (API key) Authentication (bearer):

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

[**ImportAccountTransactions202Response**](ImportAccountTransactions202Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Issued invoices cannot be deleted; only unissued drafts may be removed. |  -  |
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice**
> get_invoice(uuid)

Get an invoice

Get an invoice. Use the identifier returned by the corresponding list or create operation. Requires at least one permission: `view.invoice`.

### Example

* Bearer (API key) Authentication (bearer):

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
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_document**
> get_invoice_document(uuid)

Get an invoice in PDF

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
    # Get an invoice in PDF
    api_response = accounting.invoices_api.get_invoice_document(uuid)
    print("The response of InvoicesApi->get_invoice_document:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_invoice_document: %s\n" % e)

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
**503** | Issuance, archival, persistence or required HMRC rate data is unavailable. Inspect errors before retrying. |  -  |
**200** | Generated PDF document. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |
**202** | Background work is pending. Inspect the JSON response before retrying. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_issuance**
> get_invoice_issuance(uuid)

Retrieve the immutable source snapshot and original document fingerprints

Read the frozen invoice facts, document hashes and archive provenance. Requires permission: `view.invoice`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Retrieve the immutable source snapshot and original document fingerprints
    api_response = accounting.invoices_api.get_invoice_issuance(uuid)
    print("The response of InvoicesApi->get_invoice_issuance:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_invoice_issuance: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**GetInvoiceIssuance200Response**](GetInvoiceIssuance200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Issuance snapshot and archive provenance |  -  |
**404** | Invoice or issuance archive not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_invoices**
> list_invoices(fields=fields, page=page, per_page=per_page, order_by=order_by)

List company's invoices

List company's invoices. Retrieve records using the query parameters below. Requires at least one permission: `list.invoices`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = 'uuid,contact,status,emitted' # str | Comma-separated fields to include in each record. Default fields: uuid, contact, status, emitted. (optional)
page = 1 # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10 # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = 'created_at:desc' # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's invoices
    api_response = accounting.invoices_api.list_invoices(fields=fields, page=page, per_page=per_page, order_by=order_by)
    print("The response of InvoicesApi->list_invoices:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->list_invoices: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Comma-separated fields to include in each record. Default fields: uuid, contact, status, emitted. | [optional] 
 **page** | **int**| Page number, starting at 1. Values below 1 are treated as 1. | [optional] [default to 1]
 **per_page** | **int**| Records per page. The server caps page size to 100. Values below 1 use that maximum. | [optional] [default to 10]
 **order_by** | **str**| Sort by a supported field and direction, using field:asc or field:desc. | [optional] 

### Return type

[**ListInvoices200Response**](ListInvoices200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_unpaid_invoices**
> list_unpaid_invoices()

List company's unpaid invoices

List company's unpaid invoices. Use the parameters and response fields below for this operation. Requires at least one permission: `list.invoices`.

### Example

* Bearer (API key) Authentication (bearer):

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
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_invoice**
> update_invoice(uuid, update_invoice_request)

Update an invoice

Update a draft or replay unchanged issued facts. Issued invoice facts, lines and original documents are immutable; corrections require a credit note. Omit particulars and vat_conversion to retain existing values; supplying particulars replaces the whole object. Requires at least one permission: `edit.invoice`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The invoice uuid
update_invoice_request = accounting_sh.UpdateInvoiceRequest() # UpdateInvoiceRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update an invoice
    api_response = accounting.invoices_api.update_invoice(uuid, update_invoice_request)
    print("The response of InvoicesApi->update_invoice:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->update_invoice: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The invoice uuid | 
 **update_invoice_request** | [**UpdateInvoiceRequest**](UpdateInvoiceRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**AddInvoice200Response**](AddInvoice200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**503** | Issuance, archival, persistence or required HMRC rate data is unavailable. Inspect errors before retrying. |  -  |
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |
**400** | The request failed validation or could not be processed. Inspect errors, correct the input, and try again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_invoice_payment**
> update_invoice_payment(uuid, payment, add_bill_payment_request)

Update an invoice payment

Update an invoice payment. Send the fields accepted by this operation in the request body. Requires at least one permission: `edit.invoice.revenues`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The invoice uuid
payment = 'payment_example' # str | The invoice payment uuid
add_bill_payment_request = accounting_sh.AddBillPaymentRequest() # AddBillPaymentRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

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
 **add_bill_payment_request** | [**AddBillPaymentRequest**](AddBillPaymentRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**AddInvoice200Response**](AddInvoice200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**503** | Issuance, archival, persistence or required HMRC rate data is unavailable. Inspect errors before retrying. |  -  |
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |
**400** | The request failed validation or could not be processed. Inspect errors, correct the input, and try again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

