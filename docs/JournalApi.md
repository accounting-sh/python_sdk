# accounting_sh.JournalApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**journal_balances**](JournalApi.md#journal_balances) | **GET** /journal/balances | Account balances
[**journal_balancesheet**](JournalApi.md#journal_balancesheet) | **GET** /journal/reports/balance-sheet | Balance sheet
[**journal_correction_add**](JournalApi.md#journal_correction_add) | **POST** /journal/corrections | Add correction
[**journal_correction_delete**](JournalApi.md#journal_correction_delete) | **DELETE** /journal/corrections/{uuid} | Reject changes to immutable correction
[**journal_correction_details**](JournalApi.md#journal_correction_details) | **GET** /journal/corrections/{uuid} | Details correction
[**journal_correction_list**](JournalApi.md#journal_correction_list) | **GET** /journal/corrections | List correction
[**journal_correction_update**](JournalApi.md#journal_correction_update) | **PUT** /journal/corrections/{uuid} | Reject changes to immutable correction
[**journal_entry_add**](JournalApi.md#journal_entry_add) | **POST** /journal/{journal_uuid}/entries | Add entry
[**journal_entry_delete**](JournalApi.md#journal_entry_delete) | **DELETE** /journal/{journal_uuid}/entries/{entry_uuid} | Delete entry
[**journal_entry_details**](JournalApi.md#journal_entry_details) | **GET** /journal/{journal_uuid}/entries/{entry_uuid} | Details entry
[**journal_entry_list**](JournalApi.md#journal_entry_list) | **GET** /journal/{journal_uuid}/entries | List entry
[**journal_entry_update**](JournalApi.md#journal_entry_update) | **PUT** /journal/{journal_uuid}/entries/{entry_uuid} | Update entry
[**journal_evidence_add**](JournalApi.md#journal_evidence_add) | **POST** /journal/{journal_uuid}/entries/{entry_uuid}/evidence | Add evidence
[**journal_evidence_delete**](JournalApi.md#journal_evidence_delete) | **DELETE** /journal/{journal_uuid}/entries/{entry_uuid}/evidence/{uuid} | Reject changes to immutable evidence
[**journal_evidence_details**](JournalApi.md#journal_evidence_details) | **GET** /journal/{journal_uuid}/entries/{entry_uuid}/evidence/{uuid} | Details evidence
[**journal_evidence_list**](JournalApi.md#journal_evidence_list) | **GET** /journal/{journal_uuid}/entries/{entry_uuid}/evidence | List evidence
[**journal_evidence_update**](JournalApi.md#journal_evidence_update) | **PUT** /journal/{journal_uuid}/entries/{entry_uuid}/evidence/{uuid} | Reject changes to immutable evidence
[**journal_export_add**](JournalApi.md#journal_export_add) | **POST** /journal/exports | Add export
[**journal_export_delete**](JournalApi.md#journal_export_delete) | **DELETE** /journal/exports/{uuid} | Reject changes to immutable export
[**journal_export_details**](JournalApi.md#journal_export_details) | **GET** /journal/exports/{uuid} | Details export
[**journal_export_list**](JournalApi.md#journal_export_list) | **GET** /journal/exports | List export
[**journal_export_update**](JournalApi.md#journal_export_update) | **PUT** /journal/exports/{uuid} | Reject changes to immutable export
[**journal_initialization_add**](JournalApi.md#journal_initialization_add) | **POST** /journal/initializations | Add initialization
[**journal_initialization_delete**](JournalApi.md#journal_initialization_delete) | **DELETE** /journal/initializations/{uuid} | Reject changes to immutable initialization
[**journal_initialization_details**](JournalApi.md#journal_initialization_details) | **GET** /journal/initializations/{uuid} | Details initialization
[**journal_initialization_list**](JournalApi.md#journal_initialization_list) | **GET** /journal/initializations | List initialization
[**journal_initialization_update**](JournalApi.md#journal_initialization_update) | **PUT** /journal/initializations/{uuid} | Reject changes to immutable initialization
[**journal_issue_add**](JournalApi.md#journal_issue_add) | **POST** /journal/issues | Reject changes to immutable issue
[**journal_issue_delete**](JournalApi.md#journal_issue_delete) | **DELETE** /journal/issues/{uuid} | Reject changes to immutable issue
[**journal_issue_details**](JournalApi.md#journal_issue_details) | **GET** /journal/issues/{uuid} | Details issue
[**journal_issue_list**](JournalApi.md#journal_issue_list) | **GET** /journal/issues | List issue
[**journal_issue_update**](JournalApi.md#journal_issue_update) | **PUT** /journal/issues/{uuid} | Reject changes to immutable issue
[**journal_journal_add**](JournalApi.md#journal_journal_add) | **POST** /journal | Add journal
[**journal_journal_delete**](JournalApi.md#journal_journal_delete) | **DELETE** /journal/{journal_uuid} | Delete journal
[**journal_journal_details**](JournalApi.md#journal_journal_details) | **GET** /journal/{journal_uuid} | Details journal
[**journal_journal_list**](JournalApi.md#journal_journal_list) | **GET** /journal | List journal
[**journal_journal_update**](JournalApi.md#journal_journal_update) | **PUT** /journal/{journal_uuid} | Update journal
[**journal_mapping_add**](JournalApi.md#journal_mapping_add) | **POST** /journal/mappings | Add mapping
[**journal_mapping_delete**](JournalApi.md#journal_mapping_delete) | **DELETE** /journal/mappings/{uuid} | Delete mapping
[**journal_mapping_details**](JournalApi.md#journal_mapping_details) | **GET** /journal/mappings/{uuid} | Details mapping
[**journal_mapping_list**](JournalApi.md#journal_mapping_list) | **GET** /journal/mappings | List mapping
[**journal_mapping_update**](JournalApi.md#journal_mapping_update) | **PUT** /journal/mappings/{uuid} | Update mapping
[**journal_movements**](JournalApi.md#journal_movements) | **GET** /journal/movements | Posted account movements
[**journal_period_add**](JournalApi.md#journal_period_add) | **POST** /journal/periods | Add period
[**journal_period_delete**](JournalApi.md#journal_period_delete) | **DELETE** /journal/periods/{uuid} | Delete period
[**journal_period_details**](JournalApi.md#journal_period_details) | **GET** /journal/periods/{uuid} | Details period
[**journal_period_list**](JournalApi.md#journal_period_list) | **GET** /journal/periods | List period
[**journal_period_update**](JournalApi.md#journal_period_update) | **PUT** /journal/periods/{uuid} | Update period
[**journal_profitandloss**](JournalApi.md#journal_profitandloss) | **GET** /journal/reports/profit-and-loss | Profit and loss
[**journal_trialbalance**](JournalApi.md#journal_trialbalance) | **GET** /journal/reports/trial-balance | Trial balance


# **journal_balances**
> journal_balances(var_from=var_from, to=to, code=code, contact=contact, journal=journal, period=period, bank_account=bank_account, group_by_contact=group_by_contact)

Account balances

Posted entries only; exact decimal strings use ISO minor-unit precision in the preserved company books currency (EUR 2, JPY 0, KWD 3). Requires `journal.report.view`. Reports do not certify country compliance or source completeness.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

var_from = '2013-10-20' # date |  (optional)
to = '2013-10-20' # date |  (optional)
code = 'code_example' # str |  (optional)
contact = 'contact_example' # str |  (optional)
journal = 'journal_example' # str |  (optional)
period = 'period_example' # str |  (optional)
bank_account = 'bank_account_example' # str |  (optional)
group_by_contact = True # bool |  (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # Account balances
    api_response = accounting.journal_api.journal_balances(var_from=var_from, to=to, code=code, contact=contact, journal=journal, period=period, bank_account=bank_account, group_by_contact=group_by_contact)
    print("The response of JournalApi->journal_balances:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_balances: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **date**|  | [optional] 
 **to** | **date**|  | [optional] 
 **code** | **str**|  | [optional] 
 **contact** | **str**|  | [optional] 
 **journal** | **str**|  | [optional] 
 **period** | **str**|  | [optional] 
 **bank_account** | **str**|  | [optional] 
 **group_by_contact** | **bool**|  | [optional] 

### Return type

**object**

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Posted accounting projection with success envelope |  -  |
**400** | Invalid filters |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journal_balancesheet**
> journal_balancesheet(var_from=var_from, to=to, code=code, contact=contact, journal=journal, period=period, bank_account=bank_account)

Balance sheet

Posted entries only; exact decimal strings use ISO minor-unit precision in the preserved company books currency (EUR 2, JPY 0, KWD 3). Requires `journal.report.view`. Reports do not certify country compliance or source completeness.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

var_from = '2013-10-20' # date |  (optional)
to = '2013-10-20' # date |  (optional)
code = 'code_example' # str |  (optional)
contact = 'contact_example' # str |  (optional)
journal = 'journal_example' # str |  (optional)
period = 'period_example' # str |  (optional)
bank_account = 'bank_account_example' # str |  (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # Balance sheet
    api_response = accounting.journal_api.journal_balancesheet(var_from=var_from, to=to, code=code, contact=contact, journal=journal, period=period, bank_account=bank_account)
    print("The response of JournalApi->journal_balancesheet:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_balancesheet: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **date**|  | [optional] 
 **to** | **date**|  | [optional] 
 **code** | **str**|  | [optional] 
 **contact** | **str**|  | [optional] 
 **journal** | **str**|  | [optional] 
 **period** | **str**|  | [optional] 
 **bank_account** | **str**|  | [optional] 

### Return type

**object**

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Posted accounting projection with success envelope |  -  |
**400** | Invalid filters |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journal_correction_add**
> journal_correction_add(journal_correction_add_request)

Add correction

All identifiers are scoped to the authenticated company. Only posted manual entries can be corrected here. The original, reversal and optional replacement remain linked. Generated corrections follow the source workflow. Requires `journal.correction.add`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

journal_correction_add_request = accounting_sh.JournalCorrectionAddRequest() # JournalCorrectionAddRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Add correction
    api_response = accounting.journal_api.journal_correction_add(journal_correction_add_request)
    print("The response of JournalApi->journal_correction_add:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_correction_add: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **journal_correction_add_request** | [**JournalCorrectionAddRequest**](JournalCorrectionAddRequest.md)|  | 

### Return type

[**JournalCorrectionAdd201Response**](JournalCorrectionAdd201Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Resource response with success envelope |  -  |
**400** | Invalid request fields |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Owned resource not found |  -  |
**409** | Accounting state conflict |  -  |
**422** | Accounting validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journal_correction_delete**
> journal_correction_delete(uuid)

Reject changes to immutable correction

All identifiers are scoped to the authenticated company. Only posted manual entries can be corrected here. The original, reversal and optional replacement remain linked. Generated corrections follow the source workflow. This write is unsupported and returns 405. Requires `journal.correction.view`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Reject changes to immutable correction
   accounting.journal_api.journal_correction_delete(uuid)
except ApiException as e:
    print("Exception when calling JournalApi->journal_correction_delete: %s\n" % e)

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
**405** | Unsupported operation |  -  |
**400** | Invalid request fields |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Owned resource not found |  -  |
**409** | Accounting state conflict |  -  |
**422** | Accounting validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journal_correction_details**
> journal_correction_details(uuid)

Details correction

All identifiers are scoped to the authenticated company. Only posted manual entries can be corrected here. The original, reversal and optional replacement remain linked. Generated corrections follow the source workflow. Requires `journal.correction.view`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Details correction
    api_response = accounting.journal_api.journal_correction_details(uuid)
    print("The response of JournalApi->journal_correction_details:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_correction_details: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**JournalCorrectionAdd201Response**](JournalCorrectionAdd201Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource response with success envelope |  -  |
**400** | Invalid request fields |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Owned resource not found |  -  |
**409** | Accounting state conflict |  -  |
**422** | Accounting validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journal_correction_list**
> journal_correction_list(page=page, per_page=per_page, original_entry=original_entry)

List correction

All identifiers are scoped to the authenticated company. Only posted manual entries can be corrected here. The original, reversal and optional replacement remain linked. Generated corrections follow the source workflow. Requires `journal.correction.list`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

page = 56 # int |  (optional)
per_page = 56 # int |  (optional)
original_entry = 'original_entry_example' # str |  (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List correction
    api_response = accounting.journal_api.journal_correction_list(page=page, per_page=per_page, original_entry=original_entry)
    print("The response of JournalApi->journal_correction_list:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_correction_list: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **original_entry** | **str**|  | [optional] 

### Return type

[**JournalCorrectionList200Response**](JournalCorrectionList200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource response with success envelope |  -  |
**400** | Invalid request fields |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Owned resource not found |  -  |
**409** | Accounting state conflict |  -  |
**422** | Accounting validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journal_correction_update**
> journal_correction_update(uuid)

Reject changes to immutable correction

All identifiers are scoped to the authenticated company. Only posted manual entries can be corrected here. The original, reversal and optional replacement remain linked. Generated corrections follow the source workflow. This write is unsupported and returns 405. Requires `journal.correction.view`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Reject changes to immutable correction
   accounting.journal_api.journal_correction_update(uuid)
except ApiException as e:
    print("Exception when calling JournalApi->journal_correction_update: %s\n" % e)

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
**405** | Unsupported operation |  -  |
**400** | Invalid request fields |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Owned resource not found |  -  |
**409** | Accounting state conflict |  -  |
**422** | Accounting validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journal_entry_add**
> journal_entry_add(journal_uuid, journal_entry_add_request)

Add entry

All identifiers are scoped to the authenticated company. Entries are scoped to their parent journal. Generated and posted financial content is immutable. Lines are saved atomically; amounts use exact decimal strings in major currency units. Posting requires `journal.entry.post` and an open period; opening entries additionally require `journal.entry.opening` and reviewed initialization. Requires `journal.entry.add`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

journal_uuid = 'journal_uuid_example' # str | 
journal_entry_add_request = accounting_sh.JournalEntryAddRequest() # JournalEntryAddRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Add entry
    api_response = accounting.journal_api.journal_entry_add(journal_uuid, journal_entry_add_request)
    print("The response of JournalApi->journal_entry_add:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_entry_add: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **journal_uuid** | **str**|  | 
 **journal_entry_add_request** | [**JournalEntryAddRequest**](JournalEntryAddRequest.md)|  | 

### Return type

[**JournalEntryAdd201Response**](JournalEntryAdd201Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Resource response with success envelope |  -  |
**400** | Invalid request fields |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Owned resource not found |  -  |
**409** | Accounting state conflict |  -  |
**422** | Accounting validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journal_entry_delete**
> journal_entry_delete(journal_uuid, entry_uuid)

Delete entry

All identifiers are scoped to the authenticated company. Entries are scoped to their parent journal. Generated and posted financial content is immutable. Lines are saved atomically; amounts use exact decimal strings in major currency units. Posting requires `journal.entry.post` and an open period; opening entries additionally require `journal.entry.opening` and reviewed initialization. Requires `journal.entry.delete`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

journal_uuid = 'journal_uuid_example' # str | 
entry_uuid = 'entry_uuid_example' # str | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete entry
    api_response = accounting.journal_api.journal_entry_delete(journal_uuid, entry_uuid)
    print("The response of JournalApi->journal_entry_delete:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_entry_delete: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **journal_uuid** | **str**|  | 
 **entry_uuid** | **str**|  | 

### Return type

[**JournalCorrectionDelete405Response**](JournalCorrectionDelete405Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource response with success envelope |  -  |
**400** | Invalid request fields |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Owned resource not found |  -  |
**409** | Accounting state conflict |  -  |
**422** | Accounting validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journal_entry_details**
> journal_entry_details(journal_uuid, entry_uuid)

Details entry

All identifiers are scoped to the authenticated company. Entries are scoped to their parent journal. Generated and posted financial content is immutable. Lines are saved atomically; amounts use exact decimal strings in major currency units. Posting requires `journal.entry.post` and an open period; opening entries additionally require `journal.entry.opening` and reviewed initialization. Requires `journal.entry.view`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

journal_uuid = 'journal_uuid_example' # str | 
entry_uuid = 'entry_uuid_example' # str | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Details entry
    api_response = accounting.journal_api.journal_entry_details(journal_uuid, entry_uuid)
    print("The response of JournalApi->journal_entry_details:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_entry_details: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **journal_uuid** | **str**|  | 
 **entry_uuid** | **str**|  | 

### Return type

[**JournalEntryAdd201Response**](JournalEntryAdd201Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource response with success envelope |  -  |
**400** | Invalid request fields |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Owned resource not found |  -  |
**409** | Accounting state conflict |  -  |
**422** | Accounting validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journal_entry_list**
> journal_entry_list(journal_uuid, page=page, per_page=per_page, status=status, origin=origin, period=period, accounting_date=accounting_date, var_from=var_from, to=to, source_type=source_type, source_uuid=source_uuid, code=code, contact=contact)

List entry

All identifiers are scoped to the authenticated company. Entries are scoped to their parent journal. Generated and posted financial content is immutable. Lines are saved atomically; amounts use exact decimal strings in major currency units. Posting requires `journal.entry.post` and an open period; opening entries additionally require `journal.entry.opening` and reviewed initialization. Requires `journal.entry.list`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

journal_uuid = 'journal_uuid_example' # str | 
page = 56 # int |  (optional)
per_page = 56 # int |  (optional)
status = 'status_example' # str |  (optional)
origin = 'origin_example' # str |  (optional)
period = 'period_example' # str |  (optional)
accounting_date = 'accounting_date_example' # str |  (optional)
var_from = 'var_from_example' # str |  (optional)
to = 'to_example' # str |  (optional)
source_type = 'source_type_example' # str |  (optional)
source_uuid = 'source_uuid_example' # str |  (optional)
code = 'code_example' # str |  (optional)
contact = 'contact_example' # str |  (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List entry
    api_response = accounting.journal_api.journal_entry_list(journal_uuid, page=page, per_page=per_page, status=status, origin=origin, period=period, accounting_date=accounting_date, var_from=var_from, to=to, source_type=source_type, source_uuid=source_uuid, code=code, contact=contact)
    print("The response of JournalApi->journal_entry_list:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_entry_list: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **journal_uuid** | **str**|  | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **status** | **str**|  | [optional] 
 **origin** | **str**|  | [optional] 
 **period** | **str**|  | [optional] 
 **accounting_date** | **str**|  | [optional] 
 **var_from** | **str**|  | [optional] 
 **to** | **str**|  | [optional] 
 **source_type** | **str**|  | [optional] 
 **source_uuid** | **str**|  | [optional] 
 **code** | **str**|  | [optional] 
 **contact** | **str**|  | [optional] 

### Return type

[**JournalEntryList200Response**](JournalEntryList200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource response with success envelope |  -  |
**400** | Invalid request fields |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Owned resource not found |  -  |
**409** | Accounting state conflict |  -  |
**422** | Accounting validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journal_entry_update**
> journal_entry_update(journal_uuid, entry_uuid, journal_entry_update_request)

Update entry

All identifiers are scoped to the authenticated company. Entries are scoped to their parent journal. Generated and posted financial content is immutable. Lines are saved atomically; amounts use exact decimal strings in major currency units. Posting requires `journal.entry.post` and an open period; opening entries additionally require `journal.entry.opening` and reviewed initialization. Requires `journal.entry.edit`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

journal_uuid = 'journal_uuid_example' # str | 
entry_uuid = 'entry_uuid_example' # str | 
journal_entry_update_request = accounting_sh.JournalEntryUpdateRequest() # JournalEntryUpdateRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Update entry
    api_response = accounting.journal_api.journal_entry_update(journal_uuid, entry_uuid, journal_entry_update_request)
    print("The response of JournalApi->journal_entry_update:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_entry_update: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **journal_uuid** | **str**|  | 
 **entry_uuid** | **str**|  | 
 **journal_entry_update_request** | [**JournalEntryUpdateRequest**](JournalEntryUpdateRequest.md)|  | 

### Return type

[**JournalEntryAdd201Response**](JournalEntryAdd201Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource response with success envelope |  -  |
**400** | Invalid request fields |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Owned resource not found |  -  |
**409** | Accounting state conflict |  -  |
**422** | Accounting validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journal_evidence_add**
> journal_evidence_add(journal_uuid, entry_uuid, journal_evidence_add_request)

Add evidence

All identifiers are scoped to the authenticated company. Evidence links are append-only; the document and entry must belong to the authenticated company. Requires `journal.evidence.add`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

journal_uuid = 'journal_uuid_example' # str | 
entry_uuid = 'entry_uuid_example' # str | 
journal_evidence_add_request = accounting_sh.JournalEvidenceAddRequest() # JournalEvidenceAddRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Add evidence
    api_response = accounting.journal_api.journal_evidence_add(journal_uuid, entry_uuid, journal_evidence_add_request)
    print("The response of JournalApi->journal_evidence_add:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_evidence_add: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **journal_uuid** | **str**|  | 
 **entry_uuid** | **str**|  | 
 **journal_evidence_add_request** | [**JournalEvidenceAddRequest**](JournalEvidenceAddRequest.md)|  | 

### Return type

[**JournalEvidenceAdd201Response**](JournalEvidenceAdd201Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Resource response with success envelope |  -  |
**400** | Invalid request fields |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Owned resource not found |  -  |
**409** | Accounting state conflict |  -  |
**422** | Accounting validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journal_evidence_delete**
> journal_evidence_delete(journal_uuid, entry_uuid, uuid)

Reject changes to immutable evidence

All identifiers are scoped to the authenticated company. Evidence links are append-only; the document and entry must belong to the authenticated company. This write is unsupported and returns 405. Requires `journal.evidence.view`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

journal_uuid = 'journal_uuid_example' # str | 
entry_uuid = 'entry_uuid_example' # str | 
uuid = 'uuid_example' # str | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Reject changes to immutable evidence
   accounting.journal_api.journal_evidence_delete(journal_uuid, entry_uuid, uuid)
except ApiException as e:
    print("Exception when calling JournalApi->journal_evidence_delete: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **journal_uuid** | **str**|  | 
 **entry_uuid** | **str**|  | 
 **uuid** | **str**|  | 

### Return type

void (empty response body)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**405** | Unsupported operation |  -  |
**400** | Invalid request fields |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Owned resource not found |  -  |
**409** | Accounting state conflict |  -  |
**422** | Accounting validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journal_evidence_details**
> journal_evidence_details(journal_uuid, entry_uuid, uuid)

Details evidence

All identifiers are scoped to the authenticated company. Evidence links are append-only; the document and entry must belong to the authenticated company. Requires `journal.evidence.view`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

journal_uuid = 'journal_uuid_example' # str | 
entry_uuid = 'entry_uuid_example' # str | 
uuid = 'uuid_example' # str | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Details evidence
    api_response = accounting.journal_api.journal_evidence_details(journal_uuid, entry_uuid, uuid)
    print("The response of JournalApi->journal_evidence_details:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_evidence_details: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **journal_uuid** | **str**|  | 
 **entry_uuid** | **str**|  | 
 **uuid** | **str**|  | 

### Return type

[**JournalEvidenceAdd201Response**](JournalEvidenceAdd201Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource response with success envelope |  -  |
**400** | Invalid request fields |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Owned resource not found |  -  |
**409** | Accounting state conflict |  -  |
**422** | Accounting validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journal_evidence_list**
> journal_evidence_list(journal_uuid, entry_uuid, page=page, per_page=per_page)

List evidence

All identifiers are scoped to the authenticated company. Evidence links are append-only; the document and entry must belong to the authenticated company. Requires `journal.evidence.list`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

journal_uuid = 'journal_uuid_example' # str | 
entry_uuid = 'entry_uuid_example' # str | 
page = 56 # int |  (optional)
per_page = 56 # int |  (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List evidence
    api_response = accounting.journal_api.journal_evidence_list(journal_uuid, entry_uuid, page=page, per_page=per_page)
    print("The response of JournalApi->journal_evidence_list:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_evidence_list: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **journal_uuid** | **str**|  | 
 **entry_uuid** | **str**|  | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**JournalEvidenceList200Response**](JournalEvidenceList200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource response with success envelope |  -  |
**400** | Invalid request fields |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Owned resource not found |  -  |
**409** | Accounting state conflict |  -  |
**422** | Accounting validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journal_evidence_update**
> journal_evidence_update(journal_uuid, entry_uuid, uuid)

Reject changes to immutable evidence

All identifiers are scoped to the authenticated company. Evidence links are append-only; the document and entry must belong to the authenticated company. This write is unsupported and returns 405. Requires `journal.evidence.view`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

journal_uuid = 'journal_uuid_example' # str | 
entry_uuid = 'entry_uuid_example' # str | 
uuid = 'uuid_example' # str | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Reject changes to immutable evidence
   accounting.journal_api.journal_evidence_update(journal_uuid, entry_uuid, uuid)
except ApiException as e:
    print("Exception when calling JournalApi->journal_evidence_update: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **journal_uuid** | **str**|  | 
 **entry_uuid** | **str**|  | 
 **uuid** | **str**|  | 

### Return type

void (empty response body)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**405** | Unsupported operation |  -  |
**400** | Invalid request fields |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Owned resource not found |  -  |
**409** | Accounting state conflict |  -  |
**422** | Accounting validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journal_export_add**
> journal_export_add(journal_export_add_request)

Add export

All identifiers are scoped to the authenticated company. Creation queues generation and returns status=pending. Poll the owned details resource until status=ready; its CSV is loaded from S3 as JSON data with a SHA-256 hash; this is not a statutory export. Requires `journal.export.add`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

journal_export_add_request = accounting_sh.JournalExportAddRequest() # JournalExportAddRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Add export
    api_response = accounting.journal_api.journal_export_add(journal_export_add_request)
    print("The response of JournalApi->journal_export_add:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_export_add: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **journal_export_add_request** | [**JournalExportAddRequest**](JournalExportAddRequest.md)|  | 

### Return type

[**JournalExportAdd201Response**](JournalExportAdd201Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Resource response with success envelope |  -  |
**400** | Invalid request fields |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Owned resource not found |  -  |
**409** | Accounting state conflict |  -  |
**422** | Accounting validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journal_export_delete**
> journal_export_delete(uuid)

Reject changes to immutable export

All identifiers are scoped to the authenticated company. Creation queues generation and returns status=pending. Poll the owned details resource until status=ready; its CSV is loaded from S3 as JSON data with a SHA-256 hash; this is not a statutory export. This write is unsupported and returns 405. Requires `journal.export.view`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Reject changes to immutable export
   accounting.journal_api.journal_export_delete(uuid)
except ApiException as e:
    print("Exception when calling JournalApi->journal_export_delete: %s\n" % e)

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
**405** | Unsupported operation |  -  |
**400** | Invalid request fields |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Owned resource not found |  -  |
**409** | Accounting state conflict |  -  |
**422** | Accounting validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journal_export_details**
> journal_export_details(uuid)

Details export

All identifiers are scoped to the authenticated company. Creation queues generation and returns status=pending. Poll the owned details resource until status=ready; its CSV is loaded from S3 as JSON data with a SHA-256 hash; this is not a statutory export. Requires `journal.export.view`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Details export
    api_response = accounting.journal_api.journal_export_details(uuid)
    print("The response of JournalApi->journal_export_details:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_export_details: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**JournalExportAdd201Response**](JournalExportAdd201Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource response with success envelope |  -  |
**400** | Invalid request fields |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Owned resource not found |  -  |
**409** | Accounting state conflict |  -  |
**422** | Accounting validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journal_export_list**
> journal_export_list(page=page, per_page=per_page)

List export

All identifiers are scoped to the authenticated company. Creation queues generation and returns status=pending. Poll the owned details resource until status=ready; its CSV is loaded from S3 as JSON data with a SHA-256 hash; this is not a statutory export. Requires `journal.export.list`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

page = 56 # int |  (optional)
per_page = 56 # int |  (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List export
    api_response = accounting.journal_api.journal_export_list(page=page, per_page=per_page)
    print("The response of JournalApi->journal_export_list:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_export_list: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**JournalExportList200Response**](JournalExportList200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource response with success envelope |  -  |
**400** | Invalid request fields |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Owned resource not found |  -  |
**409** | Accounting state conflict |  -  |
**422** | Accounting validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journal_export_update**
> journal_export_update(uuid)

Reject changes to immutable export

All identifiers are scoped to the authenticated company. Creation queues generation and returns status=pending. Poll the owned details resource until status=ready; its CSV is loaded from S3 as JSON data with a SHA-256 hash; this is not a statutory export. This write is unsupported and returns 405. Requires `journal.export.view`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Reject changes to immutable export
   accounting.journal_api.journal_export_update(uuid)
except ApiException as e:
    print("Exception when calling JournalApi->journal_export_update: %s\n" % e)

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
**405** | Unsupported operation |  -  |
**400** | Invalid request fields |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Owned resource not found |  -  |
**409** | Accounting state conflict |  -  |
**422** | Accounting validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journal_initialization_add**
> journal_initialization_add(journal_initialization_add_request)

Add initialization

Creation schedules historical processing. Explicit zero opening with automatic_setup also prepares journals and mappings and requires `journal.add`, `journal.mapping.add` and `accounting_code.add`. replace_unposted additionally requires `journal.mapping.edit` and refuses any financial history. Requires `journal.initialization.add`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

journal_initialization_add_request = accounting_sh.JournalInitializationAddRequest() # JournalInitializationAddRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Add initialization
    api_response = accounting.journal_api.journal_initialization_add(journal_initialization_add_request)
    print("The response of JournalApi->journal_initialization_add:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_initialization_add: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **journal_initialization_add_request** | [**JournalInitializationAddRequest**](JournalInitializationAddRequest.md)|  | 

### Return type

[**JournalInitializationAdd202Response**](JournalInitializationAdd202Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Resource response with success envelope |  -  |
**400** | Invalid request fields |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Owned resource not found |  -  |
**409** | Accounting state conflict |  -  |
**422** | Accounting validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journal_initialization_delete**
> journal_initialization_delete(uuid)

Reject changes to immutable initialization

All identifiers are scoped to the authenticated company. Creation schedules historical processing; status remains system-managed. This write is unsupported and returns 405. Requires `journal.initialization.view`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Reject changes to immutable initialization
   accounting.journal_api.journal_initialization_delete(uuid)
except ApiException as e:
    print("Exception when calling JournalApi->journal_initialization_delete: %s\n" % e)

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
**405** | Unsupported operation |  -  |
**400** | Invalid request fields |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Owned resource not found |  -  |
**409** | Accounting state conflict |  -  |
**422** | Accounting validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journal_initialization_details**
> journal_initialization_details(uuid)

Details initialization

All identifiers are scoped to the authenticated company. Creation schedules historical processing; status remains system-managed. Requires `journal.initialization.view`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Details initialization
    api_response = accounting.journal_api.journal_initialization_details(uuid)
    print("The response of JournalApi->journal_initialization_details:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_initialization_details: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**JournalInitializationAdd202Response**](JournalInitializationAdd202Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource response with success envelope |  -  |
**400** | Invalid request fields |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Owned resource not found |  -  |
**409** | Accounting state conflict |  -  |
**422** | Accounting validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journal_initialization_list**
> journal_initialization_list(page=page, per_page=per_page, status=status)

List initialization

All identifiers are scoped to the authenticated company. Creation schedules historical processing; status remains system-managed. Requires `journal.initialization.list`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

page = 56 # int |  (optional)
per_page = 56 # int |  (optional)
status = 'status_example' # str |  (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List initialization
    api_response = accounting.journal_api.journal_initialization_list(page=page, per_page=per_page, status=status)
    print("The response of JournalApi->journal_initialization_list:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_initialization_list: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **status** | **str**|  | [optional] 

### Return type

[**JournalInitializationList200Response**](JournalInitializationList200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource response with success envelope |  -  |
**400** | Invalid request fields |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Owned resource not found |  -  |
**409** | Accounting state conflict |  -  |
**422** | Accounting validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journal_initialization_update**
> journal_initialization_update(uuid)

Reject changes to immutable initialization

All identifiers are scoped to the authenticated company. Creation schedules historical processing; status remains system-managed. This write is unsupported and returns 405. Requires `journal.initialization.view`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Reject changes to immutable initialization
   accounting.journal_api.journal_initialization_update(uuid)
except ApiException as e:
    print("Exception when calling JournalApi->journal_initialization_update: %s\n" % e)

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
**405** | Unsupported operation |  -  |
**400** | Invalid request fields |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Owned resource not found |  -  |
**409** | Accounting state conflict |  -  |
**422** | Accounting validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journal_issue_add**
> journal_issue_add()

Reject changes to immutable issue

All identifiers are scoped to the authenticated company. This write is unsupported and returns 405. Requires `journal.issue.view`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint


accounting = accounting_sh.Accounting("access_token")
try:
    # Reject changes to immutable issue
   accounting.journal_api.journal_issue_add()
except ApiException as e:
    print("Exception when calling JournalApi->journal_issue_add: %s\n" % e)

```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**405** | Unsupported operation |  -  |
**400** | Invalid request fields |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Owned resource not found |  -  |
**409** | Accounting state conflict |  -  |
**422** | Accounting validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journal_issue_delete**
> journal_issue_delete(uuid)

Reject changes to immutable issue

All identifiers are scoped to the authenticated company. This write is unsupported and returns 405. Requires `journal.issue.view`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Reject changes to immutable issue
   accounting.journal_api.journal_issue_delete(uuid)
except ApiException as e:
    print("Exception when calling JournalApi->journal_issue_delete: %s\n" % e)

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
**405** | Unsupported operation |  -  |
**400** | Invalid request fields |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Owned resource not found |  -  |
**409** | Accounting state conflict |  -  |
**422** | Accounting validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journal_issue_details**
> journal_issue_details(uuid)

Details issue

All identifiers are scoped to the authenticated company. Requires `journal.issue.view`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Details issue
    api_response = accounting.journal_api.journal_issue_details(uuid)
    print("The response of JournalApi->journal_issue_details:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_issue_details: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**JournalIssueAdd405Response**](JournalIssueAdd405Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource response with success envelope |  -  |
**400** | Invalid request fields |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Owned resource not found |  -  |
**409** | Accounting state conflict |  -  |
**422** | Accounting validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journal_issue_list**
> journal_issue_list(page=page, per_page=per_page, status=status, source_type=source_type, source_uuid=source_uuid, event=event)

List issue

All identifiers are scoped to the authenticated company. Requires `journal.issue.list`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

page = 56 # int |  (optional)
per_page = 56 # int |  (optional)
status = 'status_example' # str |  (optional)
source_type = 'source_type_example' # str |  (optional)
source_uuid = 'source_uuid_example' # str |  (optional)
event = 'event_example' # str |  (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List issue
    api_response = accounting.journal_api.journal_issue_list(page=page, per_page=per_page, status=status, source_type=source_type, source_uuid=source_uuid, event=event)
    print("The response of JournalApi->journal_issue_list:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_issue_list: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **status** | **str**|  | [optional] 
 **source_type** | **str**|  | [optional] 
 **source_uuid** | **str**|  | [optional] 
 **event** | **str**|  | [optional] 

### Return type

[**JournalIssueList200Response**](JournalIssueList200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource response with success envelope |  -  |
**400** | Invalid request fields |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Owned resource not found |  -  |
**409** | Accounting state conflict |  -  |
**422** | Accounting validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journal_issue_update**
> journal_issue_update(uuid)

Reject changes to immutable issue

All identifiers are scoped to the authenticated company. This write is unsupported and returns 405. Requires `journal.issue.view`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Reject changes to immutable issue
   accounting.journal_api.journal_issue_update(uuid)
except ApiException as e:
    print("Exception when calling JournalApi->journal_issue_update: %s\n" % e)

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
**405** | Unsupported operation |  -  |
**400** | Invalid request fields |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Owned resource not found |  -  |
**409** | Accounting state conflict |  -  |
**422** | Accounting validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journal_journal_add**
> journal_journal_add(journal_journal_add_request)

Add journal

All identifiers are scoped to the authenticated company. Requires `journal.add`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

journal_journal_add_request = accounting_sh.JournalJournalAddRequest() # JournalJournalAddRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Add journal
    api_response = accounting.journal_api.journal_journal_add(journal_journal_add_request)
    print("The response of JournalApi->journal_journal_add:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_journal_add: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **journal_journal_add_request** | [**JournalJournalAddRequest**](JournalJournalAddRequest.md)|  | 

### Return type

[**JournalJournalAdd201Response**](JournalJournalAdd201Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Resource response with success envelope |  -  |
**400** | Invalid request fields |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Owned resource not found |  -  |
**409** | Accounting state conflict |  -  |
**422** | Accounting validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journal_journal_delete**
> journal_journal_delete(journal_uuid)

Delete journal

All identifiers are scoped to the authenticated company. Requires `journal.delete`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

journal_uuid = 'journal_uuid_example' # str | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete journal
    api_response = accounting.journal_api.journal_journal_delete(journal_uuid)
    print("The response of JournalApi->journal_journal_delete:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_journal_delete: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **journal_uuid** | **str**|  | 

### Return type

[**JournalCorrectionDelete405Response**](JournalCorrectionDelete405Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource response with success envelope |  -  |
**400** | Invalid request fields |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Owned resource not found |  -  |
**409** | Accounting state conflict |  -  |
**422** | Accounting validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journal_journal_details**
> journal_journal_details(journal_uuid)

Details journal

All identifiers are scoped to the authenticated company. Requires `journal.view`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

journal_uuid = 'journal_uuid_example' # str | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Details journal
    api_response = accounting.journal_api.journal_journal_details(journal_uuid)
    print("The response of JournalApi->journal_journal_details:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_journal_details: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **journal_uuid** | **str**|  | 

### Return type

[**JournalJournalAdd201Response**](JournalJournalAdd201Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource response with success envelope |  -  |
**400** | Invalid request fields |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Owned resource not found |  -  |
**409** | Accounting state conflict |  -  |
**422** | Accounting validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journal_journal_list**
> journal_journal_list(page=page, per_page=per_page, status=status, type=type)

List journal

All identifiers are scoped to the authenticated company. Requires `journal.list`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

page = 56 # int |  (optional)
per_page = 56 # int |  (optional)
status = 'status_example' # str |  (optional)
type = 'type_example' # str |  (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List journal
    api_response = accounting.journal_api.journal_journal_list(page=page, per_page=per_page, status=status, type=type)
    print("The response of JournalApi->journal_journal_list:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_journal_list: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **status** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 

### Return type

[**JournalJournalList200Response**](JournalJournalList200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource response with success envelope |  -  |
**400** | Invalid request fields |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Owned resource not found |  -  |
**409** | Accounting state conflict |  -  |
**422** | Accounting validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journal_journal_update**
> journal_journal_update(journal_uuid, journal_journal_update_request)

Update journal

All identifiers are scoped to the authenticated company. Requires `journal.edit`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

journal_uuid = 'journal_uuid_example' # str | 
journal_journal_update_request = accounting_sh.JournalJournalUpdateRequest() # JournalJournalUpdateRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Update journal
    api_response = accounting.journal_api.journal_journal_update(journal_uuid, journal_journal_update_request)
    print("The response of JournalApi->journal_journal_update:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_journal_update: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **journal_uuid** | **str**|  | 
 **journal_journal_update_request** | [**JournalJournalUpdateRequest**](JournalJournalUpdateRequest.md)|  | 

### Return type

[**JournalJournalAdd201Response**](JournalJournalAdd201Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource response with success envelope |  -  |
**400** | Invalid request fields |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Owned resource not found |  -  |
**409** | Accounting state conflict |  -  |
**422** | Accounting validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journal_mapping_add**
> journal_mapping_add(journal_mapping_add_request)

Add mapping

All identifiers are scoped to the authenticated company. The code field identifies an existing accounting code UUID. No accounting codes are created by this endpoint. Requires `journal.mapping.add`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

journal_mapping_add_request = accounting_sh.JournalMappingAddRequest() # JournalMappingAddRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Add mapping
    api_response = accounting.journal_api.journal_mapping_add(journal_mapping_add_request)
    print("The response of JournalApi->journal_mapping_add:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_mapping_add: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **journal_mapping_add_request** | [**JournalMappingAddRequest**](JournalMappingAddRequest.md)|  | 

### Return type

[**JournalMappingAdd201Response**](JournalMappingAdd201Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Resource response with success envelope |  -  |
**400** | Invalid request fields |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Owned resource not found |  -  |
**409** | Accounting state conflict |  -  |
**422** | Accounting validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journal_mapping_delete**
> journal_mapping_delete(uuid)

Delete mapping

All identifiers are scoped to the authenticated company. The code field identifies an existing accounting code UUID. No accounting codes are created by this endpoint. Requires `journal.mapping.delete`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete mapping
    api_response = accounting.journal_api.journal_mapping_delete(uuid)
    print("The response of JournalApi->journal_mapping_delete:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_mapping_delete: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**JournalCorrectionDelete405Response**](JournalCorrectionDelete405Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource response with success envelope |  -  |
**400** | Invalid request fields |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Owned resource not found |  -  |
**409** | Accounting state conflict |  -  |
**422** | Accounting validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journal_mapping_details**
> journal_mapping_details(uuid)

Details mapping

All identifiers are scoped to the authenticated company. The code field identifies an existing accounting code UUID. No accounting codes are created by this endpoint. Requires `journal.mapping.view`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Details mapping
    api_response = accounting.journal_api.journal_mapping_details(uuid)
    print("The response of JournalApi->journal_mapping_details:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_mapping_details: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**JournalMappingAdd201Response**](JournalMappingAdd201Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource response with success envelope |  -  |
**400** | Invalid request fields |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Owned resource not found |  -  |
**409** | Accounting state conflict |  -  |
**422** | Accounting validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journal_mapping_list**
> journal_mapping_list(page=page, per_page=per_page, role=role, scope=scope, status=status)

List mapping

All identifiers are scoped to the authenticated company. The code field identifies an existing accounting code UUID. No accounting codes are created by this endpoint. Requires `journal.mapping.list`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

page = 56 # int |  (optional)
per_page = 56 # int |  (optional)
role = 'role_example' # str |  (optional)
scope = 'scope_example' # str |  (optional)
status = 'status_example' # str |  (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List mapping
    api_response = accounting.journal_api.journal_mapping_list(page=page, per_page=per_page, role=role, scope=scope, status=status)
    print("The response of JournalApi->journal_mapping_list:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_mapping_list: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **role** | **str**|  | [optional] 
 **scope** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 

### Return type

[**JournalMappingList200Response**](JournalMappingList200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource response with success envelope |  -  |
**400** | Invalid request fields |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Owned resource not found |  -  |
**409** | Accounting state conflict |  -  |
**422** | Accounting validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journal_mapping_update**
> journal_mapping_update(uuid, journal_mapping_update_request)

Update mapping

All identifiers are scoped to the authenticated company. The code field identifies an existing accounting code UUID. No accounting codes are created by this endpoint. Requires `journal.mapping.edit`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | 
journal_mapping_update_request = accounting_sh.JournalMappingUpdateRequest() # JournalMappingUpdateRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Update mapping
    api_response = accounting.journal_api.journal_mapping_update(uuid, journal_mapping_update_request)
    print("The response of JournalApi->journal_mapping_update:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_mapping_update: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **journal_mapping_update_request** | [**JournalMappingUpdateRequest**](JournalMappingUpdateRequest.md)|  | 

### Return type

[**JournalMappingAdd201Response**](JournalMappingAdd201Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource response with success envelope |  -  |
**400** | Invalid request fields |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Owned resource not found |  -  |
**409** | Accounting state conflict |  -  |
**422** | Accounting validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journal_movements**
> journal_movements(code, var_from=var_from, to=to, contact=contact, journal=journal, period=period, bank_account=bank_account, page=page, per_page=per_page)

Posted account movements

Posted entries only; exact decimal strings use ISO minor-unit precision in the preserved company books currency (EUR 2, JPY 0, KWD 3). Requires `journal.report.view`. Reports do not certify country compliance or source completeness.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

code = 'code_example' # str | 
var_from = '2013-10-20' # date |  (optional)
to = '2013-10-20' # date |  (optional)
contact = 'contact_example' # str |  (optional)
journal = 'journal_example' # str |  (optional)
period = 'period_example' # str |  (optional)
bank_account = 'bank_account_example' # str |  (optional)
page = 56 # int |  (optional)
per_page = 56 # int |  (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # Posted account movements
    api_response = accounting.journal_api.journal_movements(code, var_from=var_from, to=to, contact=contact, journal=journal, period=period, bank_account=bank_account, page=page, per_page=per_page)
    print("The response of JournalApi->journal_movements:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_movements: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 
 **var_from** | **date**|  | [optional] 
 **to** | **date**|  | [optional] 
 **contact** | **str**|  | [optional] 
 **journal** | **str**|  | [optional] 
 **period** | **str**|  | [optional] 
 **bank_account** | **str**|  | [optional] 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

**object**

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Posted accounting projection with success envelope |  -  |
**400** | Invalid filters |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journal_period_add**
> journal_period_add(journal_period_add_request)

Add period

All identifiers are scoped to the authenticated company. Requires `journal.period.add`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

journal_period_add_request = accounting_sh.JournalPeriodAddRequest() # JournalPeriodAddRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Add period
    api_response = accounting.journal_api.journal_period_add(journal_period_add_request)
    print("The response of JournalApi->journal_period_add:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_period_add: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **journal_period_add_request** | [**JournalPeriodAddRequest**](JournalPeriodAddRequest.md)|  | 

### Return type

[**JournalPeriodAdd201Response**](JournalPeriodAdd201Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Resource response with success envelope |  -  |
**400** | Invalid request fields |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Owned resource not found |  -  |
**409** | Accounting state conflict |  -  |
**422** | Accounting validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journal_period_delete**
> journal_period_delete(uuid)

Delete period

All identifiers are scoped to the authenticated company. Requires `journal.period.delete`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete period
    api_response = accounting.journal_api.journal_period_delete(uuid)
    print("The response of JournalApi->journal_period_delete:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_period_delete: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**JournalCorrectionDelete405Response**](JournalCorrectionDelete405Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource response with success envelope |  -  |
**400** | Invalid request fields |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Owned resource not found |  -  |
**409** | Accounting state conflict |  -  |
**422** | Accounting validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journal_period_details**
> journal_period_details(uuid)

Details period

All identifiers are scoped to the authenticated company. Requires `journal.period.view`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Details period
    api_response = accounting.journal_api.journal_period_details(uuid)
    print("The response of JournalApi->journal_period_details:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_period_details: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**JournalPeriodAdd201Response**](JournalPeriodAdd201Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource response with success envelope |  -  |
**400** | Invalid request fields |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Owned resource not found |  -  |
**409** | Accounting state conflict |  -  |
**422** | Accounting validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journal_period_list**
> journal_period_list(page=page, per_page=per_page, status=status)

List period

All identifiers are scoped to the authenticated company. Requires `journal.period.list`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

page = 56 # int |  (optional)
per_page = 56 # int |  (optional)
status = 'status_example' # str |  (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List period
    api_response = accounting.journal_api.journal_period_list(page=page, per_page=per_page, status=status)
    print("The response of JournalApi->journal_period_list:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_period_list: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **status** | **str**|  | [optional] 

### Return type

[**JournalPeriodList200Response**](JournalPeriodList200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource response with success envelope |  -  |
**400** | Invalid request fields |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Owned resource not found |  -  |
**409** | Accounting state conflict |  -  |
**422** | Accounting validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journal_period_update**
> journal_period_update(uuid, journal_period_update_request)

Update period

All identifiers are scoped to the authenticated company. Requires `journal.period.edit`.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | 
journal_period_update_request = accounting_sh.JournalPeriodUpdateRequest() # JournalPeriodUpdateRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Update period
    api_response = accounting.journal_api.journal_period_update(uuid, journal_period_update_request)
    print("The response of JournalApi->journal_period_update:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_period_update: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **journal_period_update_request** | [**JournalPeriodUpdateRequest**](JournalPeriodUpdateRequest.md)|  | 

### Return type

[**JournalPeriodAdd201Response**](JournalPeriodAdd201Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource response with success envelope |  -  |
**400** | Invalid request fields |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |
**404** | Owned resource not found |  -  |
**409** | Accounting state conflict |  -  |
**422** | Accounting validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journal_profitandloss**
> journal_profitandloss(var_from=var_from, to=to, code=code, contact=contact, journal=journal, period=period, bank_account=bank_account)

Profit and loss

Posted entries only; exact decimal strings use ISO minor-unit precision in the preserved company books currency (EUR 2, JPY 0, KWD 3). Requires `journal.report.view`. Reports do not certify country compliance or source completeness.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

var_from = '2013-10-20' # date |  (optional)
to = '2013-10-20' # date |  (optional)
code = 'code_example' # str |  (optional)
contact = 'contact_example' # str |  (optional)
journal = 'journal_example' # str |  (optional)
period = 'period_example' # str |  (optional)
bank_account = 'bank_account_example' # str |  (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # Profit and loss
    api_response = accounting.journal_api.journal_profitandloss(var_from=var_from, to=to, code=code, contact=contact, journal=journal, period=period, bank_account=bank_account)
    print("The response of JournalApi->journal_profitandloss:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_profitandloss: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **date**|  | [optional] 
 **to** | **date**|  | [optional] 
 **code** | **str**|  | [optional] 
 **contact** | **str**|  | [optional] 
 **journal** | **str**|  | [optional] 
 **period** | **str**|  | [optional] 
 **bank_account** | **str**|  | [optional] 

### Return type

**object**

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Posted accounting projection with success envelope |  -  |
**400** | Invalid filters |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journal_trialbalance**
> journal_trialbalance(var_from=var_from, to=to, code=code, contact=contact, journal=journal, period=period, bank_account=bank_account)

Trial balance

Posted entries only; exact decimal strings use ISO minor-unit precision in the preserved company books currency (EUR 2, JPY 0, KWD 3). Requires `journal.report.view`. Reports do not certify country compliance or source completeness.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

var_from = '2013-10-20' # date |  (optional)
to = '2013-10-20' # date |  (optional)
code = 'code_example' # str |  (optional)
contact = 'contact_example' # str |  (optional)
journal = 'journal_example' # str |  (optional)
period = 'period_example' # str |  (optional)
bank_account = 'bank_account_example' # str |  (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # Trial balance
    api_response = accounting.journal_api.journal_trialbalance(var_from=var_from, to=to, code=code, contact=contact, journal=journal, period=period, bank_account=bank_account)
    print("The response of JournalApi->journal_trialbalance:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_trialbalance: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **date**|  | [optional] 
 **to** | **date**|  | [optional] 
 **code** | **str**|  | [optional] 
 **contact** | **str**|  | [optional] 
 **journal** | **str**|  | [optional] 
 **period** | **str**|  | [optional] 
 **bank_account** | **str**|  | [optional] 

### Return type

**object**

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Posted accounting projection with success envelope |  -  |
**400** | Invalid filters |  -  |
**401** | Authentication required |  -  |
**403** | Permission denied |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

