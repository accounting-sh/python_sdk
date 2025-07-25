# accounting_sh.AccountConnectionsApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_account_connection**](AccountConnectionsApi.md#delete_account_connection) | **DELETE** /accounts/{uuid}/connect | Delete an account&#39;s connection
[**list_account_connections**](AccountConnectionsApi.md#list_account_connections) | **GET** /accounts/{uuid}/connect | List account&#39;s connections
[**list_banks**](AccountConnectionsApi.md#list_banks) | **GET** /accounts/{uuid}/connect/banks | List available bank connections
[**list_connectable_bank_accounts**](AccountConnectionsApi.md#list_connectable_bank_accounts) | **GET** /accounts/{uuid}/connect/accounts | List connectable bank accounts
[**list_connected_account_transactions**](AccountConnectionsApi.md#list_connected_account_transactions) | **GET** /accounts/{uuid}/connect/{connection} | List the connected account&#39;s transactions
[**request_bank_connection**](AccountConnectionsApi.md#request_bank_connection) | **POST** /accounts/{uuid}/connect/request | Request a new bank connection
[**select_bank_account**](AccountConnectionsApi.md#select_bank_account) | **POST** /accounts/{uuid}/connect/accounts | Select a bank account to connect


# **delete_account_connection**
> delete_account_connection(uuid)

Delete an account's connection

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The account uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete an account's connection
    api_response = accounting.account_connections_api.delete_account_connection(uuid)
    print("The response of AccountConnectionsApi->delete_account_connection:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountConnectionsApi->delete_account_connection: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The account uuid | 

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

# **list_account_connections**
> list_account_connections(uuid, fields=fields, page=page, per_page=per_page)

List account's connections

### Example

* Bearer (Api Key) Authentication (bearer):

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
**200** | Success |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_banks**
> list_banks(uuid, country=country)

List available bank connections

### Example

* Bearer (Api Key) Authentication (bearer):

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
**200** | Success |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_connectable_bank_accounts**
> list_connectable_bank_accounts(uuid, connection=connection)

List connectable bank accounts

### Example

* Bearer (Api Key) Authentication (bearer):

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
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_connected_account_transactions**
> list_connected_account_transactions(uuid, connection, period=period)

List the connected account's transactions

### Example

* Bearer (Api Key) Authentication (bearer):

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
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_bank_connection**
> request_bank_connection(uuid, request_bank_connection_request)

Request a new bank connection

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The account uuid
request_bank_connection_request = accounting_sh.RequestBankConnectionRequest() # RequestBankConnectionRequest | 

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
 **request_bank_connection_request** | [**RequestBankConnectionRequest**](RequestBankConnectionRequest.md)|  | 

### Return type

[**RequestBankConnection200Response**](RequestBankConnection200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **select_bank_account**
> select_bank_account(uuid, select_bank_account_request)

Select a bank account to connect

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The account uuid
select_bank_account_request = accounting_sh.SelectBankAccountRequest() # SelectBankAccountRequest | 

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
 **select_bank_account_request** | [**SelectBankAccountRequest**](SelectBankAccountRequest.md)|  | 

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

