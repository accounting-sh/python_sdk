# accounting_sh.CreditNotesApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_credit_note**](CreditNotesApi.md#add_credit_note) | **POST** /incomes/credit-notes | Issue a partial credit note or credit the remaining invoice balance
[**delete_credit_note**](CreditNotesApi.md#delete_credit_note) | **DELETE** /incomes/credit-notes/{uuid} | Issued credit notes cannot be deleted
[**get_credit_note**](CreditNotesApi.md#get_credit_note) | **GET** /incomes/credit-notes/{uuid} | Retrieve an issued credit note
[**get_credit_note_document**](CreditNotesApi.md#get_credit_note_document) | **GET** /incomes/credit-notes/{uuid}/document | Download the immutable credit note PDF
[**list_credit_notes**](CreditNotesApi.md#list_credit_notes) | **GET** /incomes/credit-notes | List this company&#39;s issued credit notes
[**update_credit_note**](CreditNotesApi.md#update_credit_note) | **PUT** /incomes/credit-notes/{uuid} | Issued credit notes cannot be updated


# **add_credit_note**
> add_credit_note(add_credit_note_request)

Issue a partial credit note or credit the remaining invoice balance

Issue an immutable credit note against an issued invoice. Omit items to credit the remaining balance or select original line UUIDs with positive quantities and optional positive net unit prices. Returned credit amounts are negative. replacement=true also creates a replacement draft for a full reversal with no previous credit notes. Requires permission: `correct.invoice`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_credit_note_request = accounting_sh.AddCreditNoteRequest() # AddCreditNoteRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Issue a partial credit note or credit the remaining invoice balance
    api_response = accounting.credit_notes_api.add_credit_note(add_credit_note_request)
    print("The response of CreditNotesApi->add_credit_note:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditNotesApi->add_credit_note: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_credit_note_request** | [**AddCreditNoteRequest**](AddCreditNoteRequest.md)|  | 

### Return type

[**AddCreditNote201Response**](AddCreditNote201Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Credit note issued; PDF generation queued asynchronously. Original invoice and optional replacement draft returned |  -  |
**400** | Invalid request or invoice already credited |  -  |
**404** | Invoice not found |  -  |
**503** | Document issuance unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_credit_note**
> delete_credit_note(uuid)

Issued credit notes cannot be deleted

Issued credit notes are immutable. Returns 404 for unknown or other-company identifiers and 409 for owned issued notes. Requires permission: `correct.invoice`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Issued credit notes cannot be deleted
   accounting.credit_notes_api.delete_credit_note(uuid)
except ApiException as e:
    print("Exception when calling CreditNotesApi->delete_credit_note: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

void (empty response body)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Credit note not found |  -  |
**409** | Issued credit notes are immutable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credit_note**
> get_credit_note(uuid)

Retrieve an issued credit note

Retrieve the frozen credit note and its signed line amounts. Requires permission: `view.invoice`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Retrieve an issued credit note
    api_response = accounting.credit_notes_api.get_credit_note(uuid)
    print("The response of CreditNotesApi->get_credit_note:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditNotesApi->get_credit_note: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**GetCreditNote200Response**](GetCreditNote200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Credit note |  -  |
**404** | Credit note not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credit_note_document**
> get_credit_note_document(uuid)

Download the immutable credit note PDF

Download the archived original PDF after integrity verification; returns HTTP 202 JSON while Async generation is pending. Requires permission: `view.invoice`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Download the immutable credit note PDF
    api_response = accounting.credit_notes_api.get_credit_note_document(uuid)
    print("The response of CreditNotesApi->get_credit_note_document:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditNotesApi->get_credit_note_document: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

**bytearray**

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Original PDF |  -  |
**202** | PDF generation pending; retry later |  -  |
**404** | Credit note not found |  -  |
**503** | Archive integrity check failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_credit_notes**
> list_credit_notes(page=page, per_page=per_page)

List this company's issued credit notes

List issued credit notes for the authenticated company. Pages start at 1, default page size is 10, and page size is clamped to 1–100. Requires permission: `list.invoices`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

page = 56 # int |  (optional)
per_page = 56 # int |  (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List this company's issued credit notes
    api_response = accounting.credit_notes_api.list_credit_notes(page=page, per_page=per_page)
    print("The response of CreditNotesApi->list_credit_notes:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditNotesApi->list_credit_notes: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**ListCreditNotes200Response**](ListCreditNotes200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Company credit notes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_credit_note**
> update_credit_note(uuid)

Issued credit notes cannot be updated

Issued credit notes are immutable. Returns 404 for unknown or other-company identifiers and 409 for owned issued notes. Requires permission: `correct.invoice`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Issued credit notes cannot be updated
   accounting.credit_notes_api.update_credit_note(uuid)
except ApiException as e:
    print("Exception when calling CreditNotesApi->update_credit_note: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

void (empty response body)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Credit note not found |  -  |
**409** | Issued credit notes are immutable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

