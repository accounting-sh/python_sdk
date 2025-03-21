# accounting_sh.AuthApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_init**](AuthApi.md#auth_init) | **GET** /auth/init | Init authentication process
[**login**](AuthApi.md#login) | **POST** /auth/login | Login user
[**logout**](AuthApi.md#logout) | **GET** /auth/logout | Logout current user
[**switch_company**](AuthApi.md#switch_company) | **POST** /auth/switch | Switch to a different company


# **auth_init**
> auth_init()

Init authentication process

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
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login**
> login(login_request)

Login user

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

login_request = accounting_sh.LoginRequest() # LoginRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Login user
    api_response = accounting.auth_api.login(login_request)
    print("The response of AuthApi->login:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_request** | [**LoginRequest**](LoginRequest.md)|  | 

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

# **logout**
> logout()

Logout current user

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

# **switch_company**
> switch_company(switch_company_request)

Switch to a different company

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

switch_company_request = accounting_sh.SwitchCompanyRequest() # SwitchCompanyRequest | 

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
 **switch_company_request** | [**SwitchCompanyRequest**](SwitchCompanyRequest.md)|  | 

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

