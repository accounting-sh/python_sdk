# accounting_sh.CategoriesApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_category**](CategoriesApi.md#add_category) | **POST** /categories | Add a category
[**delete_category**](CategoriesApi.md#delete_category) | **DELETE** /categories/{uuid} | Delete a category
[**get_category**](CategoriesApi.md#get_category) | **GET** /categories/{uuid} | Get a category
[**list_categories**](CategoriesApi.md#list_categories) | **GET** /categories | List company&#39;s categories
[**update_category**](CategoriesApi.md#update_category) | **PUT** /categories/{uuid} | Update a category


# **add_category**
> add_category(add_category_request)

Add a category

Add a category. Send the resource fields in the request body; the response contains the saved record. Requires at least one permission: `add.category`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_category_request = accounting_sh.AddCategoryRequest() # AddCategoryRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Add a category
    api_response = accounting.categories_api.add_category(add_category_request)
    print("The response of CategoriesApi->add_category:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->add_category: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_category_request** | [**AddCategoryRequest**](AddCategoryRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**AddCategory200Response**](AddCategory200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**400** | The request failed validation or could not be processed. Inspect errors, correct the input, and try again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_category**
> delete_category(uuid)

Delete a category

Delete a category. This action deletes the selected record. Review references to it before deletion. Requires at least one permission: `delete.category`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The category uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete a category
    api_response = accounting.categories_api.delete_category(uuid)
    print("The response of CategoriesApi->delete_category:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->delete_category: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The category uuid | 

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

# **get_category**
> get_category(uuid)

Get a category

Get a category. Use the identifier returned by the corresponding list or create operation. Requires at least one permission: `view.category`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The category uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a category
    api_response = accounting.categories_api.get_category(uuid)
    print("The response of CategoriesApi->get_category:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->get_category: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The category uuid | 

### Return type

[**AddCategory200Response**](AddCategory200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_categories**
> list_categories(fields=fields, page=page, per_page=per_page, order_by=order_by)

List company's categories

List company's categories. Retrieve records using the query parameters below. Requires at least one permission: `list.categories`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = 'uuid,name,type,color' # str | Comma-separated fields to include in each record. Default fields: uuid, name, type, color. (optional)
page = 1 # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10 # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = 'created_at:desc' # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's categories
    api_response = accounting.categories_api.list_categories(fields=fields, page=page, per_page=per_page, order_by=order_by)
    print("The response of CategoriesApi->list_categories:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->list_categories: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Comma-separated fields to include in each record. Default fields: uuid, name, type, color. | [optional] 
 **page** | **int**| Page number, starting at 1. Values below 1 are treated as 1. | [optional] [default to 1]
 **per_page** | **int**| Records per page. The server caps page size to 100. Values below 1 use that maximum. | [optional] [default to 10]
 **order_by** | **str**| Sort by a supported field and direction, using field:asc or field:desc. | [optional] 

### Return type

[**ListCategories200Response**](ListCategories200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_category**
> update_category(uuid, add_category_request)

Update a category

Update a category. Send the fields accepted by this operation in the request body. Requires at least one permission: `edit.category`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The category uuid
add_category_request = accounting_sh.AddCategoryRequest() # AddCategoryRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a category
    api_response = accounting.categories_api.update_category(uuid, add_category_request)
    print("The response of CategoriesApi->update_category:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->update_category: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The category uuid | 
 **add_category_request** | [**AddCategoryRequest**](AddCategoryRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**AddCategory200Response**](AddCategory200Response.md)

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

