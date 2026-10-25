# accounting_sh.DocumentsApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_document**](DocumentsApi.md#delete_document) | **DELETE** /documents/{uuid} | Delete a document
[**get_document**](DocumentsApi.md#get_document) | **GET** /documents/{uuid} | Get a document
[**list_documents**](DocumentsApi.md#list_documents) | **GET** /documents | List company&#39;s documents
[**process_document**](DocumentsApi.md#process_document) | **GET** /documents/{uuid}/process | Process a document
[**review_document_retention**](DocumentsApi.md#review_document_retention) | **PUT** /documents/{uuid}/retention | Review accounting retention or a legal hold
[**update_document**](DocumentsApi.md#update_document) | **PUT** /documents/{uuid} | Update a document
[**upload_document**](DocumentsApi.md#upload_document) | **POST** /documents | Upload a document
[**view_document**](DocumentsApi.md#view_document) | **GET** /documents/{uuid}/view | View a document


# **delete_document**
> delete_document(uuid)

Delete a document

Delete a document. This action deletes the selected record. Review references to it before deletion. Requires at least one permission: `delete.document`.

### Example

* Bearer (API key) Authentication (bearer):

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

[**ImportAccountTransactions202Response**](ImportAccountTransactions202Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**409** | Accounting evidence is retained or held; the requested mutation is blocked. |  -  |
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document**
> get_document(uuid)

Get a document

Get a document. Use the identifier returned by the corresponding list or create operation. Requires at least one permission: `view.document`.

### Example

* Bearer (API key) Authentication (bearer):

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
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_documents**
> list_documents(fields=fields, page=page, per_page=per_page, order_by=order_by)

List company's documents

List company's documents. Retrieve records using the query parameters below. Requires at least one permission: `list.documents`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = 'uuid,name,mimetype' # str | Comma-separated fields to include in each record. Default fields: uuid, name, mimetype. (optional)
page = 1 # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10 # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = 'created_at:desc' # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's documents
    api_response = accounting.documents_api.list_documents(fields=fields, page=page, per_page=per_page, order_by=order_by)
    print("The response of DocumentsApi->list_documents:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->list_documents: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Comma-separated fields to include in each record. Default fields: uuid, name, mimetype. | [optional] 
 **page** | **int**| Page number, starting at 1. Values below 1 are treated as 1. | [optional] [default to 1]
 **per_page** | **int**| Records per page. The server caps page size to 100. Values below 1 use that maximum. | [optional] [default to 10]
 **order_by** | **str**| Sort by a supported field and direction, using field:asc or field:desc. | [optional] 

### Return type

[**ListDocuments200Response**](ListDocuments200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_document**
> process_document(uuid)

Process a document

Queue background processing of the uploaded document. A successful response acknowledges the queued job, not completed extraction. Already processed documents return 400. This GET starts work; avoid automatic retries. Requires at least one permission: `process.document`.

### Example

* Bearer (API key) Authentication (bearer):

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

[**ImportAccountTransactions202Response**](ImportAccountTransactions202Response.md)

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

# **review_document_retention**
> review_document_retention(uuid, review_document_retention_request)

Review accounting retention or a legal hold

Review the accounting anchor, retention category or legal hold. This cannot shorten existing protection or change the frozen jurisdiction. Send hold=null explicitly to release a hold. Requires permission: `manage.document.retention`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | 
review_document_retention_request = accounting_sh.ReviewDocumentRetentionRequest() # ReviewDocumentRetentionRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Review accounting retention or a legal hold
    api_response = accounting.documents_api.review_document_retention(uuid, review_document_retention_request)
    print("The response of DocumentsApi->review_document_retention:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->review_document_retention: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **review_document_retention_request** | [**ReviewDocumentRetentionRequest**](ReviewDocumentRetentionRequest.md)|  | 

### Return type

[**ReviewDocumentRetention200Response**](ReviewDocumentRetention200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retention reviewed |  -  |
**400** | Invalid accounting anchor or review |  -  |
**403** | Retention management permission required |  -  |
**404** | Document not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_document**
> update_document(uuid, update_document_request)

Update a document

Update a document. Send the fields accepted by this operation in the request body. Requires at least one permission: `edit.document`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The document uuid
update_document_request = accounting_sh.UpdateDocumentRequest() # UpdateDocumentRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

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
 **update_document_request** | [**UpdateDocumentRequest**](UpdateDocumentRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**UploadDocument200Response**](UploadDocument200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**400** | The request failed validation or could not be processed. Inspect errors, correct the input, and try again. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_document**
> upload_document(name, file)

Upload a document

Upload a document. Send the resource fields in the request body; the response contains the saved record. Requires at least one permission: `add.document`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

name = 'name_example' # str | Human-readable name or label.
file = None # bytearray | File to upload. Send this field as a file part in a multipart/form-data request.

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
 **name** | **str**| Human-readable name or label. | 
 **file** | **bytearray**| File to upload. Send this field as a file part in a multipart/form-data request. | 

### Return type

[**UploadDocument200Response**](UploadDocument200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**400** | The request failed validation or could not be processed. Inspect errors, correct the input, and try again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_document**
> view_document(uuid)

View a document

Download the stored document content. The response is a file, rather than a JSON resource envelope. Requires at least one permission: `view.document`.

### Example

* Bearer (API key) Authentication (bearer):

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
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

