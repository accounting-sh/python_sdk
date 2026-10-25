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
> add_company_vat_id(uuid, add_company_vat_id_request)

Add a company's Vat Id

Add a company's Vat Id. Send the resource fields in the request body; the response contains the saved record. Requires at least one permission: `vat.add`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The company uuid
add_company_vat_id_request = accounting_sh.AddCompanyVatIdRequest() # AddCompanyVatIdRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Add a company's Vat Id
    api_response = accounting.vatid_api.add_company_vat_id(uuid, add_company_vat_id_request)
    print("The response of VATIDApi->add_company_vat_id:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VATIDApi->add_company_vat_id: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The company uuid | 
 **add_company_vat_id_request** | [**AddCompanyVatIdRequest**](AddCompanyVatIdRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**AddCompanyVatId200Response**](AddCompanyVatId200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**400** | The request failed validation or could not be processed. Inspect errors, correct the input, and try again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_company_vat_id**
> delete_company_vat_id(uuid, key)

Delete a company's Vat Id

Delete a company's Vat Id. This action deletes the selected record. Review references to it before deletion. Requires at least one permission: `vat.delete`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The company uuid
key = 'key_example' # str | The VAT ID uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete a company's Vat Id
    api_response = accounting.vatid_api.delete_company_vat_id(uuid, key)
    print("The response of VATIDApi->delete_company_vat_id:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VATIDApi->delete_company_vat_id: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The company uuid | 
 **key** | **str**| The VAT ID uuid | 

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

# **get_company_vat_id**
> get_company_vat_id(uuid, key)

Get a company's Vat Id

Get a company's Vat Id. Use the identifier returned by the corresponding list or create operation. Requires at least one permission: `vat.view`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The company uuid
key = 'key_example' # str | The VAT ID uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a company's Vat Id
    api_response = accounting.vatid_api.get_company_vat_id(uuid, key)
    print("The response of VATIDApi->get_company_vat_id:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VATIDApi->get_company_vat_id: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The company uuid | 
 **key** | **str**| The VAT ID uuid | 

### Return type

[**AddCompanyVatId200Response**](AddCompanyVatId200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_company_vat_id**
> list_company_vat_id(uuid, fields=fields, page=page, per_page=per_page, order_by=order_by)

List company's Vat Id

List company's Vat Id. Retrieve records using the query parameters below. Requires at least one permission: `vat.list`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The company uuid
fields = 'uuid,vat_id,country' # str | Comma-separated fields to include in each record. Default fields: uuid, vat_id, country. (optional)
page = 1 # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10 # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = 'created_at:desc' # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's Vat Id
    api_response = accounting.vatid_api.list_company_vat_id(uuid, fields=fields, page=page, per_page=per_page, order_by=order_by)
    print("The response of VATIDApi->list_company_vat_id:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VATIDApi->list_company_vat_id: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The company uuid | 
 **fields** | **str**| Comma-separated fields to include in each record. Default fields: uuid, vat_id, country. | [optional] 
 **page** | **int**| Page number, starting at 1. Values below 1 are treated as 1. | [optional] [default to 1]
 **per_page** | **int**| Records per page. The server caps page size to 100. Values below 1 use that maximum. | [optional] [default to 10]
 **order_by** | **str**| Sort by a supported field and direction, using field:asc or field:desc. | [optional] 

### Return type

[**ListCompanyVatId200Response**](ListCompanyVatId200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_company_vat_id**
> update_company_vat_id(uuid, key, add_company_vat_id_request)

Update a company's Vat Id

Update a company's Vat Id. Send the fields accepted by this operation in the request body. Requires at least one permission: `vat.edit`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The company uuid
key = 'key_example' # str | The VAT ID uuid
add_company_vat_id_request = accounting_sh.AddCompanyVatIdRequest() # AddCompanyVatIdRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a company's Vat Id
    api_response = accounting.vatid_api.update_company_vat_id(uuid, key, add_company_vat_id_request)
    print("The response of VATIDApi->update_company_vat_id:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VATIDApi->update_company_vat_id: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The company uuid | 
 **key** | **str**| The VAT ID uuid | 
 **add_company_vat_id_request** | [**AddCompanyVatIdRequest**](AddCompanyVatIdRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**AddCompanyVatId200Response**](AddCompanyVatId200Response.md)

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

