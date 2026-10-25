# accounting_sh.SearchApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search**](SearchApi.md#search) | **GET** /search | Search


# **search**
> search(q, exclude=exclude, only=only)

Search

Search indexed company resources using the supplied query. Newly saved resources may appear after indexing completes. Requires at least one permission: `search`.

### Example

* Bearer (API key) Authentication (bearer):

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
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**400** | The request failed validation or could not be processed. Inspect errors, correct the input, and try again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

