# accounting_sh.FRSuperPDPApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fr_super_pdp_approve**](FRSuperPDPApi.md#fr_super_pdp_approve) | **PUT** /fr/superpdp/inbox/{uuid}/approve | Approve a received invoice
[**fr_super_pdp_authorize**](FRSuperPDPApi.md#fr_super_pdp_authorize) | **POST** /fr/superpdp/authorize | Create a SuperPDP consent URL
[**fr_super_pdp_callback**](FRSuperPDPApi.md#fr_super_pdp_callback) | **POST** /fr/superpdp/callback | Complete SuperPDP consent
[**fr_super_pdp_classify**](FRSuperPDPApi.md#fr_super_pdp_classify) | **PUT** /fr/superpdp/operations/{uuid}/classification | Classify reporting lines
[**fr_super_pdp_configure**](FRSuperPDPApi.md#fr_super_pdp_configure) | **PUT** /fr/superpdp/settings | Configure SuperPDP synchronization
[**fr_super_pdp_disconnect**](FRSuperPDPApi.md#fr_super_pdp_disconnect) | **DELETE** /fr/superpdp | Disconnect SuperPDP
[**fr_super_pdp_inbox**](FRSuperPDPApi.md#fr_super_pdp_inbox) | **GET** /fr/superpdp/inbox | List received invoices
[**fr_super_pdp_lifecycle**](FRSuperPDPApi.md#fr_super_pdp_lifecycle) | **POST** /fr/superpdp/operations/{uuid}/events | Queue a buyer lifecycle event
[**fr_super_pdp_operations**](FRSuperPDPApi.md#fr_super_pdp_operations) | **GET** /fr/superpdp/operations | List SuperPDP operations
[**fr_super_pdp_receipt**](FRSuperPDPApi.md#fr_super_pdp_receipt) | **GET** /fr/superpdp/inbox/{uuid} | Get a received invoice
[**fr_super_pdp_receipt_history**](FRSuperPDPApi.md#fr_super_pdp_receipt_history) | **GET** /fr/superpdp/inbox/{uuid}/history | Get received invoice history
[**fr_super_pdp_receipt_pdf**](FRSuperPDPApi.md#fr_super_pdp_receipt_pdf) | **GET** /fr/superpdp/inbox/{uuid}/pdf | Get a received invoice PDF
[**fr_super_pdp_reconcile**](FRSuperPDPApi.md#fr_super_pdp_reconcile) | **PUT** /fr/superpdp/operations/{uuid}/reconcile | Reconcile a reporting submission
[**fr_super_pdp_refuse**](FRSuperPDPApi.md#fr_super_pdp_refuse) | **PUT** /fr/superpdp/inbox/{uuid}/refuse | Refuse a received invoice
[**fr_super_pdp_retry**](FRSuperPDPApi.md#fr_super_pdp_retry) | **PUT** /fr/superpdp/operations/{uuid}/retry | Retry a SuperPDP operation
[**fr_super_pdp_settings**](FRSuperPDPApi.md#fr_super_pdp_settings) | **GET** /fr/superpdp/settings | Get SuperPDP settings
[**fr_super_pdp_status**](FRSuperPDPApi.md#fr_super_pdp_status) | **GET** /fr/superpdp | Get SuperPDP connection status
[**fr_super_pdp_submit**](FRSuperPDPApi.md#fr_super_pdp_submit) | **POST** /fr/superpdp/submit | Submit an issued invoice
[**fr_super_pdp_sync**](FRSuperPDPApi.md#fr_super_pdp_sync) | **POST** /fr/superpdp/sync | Queue SuperPDP synchronization
[**fr_super_pdp_verify**](FRSuperPDPApi.md#fr_super_pdp_verify) | **POST** /fr/superpdp/verify | Queue SuperPDP verification


# **fr_super_pdp_approve**
> fr_super_pdp_approve(uuid)

Approve a received invoice

Record human approval and queue import of the exact reviewed PDF; duplicate approvals do not create another bill. Requires the `add.bill` permission and the `einvoicing` company feature.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Approve a received invoice
   accounting.fr_super_pdp_api.fr_super_pdp_approve(uuid)
except ApiException as e:
    print("Exception when calling FRSuperPDPApi->fr_super_pdp_approve: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

void (empty response body)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**402** | Company feature einvoicing is required. |  -  |
**202** | Approval retained, fr:205 and bill import queued. Poll invoice detail for the resulting bill UUID. |  -  |
**409** | Invoice is not ready for review or was already refused. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fr_super_pdp_authorize**
> fr_super_pdp_authorize()

Create a SuperPDP consent URL

Create a consent URL for the authenticated company without exposing provider credentials. Requires the `edit.company` permission and the `einvoicing` company feature.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint


accounting = accounting_sh.Accounting("access_token")
try:
    # Create a SuperPDP consent URL
   accounting.fr_super_pdp_api.fr_super_pdp_authorize()
except ApiException as e:
    print("Exception when calling FRSuperPDPApi->fr_super_pdp_authorize: %s\n" % e)

```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**402** | Company feature einvoicing is required. |  -  |
**200** | Consent URL in authorization_url; expires after ten minutes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fr_super_pdp_callback**
> fr_super_pdp_callback(fr_super_pdp_callback_request)

Complete SuperPDP consent

The configured frontend callback forwards code/state using its existing authenticated company session. Requires the `edit.company` permission and the `einvoicing` company feature.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fr_super_pdp_callback_request = accounting_sh.FrSuperPdpCallbackRequest() # FrSuperPdpCallbackRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Complete SuperPDP consent
   accounting.fr_super_pdp_api.fr_super_pdp_callback(fr_super_pdp_callback_request)
except ApiException as e:
    print("Exception when calling FRSuperPDPApi->fr_super_pdp_callback: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fr_super_pdp_callback_request** | [**FrSuperPdpCallbackRequest**](FrSuperPdpCallbackRequest.md)|  | 

### Return type

void (empty response body)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**402** | Company feature einvoicing is required. |  -  |
**200** | Connection metadata; company verification runs asynchronously. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fr_super_pdp_classify**
> fr_super_pdp_classify(uuid, fr_super_pdp_classify_request)

Classify reporting lines

Validate a complete per-line goods/services classification for a mixed consumer sale awaiting submission. Requires the `edit.company` permission and the `einvoicing` company feature.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | 
fr_super_pdp_classify_request = accounting_sh.FrSuperPdpClassifyRequest() # FrSuperPdpClassifyRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Classify reporting lines
   accounting.fr_super_pdp_api.fr_super_pdp_classify(uuid, fr_super_pdp_classify_request)
except ApiException as e:
    print("Exception when calling FRSuperPDPApi->fr_super_pdp_classify: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **fr_super_pdp_classify_request** | [**FrSuperPdpClassifyRequest**](FrSuperPdpClassifyRequest.md)|  | 

### Return type

void (empty response body)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**402** | Company feature einvoicing is required. |  -  |
**202** | Reporting classification retained; immutable issued amounts remain unchanged. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fr_super_pdp_configure**
> fr_super_pdp_configure(fr_super_pdp_configure_request)

Configure SuperPDP synchronization

Validate backfill/routing; legacy frequency inputs are adapted to shared settings with their standard edit permission. Requires the `edit.company` permission and the `einvoicing` company feature.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fr_super_pdp_configure_request = accounting_sh.FrSuperPdpConfigureRequest() # FrSuperPdpConfigureRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Configure SuperPDP synchronization
   accounting.fr_super_pdp_api.fr_super_pdp_configure(fr_super_pdp_configure_request)
except ApiException as e:
    print("Exception when calling FRSuperPDPApi->fr_super_pdp_configure: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fr_super_pdp_configure_request** | [**FrSuperPdpConfigureRequest**](FrSuperPdpConfigureRequest.md)|  | 

### Return type

void (empty response body)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**402** | Company feature einvoicing is required. |  -  |
**202** | Backfill/routing saved. VAT options and filing frequency use shared company settings. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fr_super_pdp_disconnect**
> fr_super_pdp_disconnect()

Disconnect SuperPDP

Delete local OAuth secrets; provider-side consent remains manageable from SuperPDP. Requires the `edit.company` permission and the `einvoicing` company feature.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint


accounting = accounting_sh.Accounting("access_token")
try:
    # Disconnect SuperPDP
   accounting.fr_super_pdp_api.fr_super_pdp_disconnect()
except ApiException as e:
    print("Exception when calling FRSuperPDPApi->fr_super_pdp_disconnect: %s\n" % e)

```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**402** | Company feature einvoicing is required. |  -  |
**200** | Local connection removed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fr_super_pdp_inbox**
> fr_super_pdp_inbox(page=page, review_status=review_status)

List received invoices

List owned received invoices, defaulting to pending review while allowing all historical review states. Requires the `list.bills` permission and the `einvoicing` company feature.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

page = 56 # int |  (optional)
review_status = 'pending' # str |  (optional) (default to 'pending')

accounting = accounting_sh.Accounting("access_token")
try:
    # List received invoices
   accounting.fr_super_pdp_api.fr_super_pdp_inbox(page=page, review_status=review_status)
except ApiException as e:
    print("Exception when calling FRSuperPDPApi->fr_super_pdp_inbox: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **review_status** | **str**|  | [optional] [default to &#39;pending&#39;]

### Return type

void (empty response body)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**402** | Company feature einvoicing is required. |  -  |
**200** | Received invoices, 50 per page. Defaults to pending; review_status&#x3D;all includes historical receipts. Each includes review/import status, linked bill UUID/status/URL, observed provider status codes and history/PDF URLs. |  -  |
**400** | Invalid page or review_status. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fr_super_pdp_lifecycle**
> fr_super_pdp_lifecycle(uuid, fr_super_pdp_lifecycle_request)

Queue a buyer lifecycle event

Queue a buyer lifecycle decision with a client UUID to make repeated HTTP requests idempotent. Requires the `edit.company` permission and the `einvoicing` company feature.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | 
fr_super_pdp_lifecycle_request = accounting_sh.FrSuperPdpLifecycleRequest() # FrSuperPdpLifecycleRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Queue a buyer lifecycle event
   accounting.fr_super_pdp_api.fr_super_pdp_lifecycle(uuid, fr_super_pdp_lifecycle_request)
except ApiException as e:
    print("Exception when calling FRSuperPDPApi->fr_super_pdp_lifecycle: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **fr_super_pdp_lifecycle_request** | [**FrSuperPdpLifecycleRequest**](FrSuperPdpLifecycleRequest.md)|  | 

### Return type

void (empty response body)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**402** | Company feature einvoicing is required. |  -  |
**202** | Buyer lifecycle action queued for an owned received invoice. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fr_super_pdp_operations**
> fr_super_pdp_operations(page=page, kind=kind)

List SuperPDP operations

Return bounded local invoice, inbox, lifecycle, reporting and failure records. Requires the `edit.company` permission and the `einvoicing` company feature.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

page = 56 # int |  (optional)
kind = 'kind_example' # str |  (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List SuperPDP operations
   accounting.fr_super_pdp_api.fr_super_pdp_operations(page=page, kind=kind)
except ApiException as e:
    print("Exception when calling FRSuperPDPApi->fr_super_pdp_operations: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **kind** | **str**|  | [optional] 

### Return type

void (empty response body)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**402** | Company feature einvoicing is required. |  -  |
**200** | Operations with status, provider IDs, errors and document/bill links; 50 per page. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fr_super_pdp_receipt**
> fr_super_pdp_receipt(uuid)

Get a received invoice

Return structured supplier/line/total facts and review/import state without creating accounting resources. Requires the `view.bill` permission and the `einvoicing` company feature.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a received invoice
   accounting.fr_super_pdp_api.fr_super_pdp_receipt(uuid)
except ApiException as e:
    print("Exception when calling FRSuperPDPApi->fr_super_pdp_receipt: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

void (empty response body)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**402** | Company feature einvoicing is required. |  -  |
**200** | Received invoice facts, PDF/history URLs, reviewer audit, observed provider status codes and resulting bill UUID/status/URL and document UUID when imported. |  -  |
**404** | Receipt not owned by the authenticated company. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fr_super_pdp_receipt_history**
> fr_super_pdp_receipt_history(uuid, page=page)

Get received invoice history

Retrieve one receipt's retained provider events and local lifecycle delivery outcomes without any provider calls. Requires the `view.bill` permission and the `einvoicing` company feature.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | 
page = 56 # int |  (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # Get received invoice history
   accounting.fr_super_pdp_api.fr_super_pdp_receipt_history(uuid, page=page)
except ApiException as e:
    print("Exception when calling FRSuperPDPApi->fr_super_pdp_receipt_history: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **page** | **int**|  | [optional] 

### Return type

void (empty response body)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**402** | Company feature einvoicing is required. |  -  |
**200** | Receipt including review audit and linked bill status, plus paginated events ordered newest recorded first. Event fields: source accounting/superpdp, status_code, reason, occurred_at, recorded_at, delivery status and last_error. The linked bill detail endpoint exposes its accounting status_history. |  -  |
**404** | Receipt not owned by the authenticated company. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fr_super_pdp_receipt_pdf**
> fr_super_pdp_receipt_pdf(uuid)

Get a received invoice PDF

Serve the exact private S3 PDF used for approval; callers should display it in a sandboxed PDF viewer. Requires the `view.bill` permission and the `einvoicing` company feature.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a received invoice PDF
   accounting.fr_super_pdp_api.fr_super_pdp_receipt_pdf(uuid)
except ApiException as e:
    print("Exception when calling FRSuperPDPApi->fr_super_pdp_receipt_pdf: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

void (empty response body)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**402** | Company feature einvoicing is required. |  -  |
**200** | Private application/pdf for inline review; bearer authentication required. |  -  |
**409** | Preview is still being prepared or unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fr_super_pdp_reconcile**
> fr_super_pdp_reconcile(uuid, fr_super_pdp_reconcile_request)

Reconcile a reporting submission

Queue proof checking for an ambiguous reporting submission, without posting its tax facts again. Requires the `edit.company` permission and the `einvoicing` company feature.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | 
fr_super_pdp_reconcile_request = accounting_sh.FrSuperPdpReconcileRequest() # FrSuperPdpReconcileRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Reconcile a reporting submission
   accounting.fr_super_pdp_api.fr_super_pdp_reconcile(uuid, fr_super_pdp_reconcile_request)
except ApiException as e:
    print("Exception when calling FRSuperPDPApi->fr_super_pdp_reconcile: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **fr_super_pdp_reconcile_request** | [**FrSuperPdpReconcileRequest**](FrSuperPdpReconcileRequest.md)|  | 

### Return type

void (empty response body)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**402** | Company feature einvoicing is required. |  -  |
**202** | Acceptance proof checking queued; no tax data is resent. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fr_super_pdp_refuse**
> fr_super_pdp_refuse(uuid, fr_super_pdp_refuse_request)

Refuse a received invoice

Record a reason-coded refusal and queue fr:210 without creating a bill, contact or document. Requires the `edit.bill` permission and the `einvoicing` company feature.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | 
fr_super_pdp_refuse_request = accounting_sh.FrSuperPdpRefuseRequest() # FrSuperPdpRefuseRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Refuse a received invoice
   accounting.fr_super_pdp_api.fr_super_pdp_refuse(uuid, fr_super_pdp_refuse_request)
except ApiException as e:
    print("Exception when calling FRSuperPDPApi->fr_super_pdp_refuse: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **fr_super_pdp_refuse_request** | [**FrSuperPdpRefuseRequest**](FrSuperPdpRefuseRequest.md)|  | 

### Return type

void (empty response body)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**402** | Company feature einvoicing is required. |  -  |
**202** | Refusal and reason retained; fr:210 queued, no bill is imported. |  -  |
**400** | refusal_reason_required when reason is missing or blank; invalid_refusal_reason when it is not one of the supported SuperPDP refusal reason codes. |  -  |
**409** | Invoice is not ready for review or was already approved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fr_super_pdp_retry**
> fr_super_pdp_retry(uuid, fr_super_pdp_retry_request=fr_super_pdp_retry_request)

Retry a SuperPDP operation

Retry failures, requiring an explicit provider nonreceipt check before replaying an ambiguous POST. Requires the `edit.company` permission and the `einvoicing` company feature.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | 
fr_super_pdp_retry_request = accounting_sh.FrSuperPdpRetryRequest() # FrSuperPdpRetryRequest |  (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # Retry a SuperPDP operation
   accounting.fr_super_pdp_api.fr_super_pdp_retry(uuid, fr_super_pdp_retry_request=fr_super_pdp_retry_request)
except ApiException as e:
    print("Exception when calling FRSuperPDPApi->fr_super_pdp_retry: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **fr_super_pdp_retry_request** | [**FrSuperPdpRetryRequest**](FrSuperPdpRetryRequest.md)|  | [optional] 

### Return type

void (empty response body)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**402** | Company feature einvoicing is required. |  -  |
**202** | Retry retained; uncertain submissions require explicit nonreceipt confirmation. |  -  |
**409** | Invalid operation state or uncertain submission. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fr_super_pdp_settings**
> fr_super_pdp_settings()

Get SuperPDP settings

Read the synchronized projection of company VAT settings, provider filing frequency and the local backfill boundary. Requires the `edit.company` permission and the `einvoicing` company feature.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint


accounting = accounting_sh.Accounting("access_token")
try:
    # Get SuperPDP settings
   accounting.fr_super_pdp_api.fr_super_pdp_settings()
except ApiException as e:
    print("Exception when calling FRSuperPDPApi->fr_super_pdp_settings: %s\n" % e)

```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**402** | Company feature einvoicing is required. |  -  |
**200** | since, synchronized VAT settings, shared vat_filing_frequency, required_settings and latest synchronization error. Set missing frequency using the existing company settings endpoint. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fr_super_pdp_status**
> fr_super_pdp_status()

Get SuperPDP connection status

Read safe local status and request a throttled asynchronous refresh when verification/synchronization is stale. Requires the `view.company` permission and the `einvoicing` company feature.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint


accounting = accounting_sh.Accounting("access_token")
try:
    # Get SuperPDP connection status
   accounting.fr_super_pdp_api.fr_super_pdp_status()
except ApiException as e:
    print("Exception when calling FRSuperPDPApi->fr_super_pdp_status: %s\n" % e)

```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**402** | Company feature einvoicing is required. |  -  |
**200** | Local connection, readiness, verification_checked_at, last_verification_error, last_verification_http_status and sync_requested_at. Stale connected grants wake an asynchronous sync at most once per minute; no provider request is performed inline. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fr_super_pdp_submit**
> fr_super_pdp_submit(fr_super_pdp_submit_request)

Submit an issued invoice

Opt an existing issued source into delivery/reporting; drafts and foreign-owned UUIDs are rejected. Requires the `edit.company` permission and the `einvoicing` company feature.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fr_super_pdp_submit_request = accounting_sh.FrSuperPdpSubmitRequest() # FrSuperPdpSubmitRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Submit an issued invoice
   accounting.fr_super_pdp_api.fr_super_pdp_submit(fr_super_pdp_submit_request)
except ApiException as e:
    print("Exception when calling FRSuperPDPApi->fr_super_pdp_submit: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fr_super_pdp_submit_request** | [**FrSuperPdpSubmitRequest**](FrSuperPdpSubmitRequest.md)|  | 

### Return type

void (empty response body)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**402** | Company feature einvoicing is required. |  -  |
**202** | One durable operation per issued source; repeated requests return the same operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fr_super_pdp_sync**
> fr_super_pdp_sync()

Queue SuperPDP synchronization

Queue synchronization; callers poll local operations instead of waiting for provider network calls. Requires the `edit.company` permission and the `einvoicing` company feature.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint


accounting = accounting_sh.Accounting("access_token")
try:
    # Queue SuperPDP synchronization
   accounting.fr_super_pdp_api.fr_super_pdp_sync()
except ApiException as e:
    print("Exception when calling FRSuperPDPApi->fr_super_pdp_sync: %s\n" % e)

```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**402** | Company feature einvoicing is required. |  -  |
**202** | Synchronization queued; retained work is also recovered by cron. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fr_super_pdp_verify**
> fr_super_pdp_verify()

Queue SuperPDP verification

Enqueue verification and resume invoice synchronization immediately once the grant becomes ready. Requires the `edit.company` permission and the `einvoicing` company feature.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint


accounting = accounting_sh.Accounting("access_token")
try:
    # Queue SuperPDP verification
   accounting.fr_super_pdp_api.fr_super_pdp_verify()
except ApiException as e:
    print("Exception when calling FRSuperPDPApi->fr_super_pdp_verify: %s\n" % e)

```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**402** | Company feature einvoicing is required. |  -  |
**202** | Verification and invoice synchronization queued. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

