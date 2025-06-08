# accounting_sh.TransactionsApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_transaction**](TransactionsApi.md#add_transaction) | **POST** /transactions | Add a transaction
[**add_transaction_code**](TransactionsApi.md#add_transaction_code) | **POST** /transactions/{uuid}/codes | Add a transaction&#39;s code
[**delete_transaction**](TransactionsApi.md#delete_transaction) | **DELETE** /transactions/{uuid} | Delete a transaction
[**delete_transaction_code**](TransactionsApi.md#delete_transaction_code) | **DELETE** /transactions/{uuid}/codes/{code} | Delete a transaction&#39;s code
[**get_transaction**](TransactionsApi.md#get_transaction) | **GET** /transactions/{uuid} | Get a transaction
[**import_transactions**](TransactionsApi.md#import_transactions) | **POST** /transactions/import | Import transactions - INTERNAL
[**ledger**](TransactionsApi.md#ledger) | **GET** /transactions/ledger | List company&#39;s transactions and transfers
[**list_transaction_codes**](TransactionsApi.md#list_transaction_codes) | **GET** /transactions/{uuid}/codes | List transaction&#39;s codes
[**list_transactions**](TransactionsApi.md#list_transactions) | **GET** /transactions | List company&#39;s transactions
[**update_transaction**](TransactionsApi.md#update_transaction) | **PUT** /transactions/{uuid} | Update a transaction
[**update_transaction_code**](TransactionsApi.md#update_transaction_code) | **PUT** /transactions/{uuid}/codes | Update a transaction&#39;s code


# **add_transaction**
> add_transaction(add_transaction_request)

Add a transaction

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_transaction_request = accounting_sh.AddTransactionRequest() # AddTransactionRequest | 

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
 **add_transaction_request** | [**AddTransactionRequest**](AddTransactionRequest.md)|  | 

### Return type

[**AddTransaction200Response**](AddTransaction200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_transaction_code**
> add_transaction_code(uuid, update_transaction_code_request)

Add a transaction's code

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The transaction uuid
update_transaction_code_request = accounting_sh.UpdateTransactionCodeRequest() # UpdateTransactionCodeRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Add a transaction's code
    api_response = accounting.transactions_api.add_transaction_code(uuid, update_transaction_code_request)
    print("The response of TransactionsApi->add_transaction_code:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->add_transaction_code: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The transaction uuid | 
 **update_transaction_code_request** | [**UpdateTransactionCodeRequest**](UpdateTransactionCodeRequest.md)|  | 

### Return type

[**UpdateTransactionCode200Response**](UpdateTransactionCode200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_transaction**
> delete_transaction(uuid)

Delete a transaction

### Example

* Bearer (Api Key) Authentication (bearer):

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

# **delete_transaction_code**
> delete_transaction_code(uuid, code)

Delete a transaction's code

### Example

* Bearer (Api Key) Authentication (bearer):

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

# **get_transaction**
> get_transaction(uuid)

Get a transaction

### Example

* Bearer (Api Key) Authentication (bearer):

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
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_transactions**
> import_transactions(import_transactions_request)

Import transactions - INTERNAL

Import transaction from a file or directly from extracted details

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

import_transactions_request = accounting_sh.ImportTransactionsRequest() # ImportTransactionsRequest | 

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
 **import_transactions_request** | [**ImportTransactionsRequest**](ImportTransactionsRequest.md)|  | 

### Return type

[**AddTransaction200Response**](AddTransaction200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ledger**
> ledger(fields=fields, page=page, per_page=per_page, account=account)

List company's transactions and transfers

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = 'fields_example' # str | A comma separated list of fields requested in the response (optional)
page = 'page_example' # str | The response page (optional)
per_page = 'per_page_example' # str | The number of items per page (optional)
account = 'account_example' # str | An account uuid to filter results (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's transactions and transfers
    api_response = accounting.transactions_api.ledger(fields=fields, page=page, per_page=per_page, account=account)
    print("The response of TransactionsApi->ledger:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->ledger: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| A comma separated list of fields requested in the response | [optional] 
 **page** | **str**| The response page | [optional] 
 **per_page** | **str**| The number of items per page | [optional] 
 **account** | **str**| An account uuid to filter results | [optional] 

### Return type

[**Ledger200Response**](Ledger200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transaction_codes**
> list_transaction_codes(uuid, fields=fields, page=page, per_page=per_page, account=account)

List transaction's codes

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The transaction uuid
fields = 'fields_example' # str | A comma separated list of fields requested in the response (optional)
page = 'page_example' # str | The response page (optional)
per_page = 'per_page_example' # str | The number of items per page (optional)
account = 'account_example' # str | List to the specified account (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List transaction's codes
    api_response = accounting.transactions_api.list_transaction_codes(uuid, fields=fields, page=page, per_page=per_page, account=account)
    print("The response of TransactionsApi->list_transaction_codes:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->list_transaction_codes: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The transaction uuid | 
 **fields** | **str**| A comma separated list of fields requested in the response | [optional] 
 **page** | **str**| The response page | [optional] 
 **per_page** | **str**| The number of items per page | [optional] 
 **account** | **str**| List to the specified account | [optional] 

### Return type

[**ListTransactionCodes200Response**](ListTransactionCodes200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transactions**
> list_transactions(fields=fields, page=page, per_page=per_page, account=account)

List company's transactions

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = 'fields_example' # str | A comma separated list of fields requested in the response (optional)
page = 'page_example' # str | The response page (optional)
per_page = 'per_page_example' # str | The number of items per page (optional)
account = 'account_example' # str | List to the specified account (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's transactions
    api_response = accounting.transactions_api.list_transactions(fields=fields, page=page, per_page=per_page, account=account)
    print("The response of TransactionsApi->list_transactions:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->list_transactions: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| A comma separated list of fields requested in the response | [optional] 
 **page** | **str**| The response page | [optional] 
 **per_page** | **str**| The number of items per page | [optional] 
 **account** | **str**| List to the specified account | [optional] 

### Return type

[**ListTransactions200Response**](ListTransactions200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_transaction**
> update_transaction(uuid, add_transaction_request)

Update a transaction

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The transaction uuid
add_transaction_request = accounting_sh.AddTransactionRequest() # AddTransactionRequest | 

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
 **add_transaction_request** | [**AddTransactionRequest**](AddTransactionRequest.md)|  | 

### Return type

[**AddTransaction200Response**](AddTransaction200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_transaction_code**
> update_transaction_code(uuid, update_transaction_code_request)

Update a transaction's code

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The transaction uuid
update_transaction_code_request = accounting_sh.UpdateTransactionCodeRequest() # UpdateTransactionCodeRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a transaction's code
    api_response = accounting.transactions_api.update_transaction_code(uuid, update_transaction_code_request)
    print("The response of TransactionsApi->update_transaction_code:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->update_transaction_code: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The transaction uuid | 
 **update_transaction_code_request** | [**UpdateTransactionCodeRequest**](UpdateTransactionCodeRequest.md)|  | 

### Return type

[**UpdateTransactionCode200Response**](UpdateTransactionCode200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

