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

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_category_request = accounting_sh.AddCategoryRequest() # AddCategoryRequest | 

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
 **add_category_request** | [**AddCategoryRequest**](AddCategoryRequest.md)|  | 

### Return type

[**AddCategory200Response**](AddCategory200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_category**
> delete_category(uuid)

Delete a category

### Example


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

# **get_category**
> get_category(uuid)

Get a category

### Example


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
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_categories**
> list_categories(fields=fields, page=page, per_page=per_page)

List company's categories

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
    # List company's categories
    api_response = accounting.categories_api.list_categories(fields=fields, page=page, per_page=per_page)
    print("The response of CategoriesApi->list_categories:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->list_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| A comma separated list of fields requested in the response | [optional] 
 **page** | **str**| The response page | [optional] 
 **per_page** | **str**| The number of items per page | [optional] 

### Return type

[**ListCategories200Response**](ListCategories200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_category**
> update_category(uuid, add_category_request)

Update a category

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The category uuid
add_category_request = accounting_sh.AddCategoryRequest() # AddCategoryRequest | 

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
 **add_category_request** | [**AddCategoryRequest**](AddCategoryRequest.md)|  | 

### Return type

[**AddCategory200Response**](AddCategory200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

