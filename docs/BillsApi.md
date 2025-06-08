# accounting_sh.BillsApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_bill**](BillsApi.md#add_bill) | **POST** /expenses/bills | Add a bill
[**add_bill_payment**](BillsApi.md#add_bill_payment) | **POST** /expenses/bills/{uuid}/payments | Add a bill payment
[**delete_bill**](BillsApi.md#delete_bill) | **DELETE** /expenses/bills/{uuid} | Delete a bill
[**get_bill**](BillsApi.md#get_bill) | **GET** /expenses/bills/{uuid} | Get a bill
[**get_bill_document**](BillsApi.md#get_bill_document) | **GET** /expenses/bills/{uuid}/document | Get a bill in PDF
[**list_bills**](BillsApi.md#list_bills) | **GET** /expenses/bills | List company&#39;s bills
[**update_bill**](BillsApi.md#update_bill) | **PUT** /expenses/bills/{uuid} | Update a bill
[**update_bill_payment**](BillsApi.md#update_bill_payment) | **PUT** /expenses/bills/{uuid}/payments/{payment} | Update a bill payment


# **add_bill**
> add_bill(add_bill_request)

Add a bill

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_bill_request = accounting_sh.AddBillRequest() # AddBillRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Add a bill
    api_response = accounting.bills_api.add_bill(add_bill_request)
    print("The response of BillsApi->add_bill:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillsApi->add_bill: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_bill_request** | [**AddBillRequest**](AddBillRequest.md)|  | 

### Return type

[**AddBill200Response**](AddBill200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_bill_payment**
> add_bill_payment(uuid, add_bill_payment_request)

Add a bill payment

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The bill uuid
add_bill_payment_request = accounting_sh.AddBillPaymentRequest() # AddBillPaymentRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Add a bill payment
    api_response = accounting.bills_api.add_bill_payment(uuid, add_bill_payment_request)
    print("The response of BillsApi->add_bill_payment:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillsApi->add_bill_payment: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The bill uuid | 
 **add_bill_payment_request** | [**AddBillPaymentRequest**](AddBillPaymentRequest.md)|  | 

### Return type

[**GetBill200Response**](GetBill200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bill**
> delete_bill(uuid)

Delete a bill

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The bill uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete a bill
    api_response = accounting.bills_api.delete_bill(uuid)
    print("The response of BillsApi->delete_bill:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillsApi->delete_bill: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The bill uuid | 

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

# **get_bill**
> get_bill(uuid)

Get a bill

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The bill uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a bill
    api_response = accounting.bills_api.get_bill(uuid)
    print("The response of BillsApi->get_bill:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillsApi->get_bill: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The bill uuid | 

### Return type

[**GetBill200Response**](GetBill200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bill_document**
> get_bill_document(uuid)

Get a bill in PDF

This endpoint generate a bill in PDF if `selfbilling` is set to true

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The invoice uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a bill in PDF
   accounting.bills_api.get_bill_document(uuid)
except ApiException as e:
    print("Exception when calling BillsApi->get_bill_document: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The invoice uuid | 

### Return type

void (empty response body)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_bills**
> list_bills(fields=fields, page=page, per_page=per_page)

List company's bills

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
    # List company's bills
    api_response = accounting.bills_api.list_bills(fields=fields, page=page, per_page=per_page)
    print("The response of BillsApi->list_bills:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillsApi->list_bills: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| A comma separated list of fields requested in the response | [optional] 
 **page** | **str**| The response page | [optional] 
 **per_page** | **str**| The number of items per page | [optional] 

### Return type

[**ListBills200Response**](ListBills200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bill**
> update_bill(uuid, add_bill_request)

Update a bill

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The bill uuid
add_bill_request = accounting_sh.AddBillRequest() # AddBillRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a bill
    api_response = accounting.bills_api.update_bill(uuid, add_bill_request)
    print("The response of BillsApi->update_bill:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillsApi->update_bill: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The bill uuid | 
 **add_bill_request** | [**AddBillRequest**](AddBillRequest.md)|  | 

### Return type

[**GetBill200Response**](GetBill200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bill_payment**
> update_bill_payment(uuid, payment, add_bill_payment_request)

Update a bill payment

### Example

* Bearer (Api Key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = 'uuid_example' # str | The bill uuid
payment = 'payment_example' # str | The bill payment uuid
add_bill_payment_request = accounting_sh.AddBillPaymentRequest() # AddBillPaymentRequest | 

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a bill payment
    api_response = accounting.bills_api.update_bill_payment(uuid, payment, add_bill_payment_request)
    print("The response of BillsApi->update_bill_payment:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillsApi->update_bill_payment: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The bill uuid | 
 **payment** | **str**| The bill payment uuid | 
 **add_bill_payment_request** | [**AddBillPaymentRequest**](AddBillPaymentRequest.md)|  | 

### Return type

[**GetBill200Response**](GetBill200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |  -  |
**401** | Authentication is required to access the resource. |  -  |
**403** | The server has understood the request, but refuses to execute it. |  -  |
**404** | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

