# accounting_sh.LogsApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**logs**](LogsApi.md#logs) | **GET** /logs | List company&#39;s logs


# **logs**
> logs(fields=fields, page=page, per_page=per_page, channel=channel, level=level, resource=resource, before=before, after=after, format=format, order_by=order_by)

List company's logs

List company's logs. Retrieve records using the query parameters below. Requires at least one permission: `log.view`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = 'uuid,channel,level,message,recorded_at' # str | Comma-separated fields to include in each record. Default fields: uuid, channel, level, message, recorded_at. (optional)
page = 1 # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10 # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
channel = 'channel_example' # str | The channel to retrieve the logs from (optional)
level = 'level_example' # str | The log level to retrieve (optional)
resource = 'resource_example' # str | Retrive logs linked to that resource (optional)
before = 'before_example' # str | Retrive logs before the provided date (optional)
after = 'after_example' # str | Retrive logs after the provided date (optional)
format = 'format_example' # str | In which format to retrieve the logs, available: json or txt (optional)
order_by = 'created_at:desc' # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's logs
    api_response = accounting.logs_api.logs(fields=fields, page=page, per_page=per_page, channel=channel, level=level, resource=resource, before=before, after=after, format=format, order_by=order_by)
    print("The response of LogsApi->logs:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogsApi->logs: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Comma-separated fields to include in each record. Default fields: uuid, channel, level, message, recorded_at. | [optional] 
 **page** | **int**| Page number, starting at 1. Values below 1 are treated as 1. | [optional] [default to 1]
 **per_page** | **int**| Records per page. The server caps page size to 100. Values below 1 use that maximum. | [optional] [default to 10]
 **channel** | **str**| The channel to retrieve the logs from | [optional] 
 **level** | **str**| The log level to retrieve | [optional] 
 **resource** | **str**| Retrive logs linked to that resource | [optional] 
 **before** | **str**| Retrive logs before the provided date | [optional] 
 **after** | **str**| Retrive logs after the provided date | [optional] 
 **format** | **str**| In which format to retrieve the logs, available: json or txt | [optional] 
 **order_by** | **str**| Sort by a supported field and direction, using field:asc or field:desc. | [optional] 

### Return type

[**Logs200Response**](Logs200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

