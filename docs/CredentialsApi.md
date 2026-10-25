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


# **add_credential**
> add_credential(add_credential_request)

Add a credential

Add a credential. Send the resource fields in the request body; the response contains the saved record. Requires at least one permission: `add.credential`. Requires company feature(s): `api`. Returns 402 if unavailable.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_credential_request = accounting_sh.AddCredentialRequest() # AddCredentialRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

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
 **add_credential_request** | [**AddCredentialRequest**](AddCredentialRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**AddCredential200Response**](AddCredential200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**400** | The request failed validation or could not be processed. Inspect errors, correct the input, and try again. |  -  |
**402** | The company does not have the required feature. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_credential**
> delete_credential(uuid)

Delete a credential

Delete a credential. This action deletes the selected record. Review references to it before deletion. Requires at least one permission: `delete.credential`.

### Example

* Bearer (API key) Authentication (bearer):

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

# **get_credential**
> get_credential(uuid)

Get a credential

Get a credential. Use the identifier returned by the corresponding list or create operation. Requires at least one permission: `view.credential`.

### Example

* Bearer (API key) Authentication (bearer):

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
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_credentials**
> list_credentials(fields=fields, page=page, per_page=per_page, order_by=order_by)

List company's credentials

List company's credentials. Retrieve records using the query parameters below. Requires at least one permission: `list.credentials`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = 'uuid,permissions,expired_at' # str | Comma-separated fields to include in each record. Default fields: uuid, permissions, expired_at. (optional)
page = 1 # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10 # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = 'created_at:desc' # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's credentials
    api_response = accounting.credentials_api.list_credentials(fields=fields, page=page, per_page=per_page, order_by=order_by)
    print("The response of CredentialsApi->list_credentials:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->list_credentials: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Comma-separated fields to include in each record. Default fields: uuid, permissions, expired_at. | [optional] 
 **page** | **int**| Page number, starting at 1. Values below 1 are treated as 1. | [optional] [default to 1]
 **per_page** | **int**| Records per page. The server caps page size to 100. Values below 1 use that maximum. | [optional] [default to 10]
 **order_by** | **str**| Sort by a supported field and direction, using field:asc or field:desc. | [optional] 

### Return type

[**ListCredentials200Response**](ListCredentials200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_permissions**
> list_permissions()

List available permissions

Retrieve the permission identifiers available for API credentials. Use these values in the permissions array when creating or updating a credential.

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

Inspect the current company API credential, including its permissions and expiry. Use a Bearer API credential; a browser session token is not an API credential. Requires authentication.

### Example

* Bearer (API key) Authentication (bearer):

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
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_credential**
> update_credential(uuid, add_credential_request)

Update a credential

Update a credential. Send the fields accepted by this operation in the request body. Requires at least one permission: `edit.credential`. Requires company feature(s): `api`. Returns 402 if unavailable.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The credential uuid
add_credential_request = accounting_sh.AddCredentialRequest() # AddCredentialRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

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
 **add_credential_request** | [**AddCredentialRequest**](AddCredentialRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**GetCredential200Response**](GetCredential200Response.md)

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

