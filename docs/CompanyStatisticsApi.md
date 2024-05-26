# accounting_sh.CompanyStatisticsApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_statistics**](CompanyStatisticsApi.md#get_statistics) | **GET** /companies/{uuid}/statistics/period | Get company&#39;s statistic


# **get_statistics**
> get_statistics(uuid, start=start, end=end)

Get company's statistic

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The company uuid
start = 'start_example' # str | Start date (optional)
end = 'end_example' # str | End date (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # Get company's statistic
    api_response = accounting.company_statistics_api.get_statistics(uuid, start=start, end=end)
    print("The response of CompanyStatisticsApi->get_statistics:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyStatisticsApi->get_statistics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The company uuid | 
 **start** | **str**| Start date | [optional] 
 **end** | **str**| End date | [optional] 

### Return type

[**GetStatistics200Response**](GetStatistics200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

