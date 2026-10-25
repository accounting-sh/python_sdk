# accounting_sh.AccountsApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_account**](AccountsApi.md#add_account) | **POST** /accounts | Add an account
[**delete_account**](AccountsApi.md#delete_account) | **DELETE** /accounts/{uuid} | Delete an account
[**get_account**](AccountsApi.md#get_account) | **GET** /accounts/{uuid} | Get an account
[**list_accounts**](AccountsApi.md#list_accounts) | **GET** /accounts | List company&#39;s accounts
[**update_account**](AccountsApi.md#update_account) | **PUT** /accounts/{uuid} | Update an account


# **add_account**
> add_account(add_account_request)

Add an account

Add an account. Send the resource fields in the request body; the response contains the saved record. Requires at least one permission: `add.account`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_account_request = accounting_sh.AddAccountRequest() # AddAccountRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Add an account
    api_response = accounting.accounts_api.add_account(add_account_request)
    print("The response of AccountsApi->add_account:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->add_account: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_account_request** | [**AddAccountRequest**](AddAccountRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**AddAccount200Response**](AddAccount200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**400** | The request failed validation or could not be processed. Inspect errors, correct the input, and try again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_account**
> delete_account(uuid)

Delete an account

Delete an account. This action deletes the selected record. Review references to it before deletion. Requires at least one permission: `delete.account`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The account uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete an account
    api_response = accounting.accounts_api.delete_account(uuid)
    print("The response of AccountsApi->delete_account:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->delete_account: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The account uuid | 

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

# **get_account**
> get_account(uuid)

Get an account

Get an account. Use the identifier returned by the corresponding list or create operation. Requires at least one permission: `view.account`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The account uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get an account
    api_response = accounting.accounts_api.get_account(uuid)
    print("The response of AccountsApi->get_account:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_account: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The account uuid | 

### Return type

[**GetAccount200Response**](GetAccount200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_accounts**
> list_accounts(fields=fields, page=page, per_page=per_page, order_by=order_by)

List company's accounts

List company's accounts. Retrieve records using the query parameters below. Requires at least one permission: `list.accounts`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = 'uuid,name,bank,currency,journal_number' # str | Comma-separated fields to include in each record. Default fields: uuid, name, bank, currency, journal_number. (optional)
page = 1 # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10 # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = 'created_at:desc' # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's accounts
    api_response = accounting.accounts_api.list_accounts(fields=fields, page=page, per_page=per_page, order_by=order_by)
    print("The response of AccountsApi->list_accounts:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->list_accounts: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Comma-separated fields to include in each record. Default fields: uuid, name, bank, currency, journal_number. | [optional] 
 **page** | **int**| Page number, starting at 1. Values below 1 are treated as 1. | [optional] [default to 1]
 **per_page** | **int**| Records per page. The server caps page size to 100. Values below 1 use that maximum. | [optional] [default to 10]
 **order_by** | **str**| Sort by a supported field and direction, using field:asc or field:desc. | [optional] 

### Return type

[**ListAccounts200Response**](ListAccounts200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account**
> update_account(uuid, add_account_request)

Update an account

Update an account. Send the fields accepted by this operation in the request body. Requires at least one permission: `edit.account`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The account uuid
add_account_request = accounting_sh.AddAccountRequest() # AddAccountRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update an account
    api_response = accounting.accounts_api.update_account(uuid, add_account_request)
    print("The response of AccountsApi->update_account:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->update_account: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The account uuid | 
 **add_account_request** | [**AddAccountRequest**](AddAccountRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**AddAccount200Response**](AddAccount200Response.md)

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

