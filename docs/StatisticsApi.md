# accounting_sh.StatisticsApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**summary_statistics_period**](StatisticsApi.md#summary_statistics_period) | **GET** /companies/{uuid}/statistics/summary | Company&#39;s summary statistics


# **summary_statistics_period**
> summary_statistics_period(uuid, start=start, end=end)

Company's summary statistics

Company's summary statistics. Use the parameters and response fields below for this operation. Requires at least one permission: `view.company`.

### Example

* Bearer (API key) Authentication (bearer):

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
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |
**400** | The request failed validation or could not be processed. Inspect errors, correct the input, and try again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

