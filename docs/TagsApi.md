# accounting_sh.TagsApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_tag**](TagsApi.md#add_tag) | **POST** /tags | Add a tag
[**delete_tag**](TagsApi.md#delete_tag) | **DELETE** /tags/{uuid} | Delete a tag
[**get_tag**](TagsApi.md#get_tag) | **GET** /tags/{uuid} | Get a tag
[**list_tags**](TagsApi.md#list_tags) | **GET** /tags | List company&#39;s tags
[**list_tags_by_resource**](TagsApi.md#list_tags_by_resource) | **GET** /tags/attachments/{resource} | List company&#39;s tags by resource attachment
[**update_tag**](TagsApi.md#update_tag) | **PUT** /tags/{uuid} | Update a tag


# **add_tag**
> add_tag(add_tag_request)

Add a tag

Add a tag. Send the resource fields in the request body; the response contains the saved record. Requires at least one permission: `add.tag`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_tag_request = accounting_sh.AddTagRequest() # AddTagRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Add a tag
    api_response = accounting.tags_api.add_tag(add_tag_request)
    print("The response of TagsApi->add_tag:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->add_tag: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_tag_request** | [**AddTagRequest**](AddTagRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**AddTag200Response**](AddTag200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**400** | The request failed validation or could not be processed. Inspect errors, correct the input, and try again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tag**
> delete_tag(uuid)

Delete a tag

Delete a tag. This action deletes the selected record. Review references to it before deletion. Requires at least one permission: `delete.tag`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The tag uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete a tag
    api_response = accounting.tags_api.delete_tag(uuid)
    print("The response of TagsApi->delete_tag:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->delete_tag: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The tag uuid | 

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

# **get_tag**
> get_tag(uuid)

Get a tag

Get a tag. Use the identifier returned by the corresponding list or create operation. Requires at least one permission: `view.tag`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The tag uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a tag
    api_response = accounting.tags_api.get_tag(uuid)
    print("The response of TagsApi->get_tag:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->get_tag: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The tag uuid | 

### Return type

[**AddTag200Response**](AddTag200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tags**
> list_tags(fields=fields, page=page, per_page=per_page, order_by=order_by)

List company's tags

List company's tags. Retrieve records using the query parameters below. Requires at least one permission: `list.tags`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = 'uuid,key,value,attached_at' # str | Comma-separated fields to include in each record. Default fields: uuid, key, value, attached_at. (optional)
page = 1 # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10 # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = 'created_at:desc' # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's tags
    api_response = accounting.tags_api.list_tags(fields=fields, page=page, per_page=per_page, order_by=order_by)
    print("The response of TagsApi->list_tags:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->list_tags: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Comma-separated fields to include in each record. Default fields: uuid, key, value, attached_at. | [optional] 
 **page** | **int**| Page number, starting at 1. Values below 1 are treated as 1. | [optional] [default to 1]
 **per_page** | **int**| Records per page. The server caps page size to 100. Values below 1 use that maximum. | [optional] [default to 10]
 **order_by** | **str**| Sort by a supported field and direction, using field:asc or field:desc. | [optional] 

### Return type

[**ListTags200Response**](ListTags200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tags_by_resource**
> list_tags_by_resource(resource, fields=fields, page=page, per_page=per_page, order_by=order_by)

List company's tags by resource attachment

List company's tags by resource attachment. Use the parameters and response fields below for this operation. Requires at least one permission: `list.tags`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

resource = 'resource_example' # str | The resource
fields = 'uuid,key,value,attached_at' # str | Comma-separated fields to include in each record. Default fields: uuid, key, value, attached_at. (optional)
page = 1 # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10 # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = 'created_at:desc' # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's tags by resource attachment
    api_response = accounting.tags_api.list_tags_by_resource(resource, fields=fields, page=page, per_page=per_page, order_by=order_by)
    print("The response of TagsApi->list_tags_by_resource:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->list_tags_by_resource: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**| The resource | 
 **fields** | **str**| Comma-separated fields to include in each record. Default fields: uuid, key, value, attached_at. | [optional] 
 **page** | **int**| Page number, starting at 1. Values below 1 are treated as 1. | [optional] [default to 1]
 **per_page** | **int**| Records per page. The server caps page size to 100. Values below 1 use that maximum. | [optional] [default to 10]
 **order_by** | **str**| Sort by a supported field and direction, using field:asc or field:desc. | [optional] 

### Return type

[**ListTags200Response**](ListTags200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tag**
> update_tag(uuid, add_tag_request)

Update a tag

Update a tag. Send the fields accepted by this operation in the request body. Requires at least one permission: `edit.tag`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The tag uuid
add_tag_request = accounting_sh.AddTagRequest() # AddTagRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a tag
    api_response = accounting.tags_api.update_tag(uuid, add_tag_request)
    print("The response of TagsApi->update_tag:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->update_tag: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The tag uuid | 
 **add_tag_request** | [**AddTagRequest**](AddTagRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**AddTag200Response**](AddTag200Response.md)

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

