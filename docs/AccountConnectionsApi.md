# accounting_sh.AccountConnectionsApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_account_connection**](AccountConnectionsApi.md#delete_account_connection) | **DELETE** /accounts/{uuid}/connect/{connection} | Delete an account&#39;s connection
[**import_account_transactions**](AccountConnectionsApi.md#import_account_transactions) | **POST** /accounts/{uuid}/transactions/import | Import all available bank transaction history asynchronously
[**list_account_connections**](AccountConnectionsApi.md#list_account_connections) | **GET** /accounts/{uuid}/connect | List account&#39;s connections
[**list_banks**](AccountConnectionsApi.md#list_banks) | **GET** /accounts/{uuid}/connect/banks | List available bank connections
[**list_connectable_bank_accounts**](AccountConnectionsApi.md#list_connectable_bank_accounts) | **GET** /accounts/{uuid}/connect/accounts | List connectable bank accounts
[**list_connected_account_transactions**](AccountConnectionsApi.md#list_connected_account_transactions) | **GET** /accounts/{uuid}/connect/{connection} | List the connected account&#39;s transactions
[**request_bank_connection**](AccountConnectionsApi.md#request_bank_connection) | **POST** /accounts/{uuid}/connect/request | Request a new bank connection
[**select_bank_account**](AccountConnectionsApi.md#select_bank_account) | **POST** /accounts/{uuid}/connect/accounts | Select a bank account to connect


# **delete_account_connection**
> delete_account_connection(uuid, connection)

Delete an account's connection

Delete an account's connection. This action deletes the selected record. Review references to it before deletion. Requires at least one permission: `account.connections.delete`. Requires company feature(s): `bank_connection`. Returns 402 if unavailable.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The account uuid
connection = 'connection_example' # str | The connection uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete an account's connection
    api_response = accounting.account_connections_api.delete_account_connection(uuid, connection)
    print("The response of AccountConnectionsApi->delete_account_connection:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountConnectionsApi->delete_account_connection: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The account uuid | 
 **connection** | **str**| The connection uuid | 

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
**402** | The company does not have the required feature. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_account_transactions**
> import_account_transactions(uuid)

Import all available bank transaction history asynchronously

Queue import of the available transaction history from the connected bank account. HTTP 202 acknowledges the background job; imported transactions become available through the transaction routes. Requires at least one permission: `transaction.add`. Requires company feature(s): `bank_connection`. Returns 402 if unavailable.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The account UUID

accounting = accounting_sh.Accounting("access_token")
try:
    # Import all available bank transaction history asynchronously
    api_response = accounting.account_connections_api.import_account_transactions(uuid)
    print("The response of AccountConnectionsApi->import_account_transactions:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountConnectionsApi->import_account_transactions: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The account UUID | 

### Return type

[**ImportAccountTransactions202Response**](ImportAccountTransactions202Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Import queued |  -  |
**400** | No bank account is linked |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**402** | The company does not have the required feature. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_account_connections**
> list_account_connections(uuid, fields=fields, page=page, per_page=per_page)

List account's connections

List account's connections. Retrieve records using the query parameters below. Requires at least one permission: `account.connections.list`. Requires company feature(s): `bank_connection`. Returns 402 if unavailable.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The account uuid
fields = 'fields_example' # str | A comma separated list of fields requested in the response (optional)
page = 'page_example' # str | The response page (optional)
per_page = 'per_page_example' # str | The number of items per page (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List account's connections
    api_response = accounting.account_connections_api.list_account_connections(uuid, fields=fields, page=page, per_page=per_page)
    print("The response of AccountConnectionsApi->list_account_connections:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountConnectionsApi->list_account_connections: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The account uuid | 
 **fields** | **str**| A comma separated list of fields requested in the response | [optional] 
 **page** | **str**| The response page | [optional] 
 **per_page** | **str**| The number of items per page | [optional] 

### Return type

[**ListAccountConnections200Response**](ListAccountConnections200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**402** | The company does not have the required feature. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_banks**
> list_banks(uuid, country=country)

List available bank connections

List available bank connections. Use the parameters and response fields below for this operation. Requires at least one permission: `account.connections.banks`. Requires company feature(s): `bank_connection`. Returns 402 if unavailable.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The account uuid
country = 'country_example' # str | A two letter country code, if none are specified, the company's country is used (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List available bank connections
    api_response = accounting.account_connections_api.list_banks(uuid, country=country)
    print("The response of AccountConnectionsApi->list_banks:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountConnectionsApi->list_banks: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The account uuid | 
 **country** | **str**| A two letter country code, if none are specified, the company&#39;s country is used | [optional] 

### Return type

[**ListBanks200Response**](ListBanks200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**402** | The company does not have the required feature. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_connectable_bank_accounts**
> list_connectable_bank_accounts(uuid, connection=connection)

List connectable bank accounts

List connectable bank accounts. Use the parameters and response fields below for this operation. Requires at least one permission: `account.connections.banks`. Requires company feature(s): `bank_connection`. Returns 402 if unavailable.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The account uuid
connection = 'connection_example' # str | The connection request UUID (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List connectable bank accounts
    api_response = accounting.account_connections_api.list_connectable_bank_accounts(uuid, connection=connection)
    print("The response of AccountConnectionsApi->list_connectable_bank_accounts:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountConnectionsApi->list_connectable_bank_accounts: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The account uuid | 
 **connection** | **str**| The connection request UUID | [optional] 

### Return type

[**ListConnectableBankAccounts200Response**](ListConnectableBankAccounts200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |
**400** | The request failed validation or could not be processed. Inspect errors, correct the input, and try again. |  -  |
**402** | The company does not have the required feature. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_connected_account_transactions**
> list_connected_account_transactions(uuid, connection, period=period)

List the connected account's transactions

List the connected account's transactions. Use the parameters and response fields below for this operation. Requires at least one permission: `account.connections.list`. Requires company feature(s): `bank_connection`. Returns 402 if unavailable.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The account uuid
connection = 'connection_example' # str | The connection uuid
period = 3.4 # float | The number of days to look back for transactions. Default is 7 days. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List the connected account's transactions
    api_response = accounting.account_connections_api.list_connected_account_transactions(uuid, connection, period=period)
    print("The response of AccountConnectionsApi->list_connected_account_transactions:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountConnectionsApi->list_connected_account_transactions: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The account uuid | 
 **connection** | **str**| The connection uuid | 
 **period** | **float**| The number of days to look back for transactions. Default is 7 days. | [optional] 

### Return type

[**ListConnectedAccountTransactions200Response**](ListConnectedAccountTransactions200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |
**402** | The company does not have the required feature. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_bank_connection**
> request_bank_connection(uuid, request_bank_connection_request)

Request a new bank connection

Request a new bank connection. Use the parameters and response fields below for this operation. Requires at least one permission: `account.connections.banks`. Requires company feature(s): `bank_connection`. Returns 402 if unavailable.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The account uuid
request_bank_connection_request = accounting_sh.RequestBankConnectionRequest() # RequestBankConnectionRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Request a new bank connection
    api_response = accounting.account_connections_api.request_bank_connection(uuid, request_bank_connection_request)
    print("The response of AccountConnectionsApi->request_bank_connection:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountConnectionsApi->request_bank_connection: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The account uuid | 
 **request_bank_connection_request** | [**RequestBankConnectionRequest**](RequestBankConnectionRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**RequestBankConnection200Response**](RequestBankConnection200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |
**400** | The request failed validation or could not be processed. Inspect errors, correct the input, and try again. |  -  |
**402** | The company does not have the required feature. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **select_bank_account**
> select_bank_account(uuid, select_bank_account_request)

Select a bank account to connect

Select a bank account to connect. Use the parameters and response fields below for this operation. Requires at least one permission: `account.connections.banks`. Requires company feature(s): `bank_connection`. Returns 402 if unavailable.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The account uuid
select_bank_account_request = accounting_sh.SelectBankAccountRequest() # SelectBankAccountRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Select a bank account to connect
    api_response = accounting.account_connections_api.select_bank_account(uuid, select_bank_account_request)
    print("The response of AccountConnectionsApi->select_bank_account:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountConnectionsApi->select_bank_account: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The account uuid | 
 **select_bank_account_request** | [**SelectBankAccountRequest**](SelectBankAccountRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

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
**400** | The request failed validation or could not be processed. Inspect errors, correct the input, and try again. |  -  |
**402** | The company does not have the required feature. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

