# accounting_sh.CountriesApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_translated_countries**](CountriesApi.md#get_translated_countries) | **GET** /countries/{lang} | Get translated list of countries


# **get_translated_countries**
> get_translated_countries(lang)

Get translated list of countries

Retrieve country reference data translated into the requested language.

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

lang = 'lang_example' # str | The target language

accounting = accounting_sh.Accounting("access_token")
try:
    # Get translated list of countries
    api_response = accounting.countries_api.get_translated_countries(lang)
    print("The response of CountriesApi->get_translated_countries:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountriesApi->get_translated_countries: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang** | **str**| The target language | 

### Return type

[**GetTranslatedCountries200Response**](GetTranslatedCountries200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

