# accounting_sh.ContactsApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_contact**](ContactsApi.md#add_contact) | **POST** /contacts | Create a new contact
[**delete_contact**](ContactsApi.md#delete_contact) | **DELETE** /contacts/{uuid} | Delete a contact
[**get_contact**](ContactsApi.md#get_contact) | **GET** /contacts/{uuid} | Retrieve a contact
[**list_contact_bills**](ContactsApi.md#list_contact_bills) | **GET** /contacts/{uuid}/bills | List a contact&#39;s bills
[**list_contact_invoices**](ContactsApi.md#list_contact_invoices) | **GET** /contacts/{uuid}/invoices | List a contact&#39;s invoices
[**list_contacts**](ContactsApi.md#list_contacts) | **GET** /contacts | List company&#39;s contacts
[**update_contact**](ContactsApi.md#update_contact) | **PUT** /contacts/{uuid} | Update a contact


# **add_contact**
> add_contact(add_contact_request)

Create a new contact

Create a new contact. Send the resource fields in the request body; the response contains the saved record. Requires at least one permission: `add.contact`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_contact_request = accounting_sh.AddContactRequest() # AddContactRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Create a new contact
    api_response = accounting.contacts_api.add_contact(add_contact_request)
    print("The response of ContactsApi->add_contact:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->add_contact: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_contact_request** | [**AddContactRequest**](AddContactRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**AddContact200Response**](AddContact200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**400** | The request failed validation or could not be processed. Inspect errors, correct the input, and try again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contact**
> delete_contact(uuid)

Delete a contact

Delete a contact. This action deletes the selected record. Review references to it before deletion. Requires at least one permission: `delete.contact`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The contact uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete a contact
    api_response = accounting.contacts_api.delete_contact(uuid)
    print("The response of ContactsApi->delete_contact:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->delete_contact: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The contact uuid | 

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

# **get_contact**
> get_contact(uuid)

Retrieve a contact

Retrieve a contact. Use the identifier returned by the corresponding list or create operation. Requires at least one permission: `view.contact`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The contact uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Retrieve a contact
    api_response = accounting.contacts_api.get_contact(uuid)
    print("The response of ContactsApi->get_contact:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->get_contact: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The contact uuid | 

### Return type

[**AddContact200Response**](AddContact200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_contact_bills**
> list_contact_bills(uuid, fields=fields, page=page, per_page=per_page, order_by=order_by)

List a contact's bills

List a contact's bills. Use the parameters and response fields below for this operation. Requires at least one permission: `list.bills`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The contact uuid
fields = 'uuid,vendor,bill_number,status' # str | Comma-separated fields to include in each record. Default fields: uuid, vendor, bill_number, status. (optional)
page = 1 # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10 # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = 'created_at:desc' # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List a contact's bills
    api_response = accounting.contacts_api.list_contact_bills(uuid, fields=fields, page=page, per_page=per_page, order_by=order_by)
    print("The response of ContactsApi->list_contact_bills:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->list_contact_bills: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The contact uuid | 
 **fields** | **str**| Comma-separated fields to include in each record. Default fields: uuid, vendor, bill_number, status. | [optional] 
 **page** | **int**| Page number, starting at 1. Values below 1 are treated as 1. | [optional] [default to 1]
 **per_page** | **int**| Records per page. The server caps page size to 100. Values below 1 use that maximum. | [optional] [default to 10]
 **order_by** | **str**| Sort by a supported field and direction, using field:asc or field:desc. | [optional] 

### Return type

[**ListContactBills200Response**](ListContactBills200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_contact_invoices**
> list_contact_invoices(uuid, fields=fields, page=page, per_page=per_page, order_by=order_by)

List a contact's invoices

List a contact's invoices. Use the parameters and response fields below for this operation. Requires at least one permission: `list.invoices`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The contact uuid
fields = 'uuid,customer,status,emitted' # str | Comma-separated fields to include in each record. Default fields: uuid, customer, status, emitted. (optional)
page = 1 # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10 # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = 'created_at:desc' # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List a contact's invoices
    api_response = accounting.contacts_api.list_contact_invoices(uuid, fields=fields, page=page, per_page=per_page, order_by=order_by)
    print("The response of ContactsApi->list_contact_invoices:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->list_contact_invoices: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The contact uuid | 
 **fields** | **str**| Comma-separated fields to include in each record. Default fields: uuid, customer, status, emitted. | [optional] 
 **page** | **int**| Page number, starting at 1. Values below 1 are treated as 1. | [optional] [default to 1]
 **per_page** | **int**| Records per page. The server caps page size to 100. Values below 1 use that maximum. | [optional] [default to 10]
 **order_by** | **str**| Sort by a supported field and direction, using field:asc or field:desc. | [optional] 

### Return type

[**ListContactInvoices200Response**](ListContactInvoices200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_contacts**
> list_contacts(fields=fields, page=page, per_page=per_page, order_by=order_by)

List company's contacts

List company's contacts. Retrieve records using the query parameters below. Requires at least one permission: `list.contacts`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = 'uuid,name,prefix,currency,registration_number' # str | Comma-separated fields to include in each record. Default fields: uuid, name, prefix, currency, registration_number. Optional buyer_type is the explicit business/consumer override; null uses automatic inference. (optional)
page = 1 # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10 # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = 'created_at:desc' # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's contacts
    api_response = accounting.contacts_api.list_contacts(fields=fields, page=page, per_page=per_page, order_by=order_by)
    print("The response of ContactsApi->list_contacts:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->list_contacts: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Comma-separated fields to include in each record. Default fields: uuid, name, prefix, currency, registration_number. Optional buyer_type is the explicit business/consumer override; null uses automatic inference. | [optional] 
 **page** | **int**| Page number, starting at 1. Values below 1 are treated as 1. | [optional] [default to 1]
 **per_page** | **int**| Records per page. The server caps page size to 100. Values below 1 use that maximum. | [optional] [default to 10]
 **order_by** | **str**| Sort by a supported field and direction, using field:asc or field:desc. | [optional] 

### Return type

[**ListContacts200Response**](ListContacts200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_contact**
> update_contact(uuid, add_contact_request)

Update a contact

Update a contact. Send the fields accepted by this operation in the request body. Requires at least one permission: `edit.contact`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The contact uuid
add_contact_request = accounting_sh.AddContactRequest() # AddContactRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a contact
    api_response = accounting.contacts_api.update_contact(uuid, add_contact_request)
    print("The response of ContactsApi->update_contact:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->update_contact: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The contact uuid | 
 **add_contact_request** | [**AddContactRequest**](AddContactRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**AddContact200Response**](AddContact200Response.md)

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

