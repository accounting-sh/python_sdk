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

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_contact_request = accounting_sh.AddContactRequest() # AddContactRequest | 

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
 **add_contact_request** | [**AddContactRequest**](AddContactRequest.md)|  | 

### Return type

[**AddContact200Response**](AddContact200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contact**
> delete_contact(uuid)

Delete a contact

### Example

* Bearer (Api Key) Authentication (bearer):

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

# **get_contact**
> get_contact(uuid)

Retrieve a contact

### Example

* Bearer (Api Key) Authentication (bearer):

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
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_contact_bills**
> list_contact_bills(uuid=uuid, fields=fields, page=page, per_page=per_page)

List a contact's bills

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The contact uuid (optional)
fields = 'fields_example' # str | A comma separated list of fields requested in the response (optional)
page = 'page_example' # str | The response page (optional)
per_page = 'per_page_example' # str | The number of items per page (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List a contact's bills
    api_response = accounting.contacts_api.list_contact_bills(uuid=uuid, fields=fields, page=page, per_page=per_page)
    print("The response of ContactsApi->list_contact_bills:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->list_contact_bills: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The contact uuid | [optional] 
 **fields** | **str**| A comma separated list of fields requested in the response | [optional] 
 **page** | **str**| The response page | [optional] 
 **per_page** | **str**| The number of items per page | [optional] 

### Return type

[**ListContactBills200Response**](ListContactBills200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_contact_invoices**
> list_contact_invoices(uuid, fields=fields, page=page, per_page=per_page)

List a contact's invoices

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The contact uuid
fields = 'fields_example' # str | A comma separated list of fields requested in the response (optional)
page = 'page_example' # str | The response page (optional)
per_page = 'per_page_example' # str | The number of items per page (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List a contact's invoices
    api_response = accounting.contacts_api.list_contact_invoices(uuid, fields=fields, page=page, per_page=per_page)
    print("The response of ContactsApi->list_contact_invoices:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->list_contact_invoices: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The contact uuid | 
 **fields** | **str**| A comma separated list of fields requested in the response | [optional] 
 **page** | **str**| The response page | [optional] 
 **per_page** | **str**| The number of items per page | [optional] 

### Return type

[**ListContactInvoices200Response**](ListContactInvoices200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_contacts**
> list_contacts(fields=fields, page=page, per_page=per_page)

List company's contacts

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
    # List company's contacts
    api_response = accounting.contacts_api.list_contacts(fields=fields, page=page, per_page=per_page)
    print("The response of ContactsApi->list_contacts:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->list_contacts: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| A comma separated list of fields requested in the response | [optional] 
 **page** | **str**| The response page | [optional] 
 **per_page** | **str**| The number of items per page | [optional] 

### Return type

[**ListContacts200Response**](ListContacts200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_contact**
> update_contact(uuid, add_contact_request)

Update a contact

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The contact uuid
add_contact_request = accounting_sh.AddContactRequest() # AddContactRequest | 

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
 **add_contact_request** | [**AddContactRequest**](AddContactRequest.md)|  | 

### Return type

[**AddContact200Response**](AddContact200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

