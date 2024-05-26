# accounting_sh.WebhooksApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_webhook**](WebhooksApi.md#add_webhook) | **POST** /webhooks | Add a webhook
[**delete_webhook**](WebhooksApi.md#delete_webhook) | **DELETE** /webhooks/{uuid} | Delete a webhook
[**get_webhook**](WebhooksApi.md#get_webhook) | **GET** /webhooks/{uuid} | Get a webhook
[**get_webhook_history**](WebhooksApi.md#get_webhook_history) | **GET** /webhooks/{uuid}/history | Get webhook&#39;s history
[**list_webhook_events**](WebhooksApi.md#list_webhook_events) | **GET** /webhooks/events | List available webhook events
[**list_webhooks**](WebhooksApi.md#list_webhooks) | **GET** /webhooks | List company&#39;s webhooks
[**update_webhook**](WebhooksApi.md#update_webhook) | **PUT** /webhooks/{uuid} | Update a webhook


# **add_webhook**
> add_webhook(add_webhook_request)

Add a webhook

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_webhook_request = accounting_sh.AddWebhookRequest() # AddWebhookRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Add a webhook
    api_response = accounting.webhooks_api.add_webhook(add_webhook_request)
    print("The response of WebhooksApi->add_webhook:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->add_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_webhook_request** | [**AddWebhookRequest**](AddWebhookRequest.md)|  | 

### Return type

[**AddWebhook200Response**](AddWebhook200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhook**
> delete_webhook(uuid=uuid)

Delete a webhook

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The webhook uuid (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete a webhook
    api_response = accounting.webhooks_api.delete_webhook(uuid=uuid)
    print("The response of WebhooksApi->delete_webhook:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->delete_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The webhook uuid | [optional] 

### Return type

[**AddWebhook200Response**](AddWebhook200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook**
> get_webhook(uuid=uuid)

Get a webhook

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The webhook uuid (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a webhook
    api_response = accounting.webhooks_api.get_webhook(uuid=uuid)
    print("The response of WebhooksApi->get_webhook:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->get_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The webhook uuid | [optional] 

### Return type

[**AddWebhook200Response**](AddWebhook200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook_history**
> get_webhook_history(uuid=uuid)

Get webhook's history

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The webhook uuid (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # Get webhook's history
    api_response = accounting.webhooks_api.get_webhook_history(uuid=uuid)
    print("The response of WebhooksApi->get_webhook_history:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->get_webhook_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The webhook uuid | [optional] 

### Return type

[**GetWebhookHistory200Response**](GetWebhookHistory200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_webhook_events**
> list_webhook_events()

List available webhook events

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint


accounting = accounting_sh.Accounting("access_token")
try:
    # List available webhook events
    api_response = accounting.webhooks_api.list_webhook_events()
    print("The response of WebhooksApi->list_webhook_events:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->list_webhook_events: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListWebhookEvents200Response**](ListWebhookEvents200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List every available webhook events |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_webhooks**
> list_webhooks(fields=fields, page=page, per_page=per_page)

List company's webhooks

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
    # List company's webhooks
    api_response = accounting.webhooks_api.list_webhooks(fields=fields, page=page, per_page=per_page)
    print("The response of WebhooksApi->list_webhooks:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->list_webhooks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| A comma separated list of fields requested in the response | [optional] 
 **page** | **str**| The response page | [optional] 
 **per_page** | **str**| The number of items per page | [optional] 

### Return type

[**ListWebhooks200Response**](ListWebhooks200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook**
> update_webhook(add_webhook_request, uuid=uuid)

Update a webhook

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_webhook_request = accounting_sh.AddWebhookRequest() # AddWebhookRequest | 
uuid = 'uuid_example' # str | The webhook uuid (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a webhook
    api_response = accounting.webhooks_api.update_webhook(add_webhook_request, uuid=uuid)
    print("The response of WebhooksApi->update_webhook:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->update_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_webhook_request** | [**AddWebhookRequest**](AddWebhookRequest.md)|  | 
 **uuid** | **str**| The webhook uuid | [optional] 

### Return type

[**AddWebhook200Response**](AddWebhook200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

