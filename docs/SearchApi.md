# accounting_sh.SearchApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search**](SearchApi.md#search) | **GET** /search | Search


# **search**
> search(q, exclude=exclude, only=only)

Search

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

q = 'q_example' # str | Query string
exclude = 'exclude_example' # str | Exclude specific types. This is a comma separated list. (optional)
only = 'only_example' # str | Perfom search only on those types. This is a comma separated list. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # Search
    api_response = accounting.search_api.search(q, exclude=exclude, only=only)
    print("The response of SearchApi->search:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Query string | 
 **exclude** | **str**| Exclude specific types. This is a comma separated list. | [optional] 
 **only** | **str**| Perfom search only on those types. This is a comma separated list. | [optional] 

### Return type

[**Search200Response**](Search200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

