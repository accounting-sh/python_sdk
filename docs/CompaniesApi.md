# accounting_sh.CompaniesApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_company**](CompaniesApi.md#add_company) | **POST** /companies | Add a company
[**delete_company**](CompaniesApi.md#delete_company) | **DELETE** /companies/{uuid} | Delete a company
[**get_company**](CompaniesApi.md#get_company) | **GET** /companies/{uuid} | Get a company
[**get_company_customization**](CompaniesApi.md#get_company_customization) | **GET** /companies/{uuid}/customization | Get a company&#39;s customization parameters
[**get_company_feature_set**](CompaniesApi.md#get_company_feature_set) | **GET** /companies/{uuid}/features | List a company&#39;s feature set
[**list_companies**](CompaniesApi.md#list_companies) | **GET** /companies | List companies on this instance
[**update_company**](CompaniesApi.md#update_company) | **PUT** /companies/{uuid} | Update a company


# **add_company**
> add_company(add_company_request)

Add a company

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_company_request = accounting_sh.AddCompanyRequest() # AddCompanyRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Add a company
    api_response = accounting.companies_api.add_company(add_company_request)
    print("The response of CompaniesApi->add_company:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompaniesApi->add_company: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_company_request** | [**AddCompanyRequest**](AddCompanyRequest.md)|  | 

### Return type

[**AddCompany200Response**](AddCompany200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_company**
> delete_company(uuid)

Delete a company

### Example


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

# **get_company**
> get_company(uuid)

Get a company

### Example


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
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_customization**
> get_company_customization(uuid)

Get a company's customization parameters

### Example


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

# **get_company_feature_set**
> get_company_feature_set(uuid)

List a company's feature set

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The company uuid

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
 **uuid** | **str**| The company uuid | 

### Return type

[**GetCompanyFeatureSet200Response**](GetCompanyFeatureSet200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_companies**
> list_companies(fields=fields, page=page, per_page=per_page)

List companies on this instance

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
    # List companies on this instance
    api_response = accounting.companies_api.list_companies(fields=fields, page=page, per_page=per_page)
    print("The response of CompaniesApi->list_companies:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompaniesApi->list_companies: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| A comma separated list of fields requested in the response | [optional] 
 **page** | **str**| The response page | [optional] 
 **per_page** | **str**| The number of items per page | [optional] 

### Return type

[**ListCompanies200Response**](ListCompanies200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_company**
> update_company(uuid, add_company_request)

Update a company

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The company uuid
add_company_request = accounting_sh.AddCompanyRequest() # AddCompanyRequest | 

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
 **add_company_request** | [**AddCompanyRequest**](AddCompanyRequest.md)|  | 

### Return type

[**AddCompany200Response**](AddCompany200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

