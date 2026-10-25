# accounting_sh.TransactionsApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_link**](TransactionsApi.md#add_link) | **POST** /transactions/{uuid}/links | Add a new transaction link
[**add_transaction**](TransactionsApi.md#add_transaction) | **POST** /transactions | Add a transaction
[**add_transaction_code**](TransactionsApi.md#add_transaction_code) | **POST** /transactions/{uuid}/codes | Add a transaction&#39;s code
[**delete_link**](TransactionsApi.md#delete_link) | **DELETE** /transactions/{uuid}/links/{link_uuid} | Delete a transaction link
[**delete_transaction**](TransactionsApi.md#delete_transaction) | **DELETE** /transactions/{uuid} | Delete a transaction
[**delete_transaction_code**](TransactionsApi.md#delete_transaction_code) | **DELETE** /transactions/{uuid}/codes/{code} | Delete a transaction&#39;s code
[**get_transaction**](TransactionsApi.md#get_transaction) | **GET** /transactions/{uuid} | Get a transaction
[**import_transactions**](TransactionsApi.md#import_transactions) | **POST** /transactions/import | Import transactions - INTERNAL
[**ledger**](TransactionsApi.md#ledger) | **GET** /transactions/ledger | List company&#39;s transactions and transfers
[**list_links**](TransactionsApi.md#list_links) | **GET** /transactions/{uuid}/links | List a transaction links
[**list_transaction_codes**](TransactionsApi.md#list_transaction_codes) | **GET** /transactions/{uuid}/codes | List transaction&#39;s codes
[**list_transactions**](TransactionsApi.md#list_transactions) | **GET** /transactions | List company&#39;s transactions
[**reconciliation_reject**](TransactionsApi.md#reconciliation_reject) | **POST** /transactions/{uuid}/reconciliation/rejections | Remember a rejected transaction/document candidate
[**reconciliation_run**](TransactionsApi.md#reconciliation_run) | **POST** /transactions/{uuid}/reconciliation | Schedule background matching for human review
[**reconciliation_suggestions**](TransactionsApi.md#reconciliation_suggestions) | **GET** /transactions/{uuid}/reconciliation/suggestions | Rank document and payment matches without creating links
[**reverse_transaction_link**](TransactionsApi.md#reverse_transaction_link) | **POST** /transactions/{uuid}/links/{link_uuid}/reverse | Reverse a human-confirmed match and its generated payment
[**update_link**](TransactionsApi.md#update_link) | **PUT** /transactions/{uuid}/links/{link_uuid} | Update a transaction link
[**update_transaction**](TransactionsApi.md#update_transaction) | **PUT** /transactions/{uuid} | Update a transaction
[**update_transaction_code**](TransactionsApi.md#update_transaction_code) | **PUT** /transactions/{uuid}/codes/{code} | Update a transaction&#39;s code
[**view_link**](TransactionsApi.md#view_link) | **GET** /transactions/{uuid}/links/{link_uuid} | View a transaction link


# **add_link**
> add_link(uuid, add_link_request)

Add a new transaction link

Add a new transaction link. Send the resource fields in the request body; the response contains the saved record. Requires at least one permission: `transaction_link.add`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | A transaction uuid
add_link_request = accounting_sh.AddLinkRequest() # AddLinkRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Add a new transaction link
    api_response = accounting.transactions_api.add_link(uuid, add_link_request)
    print("The response of TransactionsApi->add_link:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->add_link: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A transaction uuid | 
 **add_link_request** | [**AddLinkRequest**](AddLinkRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**AddLink200Response**](AddLink200Response.md)

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

# **add_transaction**
> add_transaction(add_transaction_request)

Add a transaction

Add a transaction. Send the resource fields in the request body; the response contains the saved record. Requires at least one permission: `transaction.add`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_transaction_request = accounting_sh.AddTransactionRequest() # AddTransactionRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Add a transaction
    api_response = accounting.transactions_api.add_transaction(add_transaction_request)
    print("The response of TransactionsApi->add_transaction:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->add_transaction: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_transaction_request** | [**AddTransactionRequest**](AddTransactionRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**AddTransaction200Response**](AddTransaction200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**400** | The request failed validation or could not be processed. Inspect errors, correct the input, and try again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_transaction_code**
> add_transaction_code(uuid, add_transaction_code_request)

Add a transaction's code

Add a transaction's code. Send the resource fields in the request body; the response contains the saved record. Requires at least one permission: `transaction_code.add`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The transaction uuid
add_transaction_code_request = accounting_sh.AddTransactionCodeRequest() # AddTransactionCodeRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Add a transaction's code
    api_response = accounting.transactions_api.add_transaction_code(uuid, add_transaction_code_request)
    print("The response of TransactionsApi->add_transaction_code:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->add_transaction_code: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The transaction uuid | 
 **add_transaction_code_request** | [**AddTransactionCodeRequest**](AddTransactionCodeRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**AddTransactionCode200Response**](AddTransactionCode200Response.md)

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

# **delete_link**
> delete_link(uuid, link_uuid)

Delete a transaction link

Delete a transaction link. This action deletes the selected record. Review references to it before deletion. Requires at least one permission: `transaction_link.delete`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | A transaction uuid
link_uuid = 'link_uuid_example' # str | A transaction link uuid OR the target uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete a transaction link
    api_response = accounting.transactions_api.delete_link(uuid, link_uuid)
    print("The response of TransactionsApi->delete_link:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->delete_link: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A transaction uuid | 
 **link_uuid** | **str**| A transaction link uuid OR the target uuid | 

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

# **delete_transaction**
> delete_transaction(uuid)

Delete a transaction

Delete a transaction. This action deletes the selected record. Review references to it before deletion. Requires at least one permission: `transaction.delete`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The transaction uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete a transaction
    api_response = accounting.transactions_api.delete_transaction(uuid)
    print("The response of TransactionsApi->delete_transaction:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->delete_transaction: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The transaction uuid | 

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

# **delete_transaction_code**
> delete_transaction_code(uuid, code)

Delete a transaction's code

Delete a transaction's code. This action deletes the selected record. Review references to it before deletion. Requires at least one permission: `transaction_code.delete`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The transaction uuid
code = 'code_example' # str | The transaction's code uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete a transaction's code
    api_response = accounting.transactions_api.delete_transaction_code(uuid, code)
    print("The response of TransactionsApi->delete_transaction_code:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->delete_transaction_code: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The transaction uuid | 
 **code** | **str**| The transaction&#39;s code uuid | 

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

# **get_transaction**
> get_transaction(uuid)

Get a transaction

Get a transaction. Use the identifier returned by the corresponding list or create operation. Requires at least one permission: `transaction.view`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The transaction uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a transaction
    api_response = accounting.transactions_api.get_transaction(uuid)
    print("The response of TransactionsApi->get_transaction:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->get_transaction: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The transaction uuid | 

### Return type

[**AddTransaction200Response**](AddTransaction200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_transactions**
> import_transactions(import_transactions_request)

Import transactions - INTERNAL

Import transaction records using the internal import payload. This operation is intended for the application import workflow. Requires at least one permission: `transaction.add`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

import_transactions_request = accounting_sh.ImportTransactionsRequest() # ImportTransactionsRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Import transactions - INTERNAL
    api_response = accounting.transactions_api.import_transactions(import_transactions_request)
    print("The response of TransactionsApi->import_transactions:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->import_transactions: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_transactions_request** | [**ImportTransactionsRequest**](ImportTransactionsRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**AddTransaction200Response**](AddTransaction200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ledger**
> ledger(fields=fields, page=page, per_page=per_page, account=account, order_by=order_by)

List company's transactions and transfers

Retrieve ledger entries combining transactions and transfers. Optionally filter by the account query parameter. Requires at least one permission: `transaction.list`, `list.transfers`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = 'uuid,account,amount,event_date' # str | Comma-separated fields to include in each record. Default fields: uuid, account, amount, event_date. (optional)
page = 1 # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10 # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
account = 'account_example' # str | An account uuid to filter results (optional)
order_by = 'created_at:desc' # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's transactions and transfers
    api_response = accounting.transactions_api.ledger(fields=fields, page=page, per_page=per_page, account=account, order_by=order_by)
    print("The response of TransactionsApi->ledger:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->ledger: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Comma-separated fields to include in each record. Default fields: uuid, account, amount, event_date. | [optional] 
 **page** | **int**| Page number, starting at 1. Values below 1 are treated as 1. | [optional] [default to 1]
 **per_page** | **int**| Records per page. The server caps page size to 100. Values below 1 use that maximum. | [optional] [default to 10]
 **account** | **str**| An account uuid to filter results | [optional] 
 **order_by** | **str**| Sort by a supported field and direction, using field:asc or field:desc. | [optional] 

### Return type

[**Ledger200Response**](Ledger200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_links**
> list_links(uuid, fields=fields, page=page, per_page=per_page, order_by=order_by)

List a transaction links

List a transaction links. Retrieve records using the query parameters below. Requires at least one permission: `transaction_link.list`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | A transaction uuid
fields = 'target_type,target,link_status' # str | Comma-separated fields to include in each record. Default fields: target_type, target, link_status. (optional)
page = 1 # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10 # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = 'created_at:desc' # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List a transaction links
    api_response = accounting.transactions_api.list_links(uuid, fields=fields, page=page, per_page=per_page, order_by=order_by)
    print("The response of TransactionsApi->list_links:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->list_links: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A transaction uuid | 
 **fields** | **str**| Comma-separated fields to include in each record. Default fields: target_type, target, link_status. | [optional] 
 **page** | **int**| Page number, starting at 1. Values below 1 are treated as 1. | [optional] [default to 1]
 **per_page** | **int**| Records per page. The server caps page size to 100. Values below 1 use that maximum. | [optional] [default to 10]
 **order_by** | **str**| Sort by a supported field and direction, using field:asc or field:desc. | [optional] 

### Return type

[**ListLinks200Response**](ListLinks200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transaction_codes**
> list_transaction_codes(uuid, fields=fields, page=page, per_page=per_page, account=account, order_by=order_by)

List transaction's codes

List transaction's codes. Retrieve records using the query parameters below. Requires at least one permission: `transaction_code.list`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The transaction uuid
fields = 'uuid,code,description,amount' # str | Comma-separated fields to include in each record. Default fields: uuid, code, description, amount. (optional)
page = 1 # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10 # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
account = 'account_example' # str | List to the specified account (optional)
order_by = 'created_at:desc' # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List transaction's codes
    api_response = accounting.transactions_api.list_transaction_codes(uuid, fields=fields, page=page, per_page=per_page, account=account, order_by=order_by)
    print("The response of TransactionsApi->list_transaction_codes:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->list_transaction_codes: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The transaction uuid | 
 **fields** | **str**| Comma-separated fields to include in each record. Default fields: uuid, code, description, amount. | [optional] 
 **page** | **int**| Page number, starting at 1. Values below 1 are treated as 1. | [optional] [default to 1]
 **per_page** | **int**| Records per page. The server caps page size to 100. Values below 1 use that maximum. | [optional] [default to 10]
 **account** | **str**| List to the specified account | [optional] 
 **order_by** | **str**| Sort by a supported field and direction, using field:asc or field:desc. | [optional] 

### Return type

[**ListTransactionCodes200Response**](ListTransactionCodes200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transactions**
> list_transactions(fields=fields, page=page, per_page=per_page, account=account, order_by=order_by)

List company's transactions

List company's transactions. Retrieve records using the query parameters below. Requires at least one permission: `transaction.list`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = 'uuid,account,amount,transaction_date' # str | Comma-separated fields to include in each record. Default fields: uuid, account, amount, transaction_date. (optional)
page = 1 # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10 # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
account = 'account_example' # str | List to the specified account (optional)
order_by = 'created_at:desc' # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's transactions
    api_response = accounting.transactions_api.list_transactions(fields=fields, page=page, per_page=per_page, account=account, order_by=order_by)
    print("The response of TransactionsApi->list_transactions:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->list_transactions: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Comma-separated fields to include in each record. Default fields: uuid, account, amount, transaction_date. | [optional] 
 **page** | **int**| Page number, starting at 1. Values below 1 are treated as 1. | [optional] [default to 1]
 **per_page** | **int**| Records per page. The server caps page size to 100. Values below 1 use that maximum. | [optional] [default to 10]
 **account** | **str**| List to the specified account | [optional] 
 **order_by** | **str**| Sort by a supported field and direction, using field:asc or field:desc. | [optional] 

### Return type

[**ListTransactions200Response**](ListTransactions200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reconciliation_reject**
> reconciliation_reject(uuid, reconciliation_reject_request)

Remember a rejected transaction/document candidate

Exclude a bill or invoice candidate from subsequent automatic matching. Confirmed financial links cannot be rejected through this operation. Requires `transaction_link.delete`, `transaction.view`, `view.bill` and `view.invoice` permissions.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | 
reconciliation_reject_request = accounting_sh.ReconciliationRejectRequest() # ReconciliationRejectRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Remember a rejected transaction/document candidate
    api_response = accounting.transactions_api.reconciliation_reject(uuid, reconciliation_reject_request)
    print("The response of TransactionsApi->reconciliation_reject:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->reconciliation_reject: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **reconciliation_reject_request** | [**ReconciliationRejectRequest**](ReconciliationRejectRequest.md)|  | 

### Return type

[**JournalCorrectionDelete405Response**](JournalCorrectionDelete405Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Candidate excluded from subsequent automatic matching |  -  |
**400** | Invalid target or confirmed financial link cannot be rejected |  -  |
**403** | Link deletion, transaction and document viewing permissions required |  -  |
**404** | Transaction not found in this company |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reconciliation_run**
> reconciliation_run(uuid)

Schedule background matching for human review

Queue transaction matching in the background. Inspect transaction links after processing; suggestions have no financial effects until human confirmation. Requires `transaction_link.add`, `transaction.view`, `view.bill` and `view.invoice` permissions.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Schedule background matching for human review
    api_response = accounting.transactions_api.reconciliation_run(uuid)
    print("The response of TransactionsApi->reconciliation_run:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->reconciliation_run: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**ReconciliationRun202Response**](ReconciliationRun202Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Matching requested; inspect transaction links after worker processing |  -  |
**503** | Background scheduling unavailable; retry later |  -  |
**403** | Link creation, transaction and document viewing permissions required |  -  |
**404** | Transaction not found in this company |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reconciliation_suggestions**
> reconciliation_suggestions(uuid)

Rank document and payment matches without creating links

Rank candidate documents and existing payments for review without creating links or payments. Requires `transaction.view`, `view.bill` and `view.invoice` permissions.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Rank document and payment matches without creating links
    api_response = accounting.transactions_api.reconciliation_suggestions(uuid)
    print("The response of TransactionsApi->reconciliation_suggestions:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->reconciliation_suggestions: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**ReconciliationSuggestions200Response**](ReconciliationSuggestions200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ranked candidates with evidence; scores are not probabilities |  -  |
**403** | Transaction and both bill/invoice viewing permissions required |  -  |
**404** | Transaction not found in this company |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reverse_transaction_link**
> reverse_transaction_link(uuid, link_uuid)

Reverse a human-confirmed match and its generated payment

Reverse a confirmed match and its generated payment while preserving a reused payment. Requires `transaction_link.edit`, `edit.invoice.revenues` and the target document viewing permission (`view.bill` or `view.invoice`).

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | 
link_uuid = 'link_uuid_example' # str | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Reverse a human-confirmed match and its generated payment
    api_response = accounting.transactions_api.reverse_transaction_link(uuid, link_uuid)
    print("The response of TransactionsApi->reverse_transaction_link:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->reverse_transaction_link: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **link_uuid** | **str**|  | 

### Return type

[**JournalCorrectionDelete405Response**](JournalCorrectionDelete405Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Match reversed; reused payments are preserved |  -  |
**400** | Link cannot be reversed |  -  |
**404** | Transaction or link not found in this company |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_link**
> update_link(uuid, link_uuid, add_link_request)

Update a transaction link

Update a transaction link. Send the fields accepted by this operation in the request body. Requires at least one permission: `transaction_link.edit`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | A transaction uuid
link_uuid = 'link_uuid_example' # str | A transaction link uuid OR the target uuid
add_link_request = accounting_sh.AddLinkRequest() # AddLinkRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a transaction link
    api_response = accounting.transactions_api.update_link(uuid, link_uuid, add_link_request)
    print("The response of TransactionsApi->update_link:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->update_link: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A transaction uuid | 
 **link_uuid** | **str**| A transaction link uuid OR the target uuid | 
 **add_link_request** | [**AddLinkRequest**](AddLinkRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**ViewLink200Response**](ViewLink200Response.md)

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

# **update_transaction**
> update_transaction(uuid, add_transaction_request)

Update a transaction

Update a transaction. Send the fields accepted by this operation in the request body. Requires at least one permission: `transaction.edit`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The transaction uuid
add_transaction_request = accounting_sh.AddTransactionRequest() # AddTransactionRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a transaction
    api_response = accounting.transactions_api.update_transaction(uuid, add_transaction_request)
    print("The response of TransactionsApi->update_transaction:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->update_transaction: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The transaction uuid | 
 **add_transaction_request** | [**AddTransactionRequest**](AddTransactionRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**AddTransaction200Response**](AddTransaction200Response.md)

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

# **update_transaction_code**
> update_transaction_code(uuid, code, add_transaction_code_request)

Update a transaction's code

Update a transaction's code. Send the fields accepted by this operation in the request body. Requires at least one permission: `transaction_code.edit`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The transaction uuid
code = 'code_example' # str | Identifier of the code selected by this route.
add_transaction_code_request = accounting_sh.AddTransactionCodeRequest() # AddTransactionCodeRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a transaction's code
    api_response = accounting.transactions_api.update_transaction_code(uuid, code, add_transaction_code_request)
    print("The response of TransactionsApi->update_transaction_code:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->update_transaction_code: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The transaction uuid | 
 **code** | **str**| Identifier of the code selected by this route. | 
 **add_transaction_code_request** | [**AddTransactionCodeRequest**](AddTransactionCodeRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**AddTransactionCode200Response**](AddTransactionCode200Response.md)

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

# **view_link**
> view_link(uuid, link_uuid)

View a transaction link

View a transaction link. Use the identifier returned by the corresponding list or create operation. Requires at least one permission: `transaction_link.view`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | A transaction uuid
link_uuid = 'link_uuid_example' # str | A transaction link uuid OR the target uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # View a transaction link
    api_response = accounting.transactions_api.view_link(uuid, link_uuid)
    print("The response of TransactionsApi->view_link:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->view_link: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A transaction uuid | 
 **link_uuid** | **str**| A transaction link uuid OR the target uuid | 

### Return type

[**ViewLink200Response**](ViewLink200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

