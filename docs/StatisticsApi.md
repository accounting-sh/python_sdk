# accounting_sh.StatisticsApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**summary_statistics_period**](StatisticsApi.md#summary_statistics_period) | **GET** /companies/{uuid}/statistics/summary | Company&#39;s summary statistics


# **summary_statistics_period**
> summary_statistics_period(uuid, start=start, end=end)

Company's summary statistics

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The company uuid
start = '2013-10-20' # date | The start date (optional)
end = '2013-10-20' # date | The end date (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # Company's summary statistics
    api_response = accounting.statistics_api.summary_statistics_period(uuid, start=start, end=end)
    print("The response of StatisticsApi->summary_statistics_period:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->summary_statistics_period: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The company uuid | 
 **start** | **date**| The start date | [optional] 
 **end** | **date**| The end date | [optional] 

### Return type

[**SummaryStatisticsPeriod200Response**](SummaryStatisticsPeriod200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

