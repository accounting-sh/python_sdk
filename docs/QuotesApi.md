# accounting_sh.QuotesApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_quote**](QuotesApi.md#add_quote) | **POST** /quotes | Add a quote
[**delete_quote**](QuotesApi.md#delete_quote) | **DELETE** /quotes/{uuid} | Delete a quote
[**get_quote**](QuotesApi.md#get_quote) | **GET** /quotes/{uuid} | Get a quote
[**get_quote_document**](QuotesApi.md#get_quote_document) | **GET** /quotes/{uuid}/document | Get a quote in PDF
[**list_quotes**](QuotesApi.md#list_quotes) | **GET** /quotes | List company&#39;s quotes
[**update_quote**](QuotesApi.md#update_quote) | **PUT** /quotes/{uuid} | Update a quote


# **add_quote**
> add_quote(add_quote_request)

Add a quote

Add a quote. Send the resource fields in the request body; the response contains the saved record. Requires at least one permission: `add.quote`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_quote_request = accounting_sh.AddQuoteRequest() # AddQuoteRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Add a quote
    api_response = accounting.quotes_api.add_quote(add_quote_request)
    print("The response of QuotesApi->add_quote:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotesApi->add_quote: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_quote_request** | [**AddQuoteRequest**](AddQuoteRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**AddQuote200Response**](AddQuote200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**400** | The request failed validation or could not be processed. Inspect errors, correct the input, and try again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_quote**
> delete_quote(uuid)

Delete a quote

Delete a quote. This action deletes the selected record. Review references to it before deletion. Requires at least one permission: `quote.delete`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The quote uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete a quote
    api_response = accounting.quotes_api.delete_quote(uuid)
    print("The response of QuotesApi->delete_quote:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotesApi->delete_quote: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The quote uuid | 

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

# **get_quote**
> get_quote(uuid)

Get a quote

Get a quote. Use the identifier returned by the corresponding list or create operation. Requires at least one permission: `view.quote`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The quote uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a quote
    api_response = accounting.quotes_api.get_quote(uuid)
    print("The response of QuotesApi->get_quote:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotesApi->get_quote: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The quote uuid | 

### Return type

[**AddQuote200Response**](AddQuote200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quote_document**
> get_quote_document(uuid)

Get a quote in PDF

Retrieve the generated PDF for this record. HTTP 200 returns application/pdf. If generation is still pending, HTTP 202 returns JSON with success=false and an explanation; retry later. Requires at least one permission: `regenerate.quote`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The quote uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a quote in PDF
    api_response = accounting.quotes_api.get_quote_document(uuid)
    print("The response of QuotesApi->get_quote_document:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotesApi->get_quote_document: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The quote uuid | 

### Return type

**bytearray**

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Generated PDF document. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |
**202** | Background work is pending. Inspect the JSON response before retrying. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_quotes**
> list_quotes(fields=fields, page=page, per_page=per_page, order_by=order_by)

List company's quotes

List company's quotes. Retrieve records using the query parameters below. Requires at least one permission: `list.quotes`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = 'uuid,contact,quote_number,status' # str | Comma-separated fields to include in each record. Default fields: uuid, contact, quote_number, status. (optional)
page = 1 # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10 # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = 'created_at:desc' # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's quotes
    api_response = accounting.quotes_api.list_quotes(fields=fields, page=page, per_page=per_page, order_by=order_by)
    print("The response of QuotesApi->list_quotes:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotesApi->list_quotes: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Comma-separated fields to include in each record. Default fields: uuid, contact, quote_number, status. | [optional] 
 **page** | **int**| Page number, starting at 1. Values below 1 are treated as 1. | [optional] [default to 1]
 **per_page** | **int**| Records per page. The server caps page size to 100. Values below 1 use that maximum. | [optional] [default to 10]
 **order_by** | **str**| Sort by a supported field and direction, using field:asc or field:desc. | [optional] 

### Return type

[**ListQuotes200Response**](ListQuotes200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_quote**
> update_quote(uuid, update_quote_request)

Update a quote

Update a quote. Send the fields accepted by this operation in the request body. Requires at least one permission: `edit.quote`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The quote uuid
update_quote_request = accounting_sh.UpdateQuoteRequest() # UpdateQuoteRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a quote
    api_response = accounting.quotes_api.update_quote(uuid, update_quote_request)
    print("The response of QuotesApi->update_quote:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotesApi->update_quote: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The quote uuid | 
 **update_quote_request** | [**UpdateQuoteRequest**](UpdateQuoteRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**AddQuote200Response**](AddQuote200Response.md)

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

