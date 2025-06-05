# accounting_sh.CurrencyApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_exchange_rate**](CurrencyApi.md#get_exchange_rate) | **GET** /currency/{from}/{to} | Get the latest currency exchange rate


# **get_exchange_rate**
> get_exchange_rate(var_from, to)

Get the latest currency exchange rate

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

var_from = 'var_from_example' # str | The currency to convert from
to = 'to_example' # str | The currency to convert to

accounting = accounting_sh.Accounting("access_token")
try:
    # Get the latest currency exchange rate
    api_response = accounting.currency_api.get_exchange_rate(var_from, to)
    print("The response of CurrencyApi->get_exchange_rate:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurrencyApi->get_exchange_rate: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **str**| The currency to convert from | 
 **to** | **str**| The currency to convert to | 

### Return type

[**GetExchangeRate200Response**](GetExchangeRate200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

