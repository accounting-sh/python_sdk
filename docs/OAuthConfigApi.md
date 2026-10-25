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

Add an OAuth configuration. Send the resource fields in the request body; the response contains the saved record. Requires at least one permission: `oauth_config.add`. Requires company feature(s): `oauth`. Returns 402 if unavailable.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_o_auth_configuration_request = accounting_sh.AddOAuthConfigurationRequest() # AddOAuthConfigurationRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

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
 **add_o_auth_configuration_request** | [**AddOAuthConfigurationRequest**](AddOAuthConfigurationRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**AddOAuthConfiguration200Response**](AddOAuthConfiguration200Response.md)

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

# **delete_o_auth_configuration**
> delete_o_auth_configuration(uuid)

Delete an oauth configuration

Delete an oauth configuration. This action deletes the selected record. Review references to it before deletion. Requires at least one permission: `oauth_config.delete`. Requires company feature(s): `oauth`. Returns 402 if unavailable.

### Example

* Bearer (API key) Authentication (bearer):

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

# **get_o_auth_configuration**
> get_o_auth_configuration(uuid)

Get an OAuth configuration

Get an OAuth configuration. Use the identifier returned by the corresponding list or create operation. Requires at least one permission: `oauth_config.view`. Requires company feature(s): `oauth`. Returns 402 if unavailable.

### Example

* Bearer (API key) Authentication (bearer):

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
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |
**402** | The company does not have the required feature. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_o_auth_configurations**
> list_o_auth_configurations(fields=fields, page=page, per_page=per_page, order_by=order_by)

List company's oauth configurations

List company's oauth configurations. Retrieve records using the query parameters below. Requires at least one permission: `oauth_config.list`. Requires company feature(s): `oauth`. Returns 402 if unavailable.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = 'uuid,provider,client_id' # str | Comma-separated fields to include in each record. Default fields: uuid, provider, client_id. (optional)
page = 1 # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10 # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = 'created_at:desc' # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's oauth configurations
    api_response = accounting.o_auth_config_api.list_o_auth_configurations(fields=fields, page=page, per_page=per_page, order_by=order_by)
    print("The response of OAuthConfigApi->list_o_auth_configurations:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthConfigApi->list_o_auth_configurations: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Comma-separated fields to include in each record. Default fields: uuid, provider, client_id. | [optional] 
 **page** | **int**| Page number, starting at 1. Values below 1 are treated as 1. | [optional] [default to 1]
 **per_page** | **int**| Records per page. The server caps page size to 100. Values below 1 use that maximum. | [optional] [default to 10]
 **order_by** | **str**| Sort by a supported field and direction, using field:asc or field:desc. | [optional] 

### Return type

[**ListOAuthConfigurations200Response**](ListOAuthConfigurations200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**402** | The company does not have the required feature. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_providers**
> list_providers()

List available providers

Retrieve the supported OAuth providers before creating an OAuth configuration.

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

Update an oauth configuration. Send the fields accepted by this operation in the request body. Requires at least one permission: `oauth_config.edit`. Requires company feature(s): `oauth`. Returns 402 if unavailable.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The oauth configuration uuid
add_o_auth_configuration_request = accounting_sh.AddOAuthConfigurationRequest() # AddOAuthConfigurationRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

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
 **add_o_auth_configuration_request** | [**AddOAuthConfigurationRequest**](AddOAuthConfigurationRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**AddOAuthConfiguration200Response**](AddOAuthConfiguration200Response.md)

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

