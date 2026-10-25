# accounting_sh.TaxApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tax_rate**](TaxApi.md#get_tax_rate) | **GET** /tax/{country} | Get the latest tax rate for a country
[**verify_vat_id**](TaxApi.md#verify_vat_id) | **GET** /vat/verify/{number} | Verify a VAT ID


# **get_tax_rate**
> get_tax_rate(country)

Get the latest tax rate for a country

Retrieve the tax rate reference data for the supplied country code. Requires at least one permission: `view.tax.rates`. Requires company feature(s): `api`. Returns 402 if unavailable.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

country = 'country_example' # str | The country

accounting = accounting_sh.Accounting("access_token")
try:
    # Get the latest tax rate for a country
    api_response = accounting.tax_api.get_tax_rate(country)
    print("The response of TaxApi->get_tax_rate:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxApi->get_tax_rate: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| The country | 

### Return type

[**GetTaxRate200Response**](GetTaxRate200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**402** | The company does not have the required feature. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_vat_id**
> verify_vat_id(number)

Verify a VAT ID

Verify the supplied VAT identifier using the external verification service. Availability and returned information depend on that service. Requires at least one permission: `vat_id:verify`. Requires company feature(s): `api`. Returns 402 if unavailable.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

number = 'number_example' # str | The VAT ID

accounting = accounting_sh.Accounting("access_token")
try:
    # Verify a VAT ID
    api_response = accounting.tax_api.verify_vat_id(number)
    print("The response of TaxApi->verify_vat_id:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxApi->verify_vat_id: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **number** | **str**| The VAT ID | 

### Return type

[**VerifyVatId200Response**](VerifyVatId200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**402** | The company does not have the required feature. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

