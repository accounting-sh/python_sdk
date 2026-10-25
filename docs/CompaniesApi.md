# accounting_sh.CompaniesApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_company**](CompaniesApi.md#add_company) | **POST** /companies | Add a company (resellers only)
[**delete_company**](CompaniesApi.md#delete_company) | **DELETE** /companies/{uuid} | Delete a company
[**get_company**](CompaniesApi.md#get_company) | **GET** /companies/{uuid} | Get a company
[**get_company_customization**](CompaniesApi.md#get_company_customization) | **GET** /companies/{uuid}/customization | Get a company&#39;s customization parameters
[**get_company_feature_set**](CompaniesApi.md#get_company_feature_set) | **GET** /companies/{uuid}/features | List a company&#39;s feature set
[**get_company_onboarding**](CompaniesApi.md#get_company_onboarding) | **GET** /companies/{uuid}/onboarding | Get company onboarding status
[**list_companies**](CompaniesApi.md#list_companies) | **GET** /companies | List companies on this instance (resellers only)
[**update_company**](CompaniesApi.md#update_company) | **PUT** /companies/{uuid} | Update a company


# **add_company**
> add_company(add_company_request)

Add a company (resellers only)

Restricted to resellers. Add a company. Send the resource fields in the request body; the response contains the saved record. Requires at least one permission: `add.company`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_company_request = accounting_sh.AddCompanyRequest() # AddCompanyRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Add a company (resellers only)
    api_response = accounting.companies_api.add_company(add_company_request)
    print("The response of CompaniesApi->add_company:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompaniesApi->add_company: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_company_request** | [**AddCompanyRequest**](AddCompanyRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**AddCompany200Response**](AddCompany200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**400** | The request failed validation or could not be processed. Inspect errors, correct the input, and try again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_company**
> delete_company(uuid)

Delete a company

Delete a company. This action deletes the selected record. Review references to it before deletion. Requires at least one permission: `company.delete`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The company uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete a company
    api_response = accounting.companies_api.delete_company(uuid)
    print("The response of CompaniesApi->delete_company:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompaniesApi->delete_company: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The company uuid | 

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

# **get_company**
> get_company(uuid)

Get a company

Get a company. Use the identifier returned by the corresponding list or create operation. Requires at least one permission: `view.company`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The company uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a company
    api_response = accounting.companies_api.get_company(uuid)
    print("The response of CompaniesApi->get_company:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompaniesApi->get_company: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The company uuid | 

### Return type

[**AddCompany200Response**](AddCompany200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_customization**
> get_company_customization(uuid)

Get a company's customization parameters

Get a company's customization parameters. Use the parameters and response fields below for this operation. Requires authentication.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The company uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a company's customization parameters
    api_response = accounting.companies_api.get_company_customization(uuid)
    print("The response of CompaniesApi->get_company_customization:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompaniesApi->get_company_customization: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The company uuid | 

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

# **get_company_feature_set**
> get_company_feature_set(uuid)

List a company's feature set

Retrieve the features enabled for the authenticated company. The company identifier must match the company associated with your authentication. Requires authentication.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | Identifier of the authenticated company.

accounting = accounting_sh.Accounting("access_token")
try:
    # List a company's feature set
    api_response = accounting.companies_api.get_company_feature_set(uuid)
    print("The response of CompaniesApi->get_company_feature_set:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompaniesApi->get_company_feature_set: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Identifier of the authenticated company. | 

### Return type

[**GetCompanyFeatureSet200Response**](GetCompanyFeatureSet200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Features enabled for the company. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_onboarding**
> get_company_onboarding(uuid)

Get company onboarding status

Get the company's current onboarding version and completion status. When incomplete, returns missing setting keys and the fiscal year end (default 31/12). French companies are checked for invoice.FR.franchise_en_base and invoice.FR.vat_on_debits; all companies are checked for preferred.locale. A completed response omits missing_settings and fiscal_year_end. Requires at least one permission: `view.company`, `edit.company`, `edit.company.settings`, `view.company.settings`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The authenticated company's UUID.

accounting = accounting_sh.Accounting("access_token")
try:
    # Get company onboarding status
    api_response = accounting.companies_api.get_company_onboarding(uuid)
    print("The response of CompaniesApi->get_company_onboarding:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompaniesApi->get_company_onboarding: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The authenticated company&#39;s UUID. | 

### Return type

[**GetCompanyOnboarding200Response**](GetCompanyOnboarding200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Onboarding status. Missing settings and fiscal year end are returned only when onboarding is incomplete. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_companies**
> list_companies(fields=fields, page=page, per_page=per_page, order_by=order_by)

List companies on this instance (resellers only)

Restricted to resellers. List companies on this instance. Retrieve records using the query parameters below. Requires at least one permission: `list.companies`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = 'uuid,name,currency,prefix' # str | Comma-separated fields to include in each record. Default fields: uuid, name, currency, prefix. (optional)
page = 1 # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10 # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = 'created_at:desc' # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List companies on this instance (resellers only)
    api_response = accounting.companies_api.list_companies(fields=fields, page=page, per_page=per_page, order_by=order_by)
    print("The response of CompaniesApi->list_companies:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompaniesApi->list_companies: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Comma-separated fields to include in each record. Default fields: uuid, name, currency, prefix. | [optional] 
 **page** | **int**| Page number, starting at 1. Values below 1 are treated as 1. | [optional] [default to 1]
 **per_page** | **int**| Records per page. The server caps page size to 100. Values below 1 use that maximum. | [optional] [default to 10]
 **order_by** | **str**| Sort by a supported field and direction, using field:asc or field:desc. | [optional] 

### Return type

[**ListCompanies200Response**](ListCompanies200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_company**
> update_company(uuid, add_company_request)

Update a company

Update a company. Send the fields accepted by this operation in the request body. Omitted optional fields retain their existing values. Requires at least one permission: `edit.company`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The company uuid
add_company_request = accounting_sh.AddCompanyRequest() # AddCompanyRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a company
    api_response = accounting.companies_api.update_company(uuid, add_company_request)
    print("The response of CompaniesApi->update_company:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompaniesApi->update_company: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The company uuid | 
 **add_company_request** | [**AddCompanyRequest**](AddCompanyRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**AddCompany200Response**](AddCompany200Response.md)

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

