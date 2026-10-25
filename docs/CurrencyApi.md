# accounting_sh.CurrencyApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_exchange_rate**](CurrencyApi.md#get_exchange_rate) | **GET** /currency/{from}/{to} | Get the latest currency exchange rate


# **get_exchange_rate**
> get_exchange_rate(var_from, to)

Get the latest currency exchange rate

Retrieve the exchange rate for the source and destination currency codes in the URL. Requires at least one permission: `view.currency.rates`. Requires company feature(s): `api`. Returns 402 if unavailable.

### Example

* Bearer (API key) Authentication (bearer):

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
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |
**402** | The company does not have the required feature. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

