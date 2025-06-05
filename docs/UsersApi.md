# accounting_sh.UsersApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user**](UsersApi.md#add_user) | **POST** /users | Add user
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /users/{uuid} | Delete user
[**get_user**](UsersApi.md#get_user) | **GET** /users/{uuid} | View user
[**list_users**](UsersApi.md#list_users) | **GET** /users | List company&#39;s users
[**update_user**](UsersApi.md#update_user) | **PUT** /users/{uuid} | Update user
[**users_companies**](UsersApi.md#users_companies) | **GET** /users/me/companies | List current user companies
[**users_me**](UsersApi.md#users_me) | **GET** /users/me | View current user details


# **add_user**
> add_user(add_user_request)

Add user

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_user_request = accounting_sh.AddUserRequest() # AddUserRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Add user
    api_response = accounting.users_api.add_user(add_user_request)
    print("The response of UsersApi->add_user:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->add_user: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_user_request** | [**AddUserRequest**](AddUserRequest.md)|  | 

### Return type

[**AddUser200Response**](AddUser200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(uuid)

Delete user

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The user uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete user
    api_response = accounting.users_api.delete_user(uuid)
    print("The response of UsersApi->delete_user:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->delete_user: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The user uuid | 

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

# **get_user**
> get_user(uuid)

View user

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The user uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # View user
    api_response = accounting.users_api.get_user(uuid)
    print("The response of UsersApi->get_user:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The user uuid | 

### Return type

[**AddUser200Response**](AddUser200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> list_users(fields=fields, page=page, per_page=per_page)

List company's users

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = 'fields_example' # str | A comma separated list of fields requested in the response (optional)
page = 'page_example' # str | The response page (optional)
per_page = 'per_page_example' # str | The number of items per page (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's users
    api_response = accounting.users_api.list_users(fields=fields, page=page, per_page=per_page)
    print("The response of UsersApi->list_users:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->list_users: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| A comma separated list of fields requested in the response | [optional] 
 **page** | **str**| The response page | [optional] 
 **per_page** | **str**| The number of items per page | [optional] 

### Return type

[**ListUsers200Response**](ListUsers200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> update_user(uuid, update_user_request)

Update user

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The user uuid
update_user_request = accounting_sh.UpdateUserRequest() # UpdateUserRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Update user
    api_response = accounting.users_api.update_user(uuid, update_user_request)
    print("The response of UsersApi->update_user:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_user: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The user uuid | 
 **update_user_request** | [**UpdateUserRequest**](UpdateUserRequest.md)|  | 

### Return type

[**AddUser200Response**](AddUser200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_companies**
> users_companies()

List current user companies

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint


accounting = accounting_sh.Accounting("access_token")
try:
    # List current user companies
    api_response = accounting.users_api.users_companies()
    print("The response of UsersApi->users_companies:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_companies: %s\n" % e)

```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UsersCompanies200Response**](UsersCompanies200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_me**
> users_me()

View current user details

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint


accounting = accounting_sh.Accounting("access_token")
try:
    # View current user details
    api_response = accounting.users_api.users_me()
    print("The response of UsersApi->users_me:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_me: %s\n" % e)

```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UsersMe200Response**](UsersMe200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

