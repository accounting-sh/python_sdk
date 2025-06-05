# accounting_sh.DocumentsApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_review**](DocumentsApi.md#cancel_review) | **DELETE** /documents/{uuid}/review | Cancel document review
[**delete_document**](DocumentsApi.md#delete_document) | **DELETE** /documents/{uuid} | Delete a document
[**get_document**](DocumentsApi.md#get_document) | **GET** /documents/{uuid} | Get a document
[**list_documents**](DocumentsApi.md#list_documents) | **GET** /documents | List company&#39;s documents
[**process_document**](DocumentsApi.md#process_document) | **GET** /documents/{uuid}/process | Process a document
[**review_url**](DocumentsApi.md#review_url) | **GET** /documents/{uuid}/review | Get url to review a document
[**update_document**](DocumentsApi.md#update_document) | **PUT** /documents/{uuid} | Update a document
[**upload_document**](DocumentsApi.md#upload_document) | **POST** /documents | Upload a document
[**view_document**](DocumentsApi.md#view_document) | **GET** /documents/{uuid}/view | View a document


# **cancel_review**
> cancel_review(uuid)

Cancel document review

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The document uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Cancel document review
    api_response = accounting.documents_api.cancel_review(uuid)
    print("The response of DocumentsApi->cancel_review:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->cancel_review: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The document uuid | 

### Return type

[**AuthInit200Response**](AuthInit200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_document**
> delete_document(uuid)

Delete a document

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The document uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete a document
    api_response = accounting.documents_api.delete_document(uuid)
    print("The response of DocumentsApi->delete_document:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->delete_document: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The document uuid | 

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

# **get_document**
> get_document(uuid)

Get a document

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The document uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a document
    api_response = accounting.documents_api.get_document(uuid)
    print("The response of DocumentsApi->get_document:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->get_document: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The document uuid | 

### Return type

[**UploadDocument200Response**](UploadDocument200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_documents**
> list_documents(fields=fields, page=page, per_page=per_page)

List company's documents

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
    # List company's documents
    api_response = accounting.documents_api.list_documents(fields=fields, page=page, per_page=per_page)
    print("The response of DocumentsApi->list_documents:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->list_documents: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| A comma separated list of fields requested in the response | [optional] 
 **page** | **str**| The response page | [optional] 
 **per_page** | **str**| The number of items per page | [optional] 

### Return type

[**ListDocuments200Response**](ListDocuments200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_document**
> process_document(uuid)

Process a document

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The document uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Process a document
    api_response = accounting.documents_api.process_document(uuid)
    print("The response of DocumentsApi->process_document:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->process_document: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The document uuid | 

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

# **review_url**
> review_url(uuid)

Get url to review a document

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The document uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get url to review a document
    api_response = accounting.documents_api.review_url(uuid)
    print("The response of DocumentsApi->review_url:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->review_url: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The document uuid | 

### Return type

[**AuthInit200Response**](AuthInit200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_document**
> update_document(uuid, update_document_request)

Update a document

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The document uuid
update_document_request = accounting_sh.UpdateDocumentRequest() # UpdateDocumentRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a document
    api_response = accounting.documents_api.update_document(uuid, update_document_request)
    print("The response of DocumentsApi->update_document:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->update_document: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The document uuid | 
 **update_document_request** | [**UpdateDocumentRequest**](UpdateDocumentRequest.md)|  | 

### Return type

[**UploadDocument200Response**](UploadDocument200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_document**
> upload_document(name, file)

Upload a document

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

name = 'name_example' # str | 
file = None # bytearray | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Upload a document
    api_response = accounting.documents_api.upload_document(name, file)
    print("The response of DocumentsApi->upload_document:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->upload_document: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **file** | [**bytearray**](bytearray.md)|  | 

### Return type

[**UploadDocument200Response**](UploadDocument200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_document**
> view_document(uuid)

View a document

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The document uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # View a document
   accounting.documents_api.view_document(uuid)
except ApiException as e:
    print("Exception when calling DocumentsApi->view_document: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The document uuid | 

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

