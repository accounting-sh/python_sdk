# accounting_sh.CredentialsApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_credential**](CredentialsApi.md#add_credential) | **POST** /credentials | Add a credential
[**delete_credential**](CredentialsApi.md#delete_credential) | **DELETE** /credentials/{uuid} | Delete a credential
[**get_credential**](CredentialsApi.md#get_credential) | **GET** /credentials/{uuid} | Get a credential
[**list_credentials**](CredentialsApi.md#list_credentials) | **GET** /credentials | List company&#39;s credentials
[**list_permissions**](CredentialsApi.md#list_permissions) | **GET** /credentials/permissions | List available permissions
[**me**](CredentialsApi.md#me) | **GET** /me | Get current credential informations
[**update_credential**](CredentialsApi.md#update_credential) | **PUT** /credentials/{uuid} | Update a credential
[**userveria**](CredentialsApi.md#userveria) | **POST** /userveria | Exchange a my stantabcorp (userveria) token for an Accounting Token


# **add_credential**
> add_credential(add_credential_request)

Add a credential

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_credential_request = accounting_sh.AddCredentialRequest() # AddCredentialRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Add a credential
    api_response = accounting.credentials_api.add_credential(add_credential_request)
    print("The response of CredentialsApi->add_credential:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->add_credential: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_credential_request** | [**AddCredentialRequest**](AddCredentialRequest.md)|  | 

### Return type

[**AddCredential200Response**](AddCredential200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_credential**
> delete_credential(uuid)

Delete a credential

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The credential uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete a credential
    api_response = accounting.credentials_api.delete_credential(uuid)
    print("The response of CredentialsApi->delete_credential:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->delete_credential: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The credential uuid | 

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

# **get_credential**
> get_credential(uuid)

Get a credential

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The credential uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a credential
    api_response = accounting.credentials_api.get_credential(uuid)
    print("The response of CredentialsApi->get_credential:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->get_credential: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The credential uuid | 

### Return type

[**GetCredential200Response**](GetCredential200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_credentials**
> list_credentials(fields=fields, page=page, per_page=per_page)

List company's credentials

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = 'fields_example' # str | A comma separated list of fields requested in the response (optional)
page = 'page_example' # str | The response page (optional)
per_page = 'per_page_example' # str | The number of items per page (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's credentials
    api_response = accounting.credentials_api.list_credentials(fields=fields, page=page, per_page=per_page)
    print("The response of CredentialsApi->list_credentials:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->list_credentials: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| A comma separated list of fields requested in the response | [optional] 
 **page** | **str**| The response page | [optional] 
 **per_page** | **str**| The number of items per page | [optional] 

### Return type

[**ListCredentials200Response**](ListCredentials200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_permissions**
> list_permissions()

List available permissions

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint


accounting = accounting_sh.Accounting("access_token")
try:
    # List available permissions
    api_response = accounting.credentials_api.list_permissions()
    print("The response of CredentialsApi->list_permissions:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->list_permissions: %s\n" % e)

```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListPermissions200Response**](ListPermissions200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List every available permissions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me**
> me()

Get current credential informations

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint


accounting = accounting_sh.Accounting("access_token")
try:
    # Get current credential informations
    api_response = accounting.credentials_api.me()
    print("The response of CredentialsApi->me:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->me: %s\n" % e)

```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Me200Response**](Me200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_credential**
> update_credential(uuid, add_credential_request)

Update a credential

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The credential uuid
add_credential_request = accounting_sh.AddCredentialRequest() # AddCredentialRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a credential
    api_response = accounting.credentials_api.update_credential(uuid, add_credential_request)
    print("The response of CredentialsApi->update_credential:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->update_credential: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The credential uuid | 
 **add_credential_request** | [**AddCredentialRequest**](AddCredentialRequest.md)|  | 

### Return type

[**GetCredential200Response**](GetCredential200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **userveria**
> userveria()

Exchange a my stantabcorp (userveria) token for an Accounting Token

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint


accounting = accounting_sh.Accounting("access_token")
try:
    # Exchange a my stantabcorp (userveria) token for an Accounting Token
    api_response = accounting.credentials_api.userveria()
    print("The response of CredentialsApi->userveria:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->userveria: %s\n" % e)

```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Userveria200Response**](Userveria200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

