# accounting_sh.VATIDApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_company_vat_id**](VATIDApi.md#add_company_vat_id) | **POST** /companies/{uuid}/vat | Add a company&#39;s Vat Id
[**delete_company_vat_id**](VATIDApi.md#delete_company_vat_id) | **DELETE** /companies/{uuid}/vat/{key} | Delete a company&#39;s Vat Id
[**get_company_vat_id**](VATIDApi.md#get_company_vat_id) | **GET** /companies/{uuid}/vat/{key} | Get a company&#39;s Vat Id
[**list_company_vat_id**](VATIDApi.md#list_company_vat_id) | **GET** /companies/{uuid}/vat | List company&#39;s Vat Id
[**update_company_vat_id**](VATIDApi.md#update_company_vat_id) | **PUT** /companies/{uuid}/vat/{key} | Update a company&#39;s Vat Id


# **add_company_vat_id**
> add_company_vat_id(add_company_vat_id_request, uuid=uuid)

Add a company's Vat Id

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_company_vat_id_request = accounting_sh.AddCompanyVatIdRequest() # AddCompanyVatIdRequest | 
uuid = 'uuid_example' # str | The company uuid (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # Add a company's Vat Id
    api_response = accounting.vatid_api.add_company_vat_id(add_company_vat_id_request, uuid=uuid)
    print("The response of VATIDApi->add_company_vat_id:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VATIDApi->add_company_vat_id: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_company_vat_id_request** | [**AddCompanyVatIdRequest**](AddCompanyVatIdRequest.md)|  | 
 **uuid** | **str**| The company uuid | [optional] 

### Return type

[**AddCompanyVatId200Response**](AddCompanyVatId200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_company_vat_id**
> delete_company_vat_id(key, uuid=uuid)

Delete a company's Vat Id

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

key = 'key_example' # str | The VAT ID uuid
uuid = 'uuid_example' # str | The company uuid (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete a company's Vat Id
    api_response = accounting.vatid_api.delete_company_vat_id(key, uuid=uuid)
    print("The response of VATIDApi->delete_company_vat_id:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VATIDApi->delete_company_vat_id: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The VAT ID uuid | 
 **uuid** | **str**| The company uuid | [optional] 

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

# **get_company_vat_id**
> get_company_vat_id(key, uuid=uuid)

Get a company's Vat Id

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

key = 'key_example' # str | The VAT ID uuid
uuid = 'uuid_example' # str | The company uuid (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a company's Vat Id
    api_response = accounting.vatid_api.get_company_vat_id(key, uuid=uuid)
    print("The response of VATIDApi->get_company_vat_id:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VATIDApi->get_company_vat_id: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The VAT ID uuid | 
 **uuid** | **str**| The company uuid | [optional] 

### Return type

[**AddCompanyVatId200Response**](AddCompanyVatId200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_company_vat_id**
> list_company_vat_id(fields=fields, page=page, per_page=per_page, uuid=uuid)

List company's Vat Id

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = 'fields_example' # str | A comma separated list of fields requested in the response (optional)
page = 'page_example' # str | The response page (optional)
per_page = 'per_page_example' # str | The number of items per page (optional)
uuid = 'uuid_example' # str | The company uuid (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's Vat Id
    api_response = accounting.vatid_api.list_company_vat_id(fields=fields, page=page, per_page=per_page, uuid=uuid)
    print("The response of VATIDApi->list_company_vat_id:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VATIDApi->list_company_vat_id: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| A comma separated list of fields requested in the response | [optional] 
 **page** | **str**| The response page | [optional] 
 **per_page** | **str**| The number of items per page | [optional] 
 **uuid** | **str**| The company uuid | [optional] 

### Return type

[**ListCompanyVatId200Response**](ListCompanyVatId200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_company_vat_id**
> update_company_vat_id(key, add_company_vat_id_request, uuid=uuid)

Update a company's Vat Id

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

key = 'key_example' # str | The VAT ID uuid
add_company_vat_id_request = accounting_sh.AddCompanyVatIdRequest() # AddCompanyVatIdRequest | 
uuid = 'uuid_example' # str | The company uuid (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a company's Vat Id
    api_response = accounting.vatid_api.update_company_vat_id(key, add_company_vat_id_request, uuid=uuid)
    print("The response of VATIDApi->update_company_vat_id:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VATIDApi->update_company_vat_id: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The VAT ID uuid | 
 **add_company_vat_id_request** | [**AddCompanyVatIdRequest**](AddCompanyVatIdRequest.md)|  | 
 **uuid** | **str**| The company uuid | [optional] 

### Return type

[**AddCompanyVatId200Response**](AddCompanyVatId200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

