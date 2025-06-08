# accounting_sh.OAuthConfigApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_o_auth_configuration**](OAuthConfigApi.md#add_o_auth_configuration) | **POST** /oauth | Add an OAuth configuration
[**delete_o_auth_configuration**](OAuthConfigApi.md#delete_o_auth_configuration) | **DELETE** /oauth/{uuid} | Delete an oauth configuration
[**get_o_auth_configuration**](OAuthConfigApi.md#get_o_auth_configuration) | **GET** /oauth/{uuid} | Get an OAuth configuration
[**list_o_auth_configurations**](OAuthConfigApi.md#list_o_auth_configurations) | **GET** /oauth | List company&#39;s oauth configurations
[**list_providers**](OAuthConfigApi.md#list_providers) | **GET** /oauth/providers | List available providers
[**update_o_auth_configuration**](OAuthConfigApi.md#update_o_auth_configuration) | **PUT** /oauth/{uuid} | Update an oauth configuration


# **add_o_auth_configuration**
> add_o_auth_configuration(add_o_auth_configuration_request)

Add an OAuth configuration

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_o_auth_configuration_request = accounting_sh.AddOAuthConfigurationRequest() # AddOAuthConfigurationRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Add an OAuth configuration
    api_response = accounting.o_auth_config_api.add_o_auth_configuration(add_o_auth_configuration_request)
    print("The response of OAuthConfigApi->add_o_auth_configuration:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthConfigApi->add_o_auth_configuration: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_o_auth_configuration_request** | [**AddOAuthConfigurationRequest**](AddOAuthConfigurationRequest.md)|  | 

### Return type

[**AddOAuthConfiguration200Response**](AddOAuthConfiguration200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_o_auth_configuration**
> delete_o_auth_configuration(uuid)

Delete an oauth configuration

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The oauth configuration uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete an oauth configuration
    api_response = accounting.o_auth_config_api.delete_o_auth_configuration(uuid)
    print("The response of OAuthConfigApi->delete_o_auth_configuration:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthConfigApi->delete_o_auth_configuration: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The oauth configuration uuid | 

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

# **get_o_auth_configuration**
> get_o_auth_configuration(uuid)

Get an OAuth configuration

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The oauth configuration uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get an OAuth configuration
    api_response = accounting.o_auth_config_api.get_o_auth_configuration(uuid)
    print("The response of OAuthConfigApi->get_o_auth_configuration:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthConfigApi->get_o_auth_configuration: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The oauth configuration uuid | 

### Return type

[**AddOAuthConfiguration200Response**](AddOAuthConfiguration200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_o_auth_configurations**
> list_o_auth_configurations(fields=fields, page=page, per_page=per_page)

List company's oauth configurations

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
    # List company's oauth configurations
    api_response = accounting.o_auth_config_api.list_o_auth_configurations(fields=fields, page=page, per_page=per_page)
    print("The response of OAuthConfigApi->list_o_auth_configurations:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthConfigApi->list_o_auth_configurations: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| A comma separated list of fields requested in the response | [optional] 
 **page** | **str**| The response page | [optional] 
 **per_page** | **str**| The number of items per page | [optional] 

### Return type

[**ListOAuthConfigurations200Response**](ListOAuthConfigurations200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_providers**
> list_providers()

List available providers

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint


accounting = accounting_sh.Accounting("access_token")
try:
    # List available providers
    api_response = accounting.o_auth_config_api.list_providers()
    print("The response of OAuthConfigApi->list_providers:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthConfigApi->list_providers: %s\n" % e)

```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListProviders200Response**](ListProviders200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List every available oauth providers |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_o_auth_configuration**
> update_o_auth_configuration(uuid, add_o_auth_configuration_request)

Update an oauth configuration

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The oauth configuration uuid
add_o_auth_configuration_request = accounting_sh.AddOAuthConfigurationRequest() # AddOAuthConfigurationRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Update an oauth configuration
    api_response = accounting.o_auth_config_api.update_o_auth_configuration(uuid, add_o_auth_configuration_request)
    print("The response of OAuthConfigApi->update_o_auth_configuration:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthConfigApi->update_o_auth_configuration: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The oauth configuration uuid | 
 **add_o_auth_configuration_request** | [**AddOAuthConfigurationRequest**](AddOAuthConfigurationRequest.md)|  | 

### Return type

[**AddOAuthConfiguration200Response**](AddOAuthConfiguration200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

