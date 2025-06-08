# accounting_sh.LogsApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**logs**](LogsApi.md#logs) | **GET** /logs | List company&#39;s logs


# **logs**
> logs(fields=fields, page=page, per_page=per_page, channel=channel, level=level, resource=resource, before=before, after=after, format=format)

List company's logs

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = 'fields_example' # str | A comma separated list of fields requested in the response (optional)
page = 'page_example' # str | The response page (optional)
per_page = 'per_page_example' # str | The number of items per page (optional)
channel = 'channel_example' # str | The channel to retrieve the logs from (optional)
level = 'level_example' # str | The log level to retrieve (optional)
resource = 'resource_example' # str | Retrive logs linked to that resource (optional)
before = 'before_example' # str | Retrive logs before the provided date (optional)
after = 'after_example' # str | Retrive logs after the provided date (optional)
format = 'format_example' # str | In which format to retrieve the logs, available: json or txt (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's logs
    api_response = accounting.logs_api.logs(fields=fields, page=page, per_page=per_page, channel=channel, level=level, resource=resource, before=before, after=after, format=format)
    print("The response of LogsApi->logs:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogsApi->logs: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| A comma separated list of fields requested in the response | [optional] 
 **page** | **str**| The response page | [optional] 
 **per_page** | **str**| The number of items per page | [optional] 
 **channel** | **str**| The channel to retrieve the logs from | [optional] 
 **level** | **str**| The log level to retrieve | [optional] 
 **resource** | **str**| Retrive logs linked to that resource | [optional] 
 **before** | **str**| Retrive logs before the provided date | [optional] 
 **after** | **str**| Retrive logs after the provided date | [optional] 
 **format** | **str**| In which format to retrieve the logs, available: json or txt | [optional] 

### Return type

[**Logs200Response**](Logs200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

