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

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_expense_report_request = accounting_sh.AddExpenseReportRequest() # AddExpenseReportRequest | 

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
 **add_expense_report_request** | [**AddExpenseReportRequest**](AddExpenseReportRequest.md)|  | 

### Return type

[**AddExpenseReport200Response**](AddExpenseReport200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_expense_report**
> delete_expense_report(uuid)

Delete an expense report

### Example


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

# **expense_report_o_auth_login**
> expense_report_o_auth_login(method)

OAuth Login

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
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_expense_report**
> get_expense_report(uuid)

Get an expense report

### Example


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
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_expense_report_account**
> get_expense_report_account()

Get the currently connected expense report user details

### Example


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
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_expense_report_user**
> get_expense_report_user(uuid)

Get an user details

### Example


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
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_expense_reports**
> list_expense_reports(fields=fields, page=page, per_page=per_page)

List company's expense reports.

List company's expense reports. If the token used has the `expense_report.limited_to_self` permission, this will only list the user's expense reports

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
    # List company's expense reports.
    api_response = accounting.expense_reports_api.list_expense_reports(fields=fields, page=page, per_page=per_page)
    print("The response of ExpenseReportsApi->list_expense_reports:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpenseReportsApi->list_expense_reports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| A comma separated list of fields requested in the response | [optional] 
 **page** | **str**| The response page | [optional] 
 **per_page** | **str**| The number of items per page | [optional] 

### Return type

[**ListExpenseReports200Response**](ListExpenseReports200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_expense_report_login_email**
> send_expense_report_login_email(send_expense_report_login_email_request)

Request login email

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

send_expense_report_login_email_request = accounting_sh.SendExpenseReportLoginEmailRequest() # SendExpenseReportLoginEmailRequest | 

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
 **send_expense_report_login_email_request** | [**SendExpenseReportLoginEmailRequest**](SendExpenseReportLoginEmailRequest.md)|  | 

### Return type

[**DeleteAccountConnection200Response**](DeleteAccountConnection200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_expense_report**
> update_expense_report(uuid, add_expense_report_request)

Update an expense report

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The expense report uuid
add_expense_report_request = accounting_sh.AddExpenseReportRequest() # AddExpenseReportRequest | 

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
 **add_expense_report_request** | [**AddExpenseReportRequest**](AddExpenseReportRequest.md)|  | 

### Return type

[**AddExpenseReport200Response**](AddExpenseReport200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_expense_report_account**
> update_expense_report_account(update_expense_report_account_request)

Update the currently connected expense report user

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

update_expense_report_account_request = accounting_sh.UpdateExpenseReportAccountRequest() # UpdateExpenseReportAccountRequest | 

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
 **update_expense_report_account_request** | [**UpdateExpenseReportAccountRequest**](UpdateExpenseReportAccountRequest.md)|  | 

### Return type

[**GetExpenseReportAccount200Response**](GetExpenseReportAccount200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_expense_report_settings**
> update_expense_report_settings(update_expense_report_settings_request)

Retrieve company settings for expense reports

At least an url or a company must be provided

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

update_expense_report_settings_request = accounting_sh.UpdateExpenseReportSettingsRequest() # UpdateExpenseReportSettingsRequest | 

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
 **update_expense_report_settings_request** | [**UpdateExpenseReportSettingsRequest**](UpdateExpenseReportSettingsRequest.md)|  | 

### Return type

[**UpdateExpenseReportSettings200Response**](UpdateExpenseReportSettings200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_expense_report_settings**
> verify_expense_report_settings(verify_expense_report_settings_request)

Verify expense reports settings

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

verify_expense_report_settings_request = accounting_sh.VerifyExpenseReportSettingsRequest() # VerifyExpenseReportSettingsRequest | 

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
 **verify_expense_report_settings_request** | [**VerifyExpenseReportSettingsRequest**](VerifyExpenseReportSettingsRequest.md)|  | 

### Return type

[**VerifyExpenseReportSettings200Response**](VerifyExpenseReportSettings200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

