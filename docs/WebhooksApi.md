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

Add a webhook. Send the resource fields in the request body; the response contains the saved record. Requires at least one permission: `add.webhook`. Requires company feature(s): `webhooks`. Returns 402 if unavailable.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_webhook_request = accounting_sh.AddWebhookRequest() # AddWebhookRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

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
 **add_webhook_request** | [**AddWebhookRequest**](AddWebhookRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**AddWebhook200Response**](AddWebhook200Response.md)

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

# **delete_webhook**
> delete_webhook(uuid)

Delete a webhook

Delete a webhook. This action deletes the selected record. Review references to it before deletion. Requires at least one permission: `delete.webhook`. Requires company feature(s): `webhooks`. Returns 402 if unavailable.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The webhook uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete a webhook
    api_response = accounting.webhooks_api.delete_webhook(uuid)
    print("The response of WebhooksApi->delete_webhook:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->delete_webhook: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The webhook uuid | 

### Return type

[**AddWebhook200Response**](AddWebhook200Response.md)

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

# **get_webhook**
> get_webhook(uuid)

Get a webhook

Get a webhook. Use the identifier returned by the corresponding list or create operation. Requires at least one permission: `view.webhook`. Requires company feature(s): `webhooks`. Returns 402 if unavailable.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The webhook uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a webhook
    api_response = accounting.webhooks_api.get_webhook(uuid)
    print("The response of WebhooksApi->get_webhook:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->get_webhook: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The webhook uuid | 

### Return type

[**AddWebhook200Response**](AddWebhook200Response.md)

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

# **get_webhook_history**
> get_webhook_history(uuid)

Get webhook's history

Retrieve delivery history for this webhook to inspect previous attempts and troubleshoot delivery failures. Requires at least one permission: `view.webhook`. Requires company feature(s): `webhooks`. Returns 402 if unavailable.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The webhook uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get webhook's history
    api_response = accounting.webhooks_api.get_webhook_history(uuid)
    print("The response of WebhooksApi->get_webhook_history:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->get_webhook_history: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The webhook uuid | 

### Return type

[**GetWebhookHistory200Response**](GetWebhookHistory200Response.md)

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

# **list_webhook_events**
> list_webhook_events()

List available webhook events

Retrieve event identifiers accepted when creating or updating a webhook subscription.

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
> list_webhooks(fields=fields, page=page, per_page=per_page, order_by=order_by)

List company's webhooks

List company's webhooks. Retrieve records using the query parameters below. Requires at least one permission: `list.webhooks`. Requires company feature(s): `webhooks`. Returns 402 if unavailable.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = 'uuid,link,events' # str | Comma-separated fields to include in each record. Default fields: uuid, link, events. (optional)
page = 1 # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10 # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = 'created_at:desc' # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's webhooks
    api_response = accounting.webhooks_api.list_webhooks(fields=fields, page=page, per_page=per_page, order_by=order_by)
    print("The response of WebhooksApi->list_webhooks:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->list_webhooks: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Comma-separated fields to include in each record. Default fields: uuid, link, events. | [optional] 
 **page** | **int**| Page number, starting at 1. Values below 1 are treated as 1. | [optional] [default to 1]
 **per_page** | **int**| Records per page. The server caps page size to 100. Values below 1 use that maximum. | [optional] [default to 10]
 **order_by** | **str**| Sort by a supported field and direction, using field:asc or field:desc. | [optional] 

### Return type

[**ListWebhooks200Response**](ListWebhooks200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**402** | The company does not have the required feature. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook**
> update_webhook(uuid, add_webhook_request)

Update a webhook

Update a webhook. Send the fields accepted by this operation in the request body. Requires at least one permission: `edit.webhook`. Requires company feature(s): `webhooks`. Returns 402 if unavailable.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The webhook uuid
add_webhook_request = accounting_sh.AddWebhookRequest() # AddWebhookRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a webhook
    api_response = accounting.webhooks_api.update_webhook(uuid, add_webhook_request)
    print("The response of WebhooksApi->update_webhook:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->update_webhook: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The webhook uuid | 
 **add_webhook_request** | [**AddWebhookRequest**](AddWebhookRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**AddWebhook200Response**](AddWebhook200Response.md)

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

