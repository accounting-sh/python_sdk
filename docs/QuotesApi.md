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

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_quote_request = accounting_sh.AddQuoteRequest() # AddQuoteRequest | 

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
 **add_quote_request** | [**AddQuoteRequest**](AddQuoteRequest.md)|  | 

### Return type

[**AddQuote200Response**](AddQuote200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_quote**
> delete_quote(uuid)

Delete a quote

### Example


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

[**DeleteAccountConnection200Response**](DeleteAccountConnection200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quote**
> get_quote(uuid)

Get a quote

### Example


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
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quote_document**
> get_quote_document(uuid)

Get a quote in PDF

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The quote uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a quote in PDF
   accounting.quotes_api.get_quote_document(uuid)
except ApiException as e:
    print("Exception when calling QuotesApi->get_quote_document: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The quote uuid | 

### Return type

void (empty response body)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_quotes**
> list_quotes(fields=fields, page=page, per_page=per_page)

List company's quotes

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = 'fields_example' # str | A comma separated list of fields requested in the response (optional)
page = 'page_example' # str | The response page (optional)
per_page = 'per_page_example' # str | The number of items per page (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's quotes
    api_response = accounting.quotes_api.list_quotes(fields=fields, page=page, per_page=per_page)
    print("The response of QuotesApi->list_quotes:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotesApi->list_quotes: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| A comma separated list of fields requested in the response | [optional] 
 **page** | **str**| The response page | [optional] 
 **per_page** | **str**| The number of items per page | [optional] 

### Return type

[**ListQuotes200Response**](ListQuotes200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_quote**
> update_quote(uuid, add_quote_request)

Update a quote

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The quote uuid
add_quote_request = accounting_sh.AddQuoteRequest() # AddQuoteRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a quote
    api_response = accounting.quotes_api.update_quote(uuid, add_quote_request)
    print("The response of QuotesApi->update_quote:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotesApi->update_quote: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The quote uuid | 
 **add_quote_request** | [**AddQuoteRequest**](AddQuoteRequest.md)|  | 

### Return type

[**AddQuote200Response**](AddQuote200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

