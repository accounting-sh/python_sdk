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

Add a revenue. Send the resource fields in the request body; the response contains the saved record. Requires at least one permission: `add.revenue`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_revenue_request = accounting_sh.AddRevenueRequest() # AddRevenueRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

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
 **add_revenue_request** | [**AddRevenueRequest**](AddRevenueRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**AddRevenue200Response**](AddRevenue200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**400** | The request failed validation or could not be processed. Inspect errors, correct the input, and try again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_revenue**
> delete_revenue(uuid)

Delete a revenue

Delete a revenue. This action deletes the selected record. Review references to it before deletion. Requires at least one permission: `revenue.delete`.

### Example

* Bearer (API key) Authentication (bearer):

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

# **get_revenue**
> get_revenue(uuid)

Get a revenue

Get a revenue. Use the identifier returned by the corresponding list or create operation. Requires at least one permission: `view.revenue`.

### Example

* Bearer (API key) Authentication (bearer):

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
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_revenues**
> list_revenues(fields=fields, page=page, per_page=per_page, order_by=order_by)

List company's revenues

List company's revenues. Retrieve records using the query parameters below. Requires at least one permission: `list.revenues`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = 'uuid,paid_at,amount,currency' # str | Comma-separated fields to include in each record. Default fields: uuid, paid_at, amount, currency. (optional)
page = 1 # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10 # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = 'created_at:desc' # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's revenues
    api_response = accounting.revenues_api.list_revenues(fields=fields, page=page, per_page=per_page, order_by=order_by)
    print("The response of RevenuesApi->list_revenues:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevenuesApi->list_revenues: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Comma-separated fields to include in each record. Default fields: uuid, paid_at, amount, currency. | [optional] 
 **page** | **int**| Page number, starting at 1. Values below 1 are treated as 1. | [optional] [default to 1]
 **per_page** | **int**| Records per page. The server caps page size to 100. Values below 1 use that maximum. | [optional] [default to 10]
 **order_by** | **str**| Sort by a supported field and direction, using field:asc or field:desc. | [optional] 

### Return type

[**ListRevenues200Response**](ListRevenues200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_revenue**
> update_revenue(uuid, add_revenue_request)

Update a revenue

Update a revenue. Send the fields accepted by this operation in the request body. Requires at least one permission: `edit.revenue`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The revenue uuid
add_revenue_request = accounting_sh.AddRevenueRequest() # AddRevenueRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

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
 **add_revenue_request** | [**AddRevenueRequest**](AddRevenueRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**AddRevenue200Response**](AddRevenue200Response.md)

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

