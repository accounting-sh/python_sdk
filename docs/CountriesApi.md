# accounting_sh.CountriesApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_translated_countries**](CountriesApi.md#get_translated_countries) | **GET** /countries/{lang} | Get translated list of countries


# **get_translated_countries**
> get_translated_countries(lang)

Get translated list of countries

### Example

* Bearer (Api Key) Authentication (bearer):

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
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

