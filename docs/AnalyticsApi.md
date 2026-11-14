# accounting_sh.AnalyticsApi

All URIs are relative to *https://api.accounting.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analytics_cards**](AnalyticsApi.md#analytics_cards) | **GET** /analytics/cards/{group} | Grouped analytics statistic cards
[**analytics_catalog**](AnalyticsApi.md#analytics_catalog) | **GET** /analytics | Available analytics graphs and card groups
[**analytics_graph**](AnalyticsApi.md#analytics_graph) | **GET** /analytics/graphs/{graph} | One frontend-ready analytics graph


# **analytics_cards**
> analytics_cards(group, start=start, end=end, interval=interval, limit=limit, currency=currency)

Grouped analytics statistic cards

Returns the selected statistic-card group for a custom date range. Requires `analytics`. Expense self-only restrictions and company feature gates still apply. Cards expose units, labels, comparisons where supported and calculation metadata; monetary values use exact decimal strings.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

group = 'group_example' # str | Select a related statistics-card group. See GET /analytics for available group metadata.
start = '2013-10-20' # date | Inclusive first activity date in YYYY-MM-DD format. (optional)
end = '2013-10-20' # date | Inclusive last activity date; also the balance as-of date where applicable. (optional)
interval = 'month' # str | Calendar bucket for time-series graphs. (optional) (default to 'month')
limit = 10 # int | Maximum ranked categories where the graph supports a limit. (optional) (default to 10)
currency = 'currency_example' # str | Optional ISO 4217 currency filter; does not request arbitrary currency conversion. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # Grouped analytics statistic cards
    api_response = accounting.analytics_api.analytics_cards(group, start=start, end=end, interval=interval, limit=limit, currency=currency)
    print("The response of AnalyticsApi->analytics_cards:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->analytics_cards: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| Select a related statistics-card group. See GET /analytics for available group metadata. | 
 **start** | **date**| Inclusive first activity date in YYYY-MM-DD format. | [optional] 
 **end** | **date**| Inclusive last activity date; also the balance as-of date where applicable. | [optional] 
 **interval** | **str**| Calendar bucket for time-series graphs. | [optional] [default to &#39;month&#39;]
 **limit** | **int**| Maximum ranked categories where the graph supports a limit. | [optional] [default to 10]
 **currency** | **str**| Optional ISO 4217 currency filter; does not request arbitrary currency conversion. | [optional] 

### Return type

[**AnalyticsCards200Response**](AnalyticsCards200Response.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Grouped statistic cards |  -  |
**400** | Invalid filters |  -  |
**401** | Authentication required |  -  |
**403** | Statistics permission missing or expense access restricted |  -  |
**404** | Unknown card group |  -  |
**503** | Analytics schema or refreshed data unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **analytics_catalog**
> analytics_catalog()

Available analytics graphs and card groups

Requires `analytics`. Lists available graph and grouped-card identifiers. Uses the authenticated company; no company override is accepted. This metadata request never refreshes views.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint


accounting = accounting_sh.Accounting("access_token")
try:
    # Available analytics graphs and card groups
    api_response = accounting.analytics_api.analytics_catalog()
    print("The response of AnalyticsApi->analytics_catalog:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->analytics_catalog: %s\n" % e)

```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Permission-filtered graph and card definitions |  -  |
**401** | Authentication required |  -  |
**403** | Authenticated company required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **analytics_graph**
> analytics_graph(graph, start=start, end=end, interval=interval, limit=limit, currency=currency)

One frontend-ready analytics graph

One HTTP request returns one graph with chart type, data, labels, series/legend, units, and calculation metadata. Requires `analytics`. Expense self-only restrictions and company feature gates still apply. Reads materialized analytics only; never refreshes in HTTP. Decimal monetary values are strings.

### Example

* Bearer (API key) Authentication (bearer):

```python
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

graph = 'graph_example' # str | Select one of the implemented graph identifiers. See GET /analytics for localized titles, metric IDs, bases and feature requirements.
start = '2013-10-20' # date | Inclusive first activity date in YYYY-MM-DD format. (optional)
end = '2013-10-20' # date | Inclusive last activity date; also the balance as-of date where applicable. (optional)
interval = 'month' # str | Calendar bucket for time-series graphs. (optional) (default to 'month')
limit = 10 # int | Maximum ranked categories where the graph supports a limit. (optional) (default to 10)
currency = 'currency_example' # str | Optional ISO 4217 currency filter; does not request arbitrary currency conversion. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # One frontend-ready analytics graph
    api_response = accounting.analytics_api.analytics_graph(graph, start=start, end=end, interval=interval, limit=limit, currency=currency)
    print("The response of AnalyticsApi->analytics_graph:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->analytics_graph: %s\n" % e)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **graph** | **str**| Select one of the implemented graph identifiers. See GET /analytics for localized titles, metric IDs, bases and feature requirements. | 
 **start** | **date**| Inclusive first activity date in YYYY-MM-DD format. | [optional] 
 **end** | **date**| Inclusive last activity date; also the balance as-of date where applicable. | [optional] 
 **interval** | **str**| Calendar bucket for time-series graphs. | [optional] [default to &#39;month&#39;]
 **limit** | **int**| Maximum ranked categories where the graph supports a limit. | [optional] [default to 10]
 **currency** | **str**| Optional ISO 4217 currency filter; does not request arbitrary currency conversion. | [optional] 

### Return type

[**AnalyticsGraphResponse**](AnalyticsGraphResponse.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A complete graph result |  -  |
**400** | Invalid date range, interval, limit or currency |  -  |
**401** | Authentication required |  -  |
**403** | Statistics permission missing or expense access restricted |  -  |
**404** | Unknown graph |  -  |
**503** | Analytics schema or refreshed data unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

