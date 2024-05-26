# accounting_sh.PaymentsApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_payment**](PaymentsApi.md#add_payment) | **POST** /expenses/payments | Add a payment
[**delete_payment**](PaymentsApi.md#delete_payment) | **DELETE** /expenses/payments/{uuid} | Delete a payment
[**get_payment**](PaymentsApi.md#get_payment) | **GET** /expenses/payments/{uuid} | Get a payment
[**list_payments**](PaymentsApi.md#list_payments) | **GET** /expenses/payments | List company&#39;s payments
[**update_payment**](PaymentsApi.md#update_payment) | **PUT** /expenses/payments/{uuid} | Update a payment


# **add_payment**
> add_payment(add_payment_request)

Add a payment

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_payment_request = accounting_sh.AddPaymentRequest() # AddPaymentRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Add a payment
    api_response = accounting.payments_api.add_payment(add_payment_request)
    print("The response of PaymentsApi->add_payment:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->add_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_payment_request** | [**AddPaymentRequest**](AddPaymentRequest.md)|  | 

### Return type

[**AddPayment200Response**](AddPayment200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_payment**
> delete_payment(uuid)

Delete a payment

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The payment uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete a payment
    api_response = accounting.payments_api.delete_payment(uuid)
    print("The response of PaymentsApi->delete_payment:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->delete_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The payment uuid | 

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

# **get_payment**
> get_payment(uuid)

Get a payment

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The payment uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a payment
    api_response = accounting.payments_api.get_payment(uuid)
    print("The response of PaymentsApi->get_payment:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->get_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The payment uuid | 

### Return type

[**AddPayment200Response**](AddPayment200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_payments**
> list_payments(fields=fields, page=page, per_page=per_page)

List company's payments

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
    # List company's payments
    api_response = accounting.payments_api.list_payments(fields=fields, page=page, per_page=per_page)
    print("The response of PaymentsApi->list_payments:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->list_payments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| A comma separated list of fields requested in the response | [optional] 
 **page** | **str**| The response page | [optional] 
 **per_page** | **str**| The number of items per page | [optional] 

### Return type

[**ListPayments200Response**](ListPayments200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_payment**
> update_payment(uuid, add_payment_request)

Update a payment

### Example


```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The payment uuid
add_payment_request = accounting_sh.AddPaymentRequest() # AddPaymentRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a payment
    api_response = accounting.payments_api.update_payment(uuid, add_payment_request)
    print("The response of PaymentsApi->update_payment:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->update_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The payment uuid | 
 **add_payment_request** | [**AddPaymentRequest**](AddPaymentRequest.md)|  | 

### Return type

[**AddPayment200Response**](AddPayment200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

