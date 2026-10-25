# accounting_sh.ExportApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_exports**](ExportApi.md#list_exports) | **GET** /export | List company&#39;s exports
[**request_export**](ExportApi.md#request_export) | **POST** /export | Request an export


# **list_exports**
> list_exports(fields=fields, page=page, per_page=per_page, order_by=order_by)

List company's exports

List company's exports. Retrieve records using the query parameters below. Requires at least one permission: `export`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = 'uuid,status,document,created_at,updated_at' # str | Comma-separated fields to include in each record. Default fields: uuid, status, document, created_at, updated_at. (optional)
page = 1 # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10 # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = 'created_at:desc' # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's exports
    api_response = accounting.export_api.list_exports(fields=fields, page=page, per_page=per_page, order_by=order_by)
    print("The response of ExportApi->list_exports:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportApi->list_exports: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Comma-separated fields to include in each record. Default fields: uuid, status, document, created_at, updated_at. | [optional] 
 **page** | **int**| Page number, starting at 1. Values below 1 are treated as 1. | [optional] [default to 1]
 **per_page** | **int**| Records per page. The server caps page size to 100. Values below 1 use that maximum. | [optional] [default to 10]
 **order_by** | **str**| Sort by a supported field and direction, using field:asc or field:desc. | [optional] 

### Return type

[**ListExports200Response**](ListExports200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_export**
> request_export(request_export_request)

Request an export

Queue an accounting ZIP using the supplied options. For companies with Journal, the ZIP also includes posted lines in journal.csv and an integrity/completeness manifest in journal-metadata.json, filtered by the export accounting-date range. Journal snapshots exceeding 50000 lines fail rather than truncate. HTTP 202 acknowledges the job. Use GET /export to find the export and its generation status. Requires at least one permission: `export`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

request_export_request = accounting_sh.RequestExportRequest() # RequestExportRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Request an export
    api_response = accounting.export_api.request_export(request_export_request)
    print("The response of ExportApi->request_export:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportApi->request_export: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_export_request** | [**RequestExportRequest**](RequestExportRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**ImportAccountTransactions202Response**](ImportAccountTransactions202Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**400** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

