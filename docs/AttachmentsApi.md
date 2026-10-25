# accounting_sh.AttachmentsApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_attachment**](AttachmentsApi.md#add_attachment) | **POST** /attachments | Add an attachment
[**delete_attachment**](AttachmentsApi.md#delete_attachment) | **DELETE** /attachments/{uuid} | Delete an attachment
[**get_attachment**](AttachmentsApi.md#get_attachment) | **GET** /attachments/{uuid} | Get an attachment
[**list_attachments**](AttachmentsApi.md#list_attachments) | **GET** /attachments | List company&#39;s attachments
[**retrieve_attachments**](AttachmentsApi.md#retrieve_attachments) | **GET** /attachments/resource/{resource} | List company&#39;s attachments link to resource
[**update_attachment**](AttachmentsApi.md#update_attachment) | **PUT** /attachments/{uuid} | Update an attachment


# **add_attachment**
> add_attachment(add_attachment_request)

Add an attachment

Add an attachment. Send the resource fields in the request body; the response contains the saved record. Requires at least one permission: `attachment.add`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_attachment_request = accounting_sh.AddAttachmentRequest() # AddAttachmentRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Add an attachment
    api_response = accounting.attachments_api.add_attachment(add_attachment_request)
    print("The response of AttachmentsApi->add_attachment:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentsApi->add_attachment: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_attachment_request** | [**AddAttachmentRequest**](AddAttachmentRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**AddAttachment200Response**](AddAttachment200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**400** | The request failed validation or could not be processed. Inspect errors, correct the input, and try again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_attachment**
> delete_attachment(uuid)

Delete an attachment

Delete an attachment. This action deletes the selected record. Review references to it before deletion. Requires at least one permission: `attachment.delete`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The attachment uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete an attachment
    api_response = accounting.attachments_api.delete_attachment(uuid)
    print("The response of AttachmentsApi->delete_attachment:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentsApi->delete_attachment: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The attachment uuid | 

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

# **get_attachment**
> get_attachment(uuid)

Get an attachment

Get an attachment. Use the identifier returned by the corresponding list or create operation. Requires at least one permission: `attachment.view`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The attachment uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get an attachment
    api_response = accounting.attachments_api.get_attachment(uuid)
    print("The response of AttachmentsApi->get_attachment:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentsApi->get_attachment: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The attachment uuid | 

### Return type

[**AddAttachment200Response**](AddAttachment200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_attachments**
> list_attachments(fields=fields, page=page, per_page=per_page, order_by=order_by)

List company's attachments

List company's attachments. Retrieve records using the query parameters below. Requires at least one permission: `attachment.list`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = 'uuid,document,attached_to' # str | Comma-separated fields to include in each record. Default fields: uuid, document, attached_to. (optional)
page = 1 # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10 # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = 'created_at:desc' # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's attachments
    api_response = accounting.attachments_api.list_attachments(fields=fields, page=page, per_page=per_page, order_by=order_by)
    print("The response of AttachmentsApi->list_attachments:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentsApi->list_attachments: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Comma-separated fields to include in each record. Default fields: uuid, document, attached_to. | [optional] 
 **page** | **int**| Page number, starting at 1. Values below 1 are treated as 1. | [optional] [default to 1]
 **per_page** | **int**| Records per page. The server caps page size to 100. Values below 1 use that maximum. | [optional] [default to 10]
 **order_by** | **str**| Sort by a supported field and direction, using field:asc or field:desc. | [optional] 

### Return type

[**ListAttachments200Response**](ListAttachments200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_attachments**
> retrieve_attachments(resource, fields=fields, page=page, per_page=per_page, order_by=order_by)

List company's attachments link to resource

List company's attachments link to resource. Use the parameters and response fields below for this operation. Requires at least one permission: `attachment.list`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

resource = 'resource_example' # str | The resource
fields = 'uuid,document,attached_to' # str | Comma-separated fields to include in each record. Default fields: uuid, document, attached_to. (optional)
page = 1 # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10 # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = 'created_at:desc' # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's attachments link to resource
    api_response = accounting.attachments_api.retrieve_attachments(resource, fields=fields, page=page, per_page=per_page, order_by=order_by)
    print("The response of AttachmentsApi->retrieve_attachments:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentsApi->retrieve_attachments: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**| The resource | 
 **fields** | **str**| Comma-separated fields to include in each record. Default fields: uuid, document, attached_to. | [optional] 
 **page** | **int**| Page number, starting at 1. Values below 1 are treated as 1. | [optional] [default to 1]
 **per_page** | **int**| Records per page. The server caps page size to 100. Values below 1 use that maximum. | [optional] [default to 10]
 **order_by** | **str**| Sort by a supported field and direction, using field:asc or field:desc. | [optional] 

### Return type

[**ListAttachments200Response**](ListAttachments200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_attachment**
> update_attachment(uuid, add_attachment_request)

Update an attachment

Update an attachment. Send the fields accepted by this operation in the request body. Requires at least one permission: `attachment.edit`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The attachment uuid
add_attachment_request = accounting_sh.AddAttachmentRequest() # AddAttachmentRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update an attachment
    api_response = accounting.attachments_api.update_attachment(uuid, add_attachment_request)
    print("The response of AttachmentsApi->update_attachment:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentsApi->update_attachment: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The attachment uuid | 
 **add_attachment_request** | [**AddAttachmentRequest**](AddAttachmentRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**AddAttachment200Response**](AddAttachment200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**409** | Accounting evidence is retained or held; the requested mutation is blocked. |  -  |
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |
**400** | The request failed validation or could not be processed. Inspect errors, correct the input, and try again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

