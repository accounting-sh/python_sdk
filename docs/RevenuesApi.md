# accounting_sh.RevenuesApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_revenue**](RevenuesApi.md#add_revenue) | **POST** /incomes/revenues | Add a revenue
[**delete_revenue**](RevenuesApi.md#delete_revenue) | **DELETE** /incomes/revenues/{uuid} | Delete a revenue
[**get_revenue**](RevenuesApi.md#get_revenue) | **GET** /incomes/revenues/{uuid} | Get a revenue
[**list_revenues**](RevenuesApi.md#list_revenues) | **GET** /incomes/revenues | List company&#39;s revenues
[**update_revenue**](RevenuesApi.md#update_revenue) | **PUT** /incomes/revenues/{uuid} | Update a revenue


# **add_revenue**
> add_revenue(add_revenue_request)

Add a revenue

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_revenue_request = accounting_sh.AddRevenueRequest() # AddRevenueRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Add a revenue
    api_response = accounting.revenues_api.add_revenue(add_revenue_request)
    print("The response of RevenuesApi->add_revenue:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevenuesApi->add_revenue: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_revenue_request** | [**AddRevenueRequest**](AddRevenueRequest.md)|  | 

### Return type

[**AddRevenue200Response**](AddRevenue200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_revenue**
> delete_revenue(uuid)

Delete a revenue

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The revenue uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete a revenue
    api_response = accounting.revenues_api.delete_revenue(uuid)
    print("The response of RevenuesApi->delete_revenue:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevenuesApi->delete_revenue: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The revenue uuid | 

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

# **get_revenue**
> get_revenue(uuid)

Get a revenue

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The revenue uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a revenue
    api_response = accounting.revenues_api.get_revenue(uuid)
    print("The response of RevenuesApi->get_revenue:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevenuesApi->get_revenue: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The revenue uuid | 

### Return type

[**AddRevenue200Response**](AddRevenue200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_revenues**
> list_revenues(fields=fields, page=page, per_page=per_page)

List company's revenues

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
    # List company's revenues
    api_response = accounting.revenues_api.list_revenues(fields=fields, page=page, per_page=per_page)
    print("The response of RevenuesApi->list_revenues:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevenuesApi->list_revenues: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| A comma separated list of fields requested in the response | [optional] 
 **page** | **str**| The response page | [optional] 
 **per_page** | **str**| The number of items per page | [optional] 

### Return type

[**ListRevenues200Response**](ListRevenues200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_revenue**
> update_revenue(uuid, add_revenue_request)

Update a revenue

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The revenue uuid
add_revenue_request = accounting_sh.AddRevenueRequest() # AddRevenueRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a revenue
    api_response = accounting.revenues_api.update_revenue(uuid, add_revenue_request)
    print("The response of RevenuesApi->update_revenue:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevenuesApi->update_revenue: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The revenue uuid | 
 **add_revenue_request** | [**AddRevenueRequest**](AddRevenueRequest.md)|  | 

### Return type

[**AddRevenue200Response**](AddRevenue200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

