# accounting_sh.AuthApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_init**](AuthApi.md#auth_init) | **GET** /auth/init | Init authentication process
[**login**](AuthApi.md#login) | **POST** /auth/login | Login user
[**login_get_alias**](AuthApi.md#login_get_alias) | **GET** /auth/login | Login user
[**logout**](AuthApi.md#logout) | **GET** /auth/logout | Logout current user
[**switch_company**](AuthApi.md#switch_company) | **POST** /auth/switch | Switch to a different company


# **auth_init**
> auth_init()

Init authentication process

Retrieve the authorization URL used to start interactive OAuth sign-in. Open the returned URL in a browser, then use the authorization code with /auth/login.

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint


accounting = accounting_sh.Accounting("access_token")
try:
    # Init authentication process
    api_response = accounting.auth_api.auth_init()
    print("The response of AuthApi->auth_init:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_init: %s\n" % e)

```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AuthInit200Response**](AuthInit200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login**
> login(login_get_alias_request)

Login user

Exchange the OAuth authorization code for a browser session. Use the resulting session for subsequent user requests.

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

login_get_alias_request = accounting_sh.LoginGetAliasRequest() # LoginGetAliasRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Login user
    api_response = accounting.auth_api.login(login_get_alias_request)
    print("The response of AuthApi->login:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->login: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_get_alias_request** | [**LoginGetAliasRequest**](LoginGetAliasRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

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
**503** | Identity provider unavailable, timed out or returned an invalid response. Retry after the Retry-After delay. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_get_alias**
> login_get_alias(login_get_alias_request)

Login user

Exchange the OAuth authorization code for a browser session. Use the resulting session for subsequent user requests. Equivalent to POST /auth/login.

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

login_get_alias_request = accounting_sh.LoginGetAliasRequest() # LoginGetAliasRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Login user
    api_response = accounting.auth_api.login_get_alias(login_get_alias_request)
    print("The response of AuthApi->login_get_alias:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->login_get_alias: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_get_alias_request** | [**LoginGetAliasRequest**](LoginGetAliasRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

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
**503** | Identity provider unavailable, timed out or returned an invalid response. Retry after the Retry-After delay. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout**
> logout()

Logout current user

Sign out the current user. This endpoint changes session state and should not be prefetched.

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint


accounting = accounting_sh.Accounting("access_token")
try:
    # Logout current user
    api_response = accounting.auth_api.logout()
    print("The response of AuthApi->logout:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->logout: %s\n" % e)

```



### Parameters

This endpoint does not need any parameter.

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

# **switch_company**
> switch_company(switch_company_request)

Switch to a different company

Switch the current user session to a company in which the user has a membership. Send the company identifier in the JSON body. This requires a user session; a company API credential does not identify a user. Requires authentication.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

switch_company_request = accounting_sh.SwitchCompanyRequest() # SwitchCompanyRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Switch to a different company
    api_response = accounting.auth_api.switch_company(switch_company_request)
    print("The response of AuthApi->switch_company:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->switch_company: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **switch_company_request** | [**SwitchCompanyRequest**](SwitchCompanyRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

