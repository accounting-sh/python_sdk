# accounting_sh.ExpenseReportsApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_expense_report**](ExpenseReportsApi.md#add_expense_report) | **POST** /expenses/expense-reports | Add an expense report
[**delete_expense_report**](ExpenseReportsApi.md#delete_expense_report) | **DELETE** /expenses/expense-reports/{uuid} | Delete an expense report
[**expense_report_o_auth_login**](ExpenseReportsApi.md#expense_report_o_auth_login) | **GET** /expenses/expense-reports/login/{method} | OAuth Login
[**get_expense_report**](ExpenseReportsApi.md#get_expense_report) | **GET** /expenses/expense-reports/{uuid} | Get an expense report
[**get_expense_report_account**](ExpenseReportsApi.md#get_expense_report_account) | **GET** /expenses/expense-reports/me | Get the currently connected expense report user details
[**get_expense_report_user**](ExpenseReportsApi.md#get_expense_report_user) | **GET** /expenses/expense-reports/users/{uuid} | Get an user details
[**list_expense_reports**](ExpenseReportsApi.md#list_expense_reports) | **GET** /expenses/expense-reports | List company&#39;s expense reports.
[**send_expense_report_login_email**](ExpenseReportsApi.md#send_expense_report_login_email) | **POST** /expenses/expense-reports/login | Request login email
[**update_expense_report**](ExpenseReportsApi.md#update_expense_report) | **PUT** /expenses/expense-reports/{uuid} | Update an expense report
[**update_expense_report_account**](ExpenseReportsApi.md#update_expense_report_account) | **PUT** /expenses/expense-reports/me | Update the currently connected expense report user
[**update_expense_report_settings**](ExpenseReportsApi.md#update_expense_report_settings) | **POST** /expenses/expense-reports/settings | Retrieve company settings for expense reports
[**verify_expense_report_settings**](ExpenseReportsApi.md#verify_expense_report_settings) | **POST** /expenses/expense-reports/verify | Verify expense reports settings


# **add_expense_report**
> add_expense_report(add_expense_report_request)

Add an expense report

Add an expense report. Send the resource fields in the request body; the response contains the saved record. Requires at least one permission: `expense_report.add`. Requires company feature(s): `expense_report`. Returns 402 if unavailable.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_expense_report_request = accounting_sh.AddExpenseReportRequest() # AddExpenseReportRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Add an expense report
    api_response = accounting.expense_reports_api.add_expense_report(add_expense_report_request)
    print("The response of ExpenseReportsApi->add_expense_report:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpenseReportsApi->add_expense_report: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_expense_report_request** | [**AddExpenseReportRequest**](AddExpenseReportRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**AddExpenseReport200Response**](AddExpenseReport200Response.md)

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

# **delete_expense_report**
> delete_expense_report(uuid)

Delete an expense report

Delete an expense report. This action deletes the selected record. Review references to it before deletion. Requires at least one permission: `expense_report.delete`. Requires company feature(s): `expense_report`. Returns 402 if unavailable.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The expense report uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete an expense report
    api_response = accounting.expense_reports_api.delete_expense_report(uuid)
    print("The response of ExpenseReportsApi->delete_expense_report:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpenseReportsApi->delete_expense_report: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The expense report uuid | 

### Return type

[**ImportAccountTransactions202Response**](ImportAccountTransactions202Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**409** | Accounting evidence is retained or held; the requested mutation is blocked. |  -  |
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |
**402** | The company does not have the required feature. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **expense_report_o_auth_login**
> expense_report_o_auth_login(method)

OAuth Login

OAuth Login. Use the parameters and response fields below for this operation.

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

method = 'method_example' # str | The OAuth Provider to use

accounting = accounting_sh.Accounting("access_token")
try:
    # OAuth Login
    api_response = accounting.expense_reports_api.expense_report_o_auth_login(method)
    print("The response of ExpenseReportsApi->expense_report_o_auth_login:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpenseReportsApi->expense_report_o_auth_login: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **method** | **str**| The OAuth Provider to use | 

### Return type

[**ExpenseReportOAuthLogin200Response**](ExpenseReportOAuthLogin200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**400** | The request failed validation or could not be processed. Inspect errors, correct the input, and try again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_expense_report**
> get_expense_report(uuid)

Get an expense report

Get an expense report. Use the identifier returned by the corresponding list or create operation. Requires at least one permission: `expense_report.view`. Requires company feature(s): `expense_report`. Returns 402 if unavailable.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The expense report uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get an expense report
    api_response = accounting.expense_reports_api.get_expense_report(uuid)
    print("The response of ExpenseReportsApi->get_expense_report:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpenseReportsApi->get_expense_report: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The expense report uuid | 

### Return type

[**AddExpenseReport200Response**](AddExpenseReport200Response.md)

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

# **get_expense_report_account**
> get_expense_report_account()

Get the currently connected expense report user details

Get the currently connected expense report user details. Use the parameters and response fields below for this operation. Requires at least one permission: `expense_report.view.account`. Requires company feature(s): `expense_report`. Returns 402 if unavailable.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint


accounting = accounting_sh.Accounting("access_token")
try:
    # Get the currently connected expense report user details
    api_response = accounting.expense_reports_api.get_expense_report_account()
    print("The response of ExpenseReportsApi->get_expense_report_account:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpenseReportsApi->get_expense_report_account: %s\n" % e)

```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetExpenseReportAccount200Response**](GetExpenseReportAccount200Response.md)

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

# **get_expense_report_user**
> get_expense_report_user(uuid)

Get an user details

Get an user details. Use the parameters and response fields below for this operation. Requires at least one permission: `expense_report.view.user`. Requires company feature(s): `expense_report`. Returns 402 if unavailable.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The expense report user uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get an user details
    api_response = accounting.expense_reports_api.get_expense_report_user(uuid)
    print("The response of ExpenseReportsApi->get_expense_report_user:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpenseReportsApi->get_expense_report_user: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The expense report user uuid | 

### Return type

[**GetExpenseReportAccount200Response**](GetExpenseReportAccount200Response.md)

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

# **list_expense_reports**
> list_expense_reports(fields=fields, page=page, per_page=per_page, order_by=order_by)

List company's expense reports.

List company's expense reports. Retrieve records using the query parameters below. Requires at least one permission: `expense_report.list`. Requires company feature(s): `expense_report`. Returns 402 if unavailable.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = 'uuid,user,status' # str | Comma-separated fields to include in each record. Default fields: uuid, user, status. (optional)
page = 1 # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10 # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = 'created_at:desc' # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's expense reports.
    api_response = accounting.expense_reports_api.list_expense_reports(fields=fields, page=page, per_page=per_page, order_by=order_by)
    print("The response of ExpenseReportsApi->list_expense_reports:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpenseReportsApi->list_expense_reports: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Comma-separated fields to include in each record. Default fields: uuid, user, status. | [optional] 
 **page** | **int**| Page number, starting at 1. Values below 1 are treated as 1. | [optional] [default to 1]
 **per_page** | **int**| Records per page. The server caps page size to 100. Values below 1 use that maximum. | [optional] [default to 10]
 **order_by** | **str**| Sort by a supported field and direction, using field:asc or field:desc. | [optional] 

### Return type

[**ListExpenseReports200Response**](ListExpenseReports200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**402** | The company does not have the required feature. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_expense_report_login_email**
> send_expense_report_login_email(send_expense_report_login_email_request)

Request login email

Request a sign-in email for an expense report user. This action sends an email; avoid automatic retries.

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

send_expense_report_login_email_request = accounting_sh.SendExpenseReportLoginEmailRequest() # SendExpenseReportLoginEmailRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Request login email
    api_response = accounting.expense_reports_api.send_expense_report_login_email(send_expense_report_login_email_request)
    print("The response of ExpenseReportsApi->send_expense_report_login_email:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpenseReportsApi->send_expense_report_login_email: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_expense_report_login_email_request** | [**SendExpenseReportLoginEmailRequest**](SendExpenseReportLoginEmailRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**ImportAccountTransactions202Response**](ImportAccountTransactions202Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**400** | The request failed validation or could not be processed. Inspect errors, correct the input, and try again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_expense_report**
> update_expense_report(uuid, add_expense_report_request)

Update an expense report

Update an expense report. Send the fields accepted by this operation in the request body. Requires at least one permission: `expense_report.edit`. Requires company feature(s): `expense_report`. Returns 402 if unavailable.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The expense report uuid
add_expense_report_request = accounting_sh.AddExpenseReportRequest() # AddExpenseReportRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update an expense report
    api_response = accounting.expense_reports_api.update_expense_report(uuid, add_expense_report_request)
    print("The response of ExpenseReportsApi->update_expense_report:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpenseReportsApi->update_expense_report: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The expense report uuid | 
 **add_expense_report_request** | [**AddExpenseReportRequest**](AddExpenseReportRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**AddExpenseReport200Response**](AddExpenseReport200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**409** | Accounting evidence is retained or held; the requested mutation is blocked. |  -  |
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**400** | The request failed validation or could not be processed. Inspect errors, correct the input, and try again. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |
**402** | The company does not have the required feature. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_expense_report_account**
> update_expense_report_account(update_expense_report_account_request)

Update the currently connected expense report user

Update the currently connected expense report user. Send the fields accepted by this operation in the request body. Requires at least one permission: `expense_report.edit.account`. Requires company feature(s): `expense_report`. Returns 402 if unavailable.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

update_expense_report_account_request = accounting_sh.UpdateExpenseReportAccountRequest() # UpdateExpenseReportAccountRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update the currently connected expense report user
    api_response = accounting.expense_reports_api.update_expense_report_account(update_expense_report_account_request)
    print("The response of ExpenseReportsApi->update_expense_report_account:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpenseReportsApi->update_expense_report_account: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_expense_report_account_request** | [**UpdateExpenseReportAccountRequest**](UpdateExpenseReportAccountRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**GetExpenseReportAccount200Response**](GetExpenseReportAccount200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**400** | The request failed validation or could not be processed. Inspect errors, correct the input, and try again. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |
**402** | The company does not have the required feature. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_expense_report_settings**
> update_expense_report_settings(update_expense_report_settings_request)

Retrieve company settings for expense reports

Retrieve company settings for expense reports. Use the parameters and response fields below for this operation.

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

update_expense_report_settings_request = accounting_sh.UpdateExpenseReportSettingsRequest() # UpdateExpenseReportSettingsRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Retrieve company settings for expense reports
    api_response = accounting.expense_reports_api.update_expense_report_settings(update_expense_report_settings_request)
    print("The response of ExpenseReportsApi->update_expense_report_settings:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpenseReportsApi->update_expense_report_settings: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_expense_report_settings_request** | [**UpdateExpenseReportSettingsRequest**](UpdateExpenseReportSettingsRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**UpdateExpenseReportSettings200Response**](UpdateExpenseReportSettings200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for this operation. Returned fields are described below. |  -  |
**500** | An unexpected server error occurred. Inspect the response before deciding whether it is safe to retry a mutation. |  -  |
**401** | Authentication is missing, invalid or expired. Supply a valid API credential or user session. |  -  |
**403** | The authenticated credential or user does not have permission to perform this operation. |  -  |
**400** | The request failed validation or could not be processed. Inspect errors, correct the input, and try again. |  -  |
**404** | The operation could not find the requested resource. Check the identifier and company context. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_expense_report_settings**
> verify_expense_report_settings(verify_expense_report_settings_request)

Verify expense reports settings

Verify expense reports settings. Use the parameters and response fields below for this operation. Requires at least one permission: `edit.company.settings`. Requires company feature(s): `expense_report`. Returns 402 if unavailable.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

verify_expense_report_settings_request = accounting_sh.VerifyExpenseReportSettingsRequest() # VerifyExpenseReportSettingsRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Verify expense reports settings
    api_response = accounting.expense_reports_api.verify_expense_report_settings(verify_expense_report_settings_request)
    print("The response of ExpenseReportsApi->verify_expense_report_settings:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpenseReportsApi->verify_expense_report_settings: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verify_expense_report_settings_request** | [**VerifyExpenseReportSettingsRequest**](VerifyExpenseReportSettingsRequest.md)| Send a JSON object with the fields below. Fields marked required must be supplied. | 

### Return type

[**VerifyExpenseReportSettings200Response**](VerifyExpenseReportSettings200Response.md)

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

