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

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_attachment_request = accounting_sh.AddAttachmentRequest() # AddAttachmentRequest | 

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
 **add_attachment_request** | [**AddAttachmentRequest**](AddAttachmentRequest.md)|  | 

### Return type

[**AddAttachment200Response**](AddAttachment200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_attachment**
> delete_attachment(uuid)

Delete an attachment

### Example

* Bearer (Api Key) Authentication (bearer):

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

# **get_attachment**
> get_attachment(uuid)

Get an attachment

### Example

* Bearer (Api Key) Authentication (bearer):

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
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_attachments**
> list_attachments(fields=fields, page=page, per_page=per_page)

List company's attachments

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
    # List company's attachments
    api_response = accounting.attachments_api.list_attachments(fields=fields, page=page, per_page=per_page)
    print("The response of AttachmentsApi->list_attachments:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentsApi->list_attachments: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| A comma separated list of fields requested in the response | [optional] 
 **page** | **str**| The response page | [optional] 
 **per_page** | **str**| The number of items per page | [optional] 

### Return type

[**ListAttachments200Response**](ListAttachments200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_attachments**
> retrieve_attachments(resource, fields=fields, page=page, per_page=per_page)

List company's attachments link to resource

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

resource = 'resource_example' # str | The resource
fields = 'fields_example' # str | A comma separated list of fields requested in the response (optional)
page = 'page_example' # str | The response page (optional)
per_page = 'per_page_example' # str | The number of items per page (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's attachments link to resource
    api_response = accounting.attachments_api.retrieve_attachments(resource, fields=fields, page=page, per_page=per_page)
    print("The response of AttachmentsApi->retrieve_attachments:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentsApi->retrieve_attachments: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**| The resource | 
 **fields** | **str**| A comma separated list of fields requested in the response | [optional] 
 **page** | **str**| The response page | [optional] 
 **per_page** | **str**| The number of items per page | [optional] 

### Return type

[**ListAttachments200Response**](ListAttachments200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_attachment**
> update_attachment(uuid, add_attachment_request)

Update an attachment

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The attachment uuid
add_attachment_request = accounting_sh.AddAttachmentRequest() # AddAttachmentRequest | 

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
 **add_attachment_request** | [**AddAttachmentRequest**](AddAttachmentRequest.md)|  | 

### Return type

[**AddAttachment200Response**](AddAttachment200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

