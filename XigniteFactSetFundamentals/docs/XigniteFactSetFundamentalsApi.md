# swagger_client.XigniteFactSetFundamentalsApi

All URIs are relative to *https://factsetfundamentals.xignite.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**x_fact_set_fundamentals_get_balance_sheets_get**](XigniteFactSetFundamentalsApi.md#x_fact_set_fundamentals_get_balance_sheets_get) | **GET** /xFactSetFundamentals/GetBalanceSheets | 
[**x_fact_set_fundamentals_get_cash_flow_statements_get**](XigniteFactSetFundamentalsApi.md#x_fact_set_fundamentals_get_cash_flow_statements_get) | **GET** /xFactSetFundamentals/GetCashFlowStatements | 
[**x_fact_set_fundamentals_get_financial_statements_get**](XigniteFactSetFundamentalsApi.md#x_fact_set_fundamentals_get_financial_statements_get) | **GET** /xFactSetFundamentals/GetFinancialStatements | 
[**x_fact_set_fundamentals_get_fundamentals_daily_range_get**](XigniteFactSetFundamentalsApi.md#x_fact_set_fundamentals_get_fundamentals_daily_range_get) | **GET** /xFactSetFundamentals/GetFundamentalsDailyRange | 
[**x_fact_set_fundamentals_get_fundamentals_fiscal_range_get**](XigniteFactSetFundamentalsApi.md#x_fact_set_fundamentals_get_fundamentals_fiscal_range_get) | **GET** /xFactSetFundamentals/GetFundamentalsFiscalRange | 
[**x_fact_set_fundamentals_get_fundamentals_get**](XigniteFactSetFundamentalsApi.md#x_fact_set_fundamentals_get_fundamentals_get) | **GET** /xFactSetFundamentals/GetFundamentals | 
[**x_fact_set_fundamentals_get_income_statements_get**](XigniteFactSetFundamentalsApi.md#x_fact_set_fundamentals_get_income_statements_get) | **GET** /xFactSetFundamentals/GetIncomeStatements | 
[**x_fact_set_fundamentals_get_latest_fundamentals_get**](XigniteFactSetFundamentalsApi.md#x_fact_set_fundamentals_get_latest_fundamentals_get) | **GET** /xFactSetFundamentals/GetLatestFundamentals | 
[**x_fact_set_fundamentals_list_companies_get**](XigniteFactSetFundamentalsApi.md#x_fact_set_fundamentals_list_companies_get) | **GET** /xFactSetFundamentals/ListCompanies | 
[**x_fact_set_fundamentals_list_exchanges_by_region_get**](XigniteFactSetFundamentalsApi.md#x_fact_set_fundamentals_list_exchanges_by_region_get) | **GET** /xFactSetFundamentals/ListExchangesByRegion | 
[**x_fact_set_fundamentals_list_exchanges_get**](XigniteFactSetFundamentalsApi.md#x_fact_set_fundamentals_list_exchanges_get) | **GET** /xFactSetFundamentals/ListExchanges | 
[**x_fact_set_fundamentals_list_fundamentals_by_data_group_get**](XigniteFactSetFundamentalsApi.md#x_fact_set_fundamentals_list_fundamentals_by_data_group_get) | **GET** /xFactSetFundamentals/ListFundamentalsByDataGroup | 
[**x_fact_set_fundamentals_list_fundamentals_get**](XigniteFactSetFundamentalsApi.md#x_fact_set_fundamentals_list_fundamentals_get) | **GET** /xFactSetFundamentals/ListFundamentals | 
[**x_fact_set_fundamentals_list_sectors_and_industries_get**](XigniteFactSetFundamentalsApi.md#x_fact_set_fundamentals_list_sectors_and_industries_get) | **GET** /xFactSetFundamentals/ListSectorsAndIndustries | 
[**x_fact_set_fundamentals_search_fundamentals_get**](XigniteFactSetFundamentalsApi.md#x_fact_set_fundamentals_search_fundamentals_get) | **GET** /xFactSetFundamentals/SearchFundamentals | 

# **x_fact_set_fundamentals_get_balance_sheets_get**
> list[CompanyBalanceSheet] x_fact_set_fundamentals_get_balance_sheets_get(identifiers=identifiers, identifier_type=identifier_type, as_of_date=as_of_date, report_type=report_type, exclude_restated=exclude_restated, updated_since=updated_since)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: basic
configuration = swagger_client.Configuration()
configuration.api_key['_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['_token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.XigniteFactSetFundamentalsApi(swagger_client.ApiClient(configuration))
identifiers = 'identifiers_example' # str |  (optional)
identifier_type = 'identifier_type_example' # str |  (optional)
as_of_date = 'as_of_date_example' # str |  (optional)
report_type = 'report_type_example' # str |  (optional)
exclude_restated = 'exclude_restated_example' # str |  (optional)
updated_since = 'updated_since_example' # str |  (optional)

try:
    api_response = api_instance.x_fact_set_fundamentals_get_balance_sheets_get(identifiers=identifiers, identifier_type=identifier_type, as_of_date=as_of_date, report_type=report_type, exclude_restated=exclude_restated, updated_since=updated_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XigniteFactSetFundamentalsApi->x_fact_set_fundamentals_get_balance_sheets_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifiers** | **str**|  | [optional] 
 **identifier_type** | **str**|  | [optional] 
 **as_of_date** | **str**|  | [optional] 
 **report_type** | **str**|  | [optional] 
 **exclude_restated** | **str**|  | [optional] 
 **updated_since** | **str**|  | [optional] 

### Return type

[**list[CompanyBalanceSheet]**](CompanyBalanceSheet.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **x_fact_set_fundamentals_get_cash_flow_statements_get**
> list[CompanyCashFlowStatement] x_fact_set_fundamentals_get_cash_flow_statements_get(identifiers=identifiers, identifier_type=identifier_type, as_of_date=as_of_date, report_type=report_type, exclude_restated=exclude_restated, updated_since=updated_since)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: basic
configuration = swagger_client.Configuration()
configuration.api_key['_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['_token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.XigniteFactSetFundamentalsApi(swagger_client.ApiClient(configuration))
identifiers = 'identifiers_example' # str |  (optional)
identifier_type = 'identifier_type_example' # str |  (optional)
as_of_date = 'as_of_date_example' # str |  (optional)
report_type = 'report_type_example' # str |  (optional)
exclude_restated = 'exclude_restated_example' # str |  (optional)
updated_since = 'updated_since_example' # str |  (optional)

try:
    api_response = api_instance.x_fact_set_fundamentals_get_cash_flow_statements_get(identifiers=identifiers, identifier_type=identifier_type, as_of_date=as_of_date, report_type=report_type, exclude_restated=exclude_restated, updated_since=updated_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XigniteFactSetFundamentalsApi->x_fact_set_fundamentals_get_cash_flow_statements_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifiers** | **str**|  | [optional] 
 **identifier_type** | **str**|  | [optional] 
 **as_of_date** | **str**|  | [optional] 
 **report_type** | **str**|  | [optional] 
 **exclude_restated** | **str**|  | [optional] 
 **updated_since** | **str**|  | [optional] 

### Return type

[**list[CompanyCashFlowStatement]**](CompanyCashFlowStatement.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **x_fact_set_fundamentals_get_financial_statements_get**
> list[CompanyFinancialStatements] x_fact_set_fundamentals_get_financial_statements_get(identifiers=identifiers, identifier_type=identifier_type, statement_types=statement_types, as_of_date=as_of_date, report_type=report_type, exclude_restated=exclude_restated)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: basic
configuration = swagger_client.Configuration()
configuration.api_key['_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['_token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.XigniteFactSetFundamentalsApi(swagger_client.ApiClient(configuration))
identifiers = 'identifiers_example' # str |  (optional)
identifier_type = 'identifier_type_example' # str |  (optional)
statement_types = 'statement_types_example' # str |  (optional)
as_of_date = 'as_of_date_example' # str |  (optional)
report_type = 'report_type_example' # str |  (optional)
exclude_restated = 'exclude_restated_example' # str |  (optional)

try:
    api_response = api_instance.x_fact_set_fundamentals_get_financial_statements_get(identifiers=identifiers, identifier_type=identifier_type, statement_types=statement_types, as_of_date=as_of_date, report_type=report_type, exclude_restated=exclude_restated)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XigniteFactSetFundamentalsApi->x_fact_set_fundamentals_get_financial_statements_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifiers** | **str**|  | [optional] 
 **identifier_type** | **str**|  | [optional] 
 **statement_types** | **str**|  | [optional] 
 **as_of_date** | **str**|  | [optional] 
 **report_type** | **str**|  | [optional] 
 **exclude_restated** | **str**|  | [optional] 

### Return type

[**list[CompanyFinancialStatements]**](CompanyFinancialStatements.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **x_fact_set_fundamentals_get_fundamentals_daily_range_get**
> list[CompanyFundamentals] x_fact_set_fundamentals_get_fundamentals_daily_range_get(identifiers=identifiers, identifier_type=identifier_type, fundamental_types=fundamental_types, start_date=start_date, end_date=end_date, report_type=report_type, exclude_restated=exclude_restated, updated_since=updated_since)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: basic
configuration = swagger_client.Configuration()
configuration.api_key['_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['_token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.XigniteFactSetFundamentalsApi(swagger_client.ApiClient(configuration))
identifiers = 'identifiers_example' # str |  (optional)
identifier_type = 'identifier_type_example' # str |  (optional)
fundamental_types = 'fundamental_types_example' # str |  (optional)
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
report_type = 'report_type_example' # str |  (optional)
exclude_restated = 'exclude_restated_example' # str |  (optional)
updated_since = 'updated_since_example' # str |  (optional)

try:
    api_response = api_instance.x_fact_set_fundamentals_get_fundamentals_daily_range_get(identifiers=identifiers, identifier_type=identifier_type, fundamental_types=fundamental_types, start_date=start_date, end_date=end_date, report_type=report_type, exclude_restated=exclude_restated, updated_since=updated_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XigniteFactSetFundamentalsApi->x_fact_set_fundamentals_get_fundamentals_daily_range_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifiers** | **str**|  | [optional] 
 **identifier_type** | **str**|  | [optional] 
 **fundamental_types** | **str**|  | [optional] 
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **report_type** | **str**|  | [optional] 
 **exclude_restated** | **str**|  | [optional] 
 **updated_since** | **str**|  | [optional] 

### Return type

[**list[CompanyFundamentals]**](CompanyFundamentals.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **x_fact_set_fundamentals_get_fundamentals_fiscal_range_get**
> list[CompanyFundamentals] x_fact_set_fundamentals_get_fundamentals_fiscal_range_get(identifiers=identifiers, identifier_type=identifier_type, fundamental_types=fundamental_types, start_date=start_date, end_date=end_date, report_type=report_type, exclude_restated=exclude_restated, updated_since=updated_since)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: basic
configuration = swagger_client.Configuration()
configuration.api_key['_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['_token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.XigniteFactSetFundamentalsApi(swagger_client.ApiClient(configuration))
identifiers = 'identifiers_example' # str |  (optional)
identifier_type = 'identifier_type_example' # str |  (optional)
fundamental_types = 'fundamental_types_example' # str |  (optional)
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
report_type = 'report_type_example' # str |  (optional)
exclude_restated = 'exclude_restated_example' # str |  (optional)
updated_since = 'updated_since_example' # str |  (optional)

try:
    api_response = api_instance.x_fact_set_fundamentals_get_fundamentals_fiscal_range_get(identifiers=identifiers, identifier_type=identifier_type, fundamental_types=fundamental_types, start_date=start_date, end_date=end_date, report_type=report_type, exclude_restated=exclude_restated, updated_since=updated_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XigniteFactSetFundamentalsApi->x_fact_set_fundamentals_get_fundamentals_fiscal_range_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifiers** | **str**|  | [optional] 
 **identifier_type** | **str**|  | [optional] 
 **fundamental_types** | **str**|  | [optional] 
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **report_type** | **str**|  | [optional] 
 **exclude_restated** | **str**|  | [optional] 
 **updated_since** | **str**|  | [optional] 

### Return type

[**list[CompanyFundamentals]**](CompanyFundamentals.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **x_fact_set_fundamentals_get_fundamentals_get**
> list[CompanyFundamentals] x_fact_set_fundamentals_get_fundamentals_get(identifiers=identifiers, identifier_type=identifier_type, fundamental_types=fundamental_types, report_type=report_type, exclude_restated=exclude_restated, as_of_date=as_of_date, updated_since=updated_since)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: basic
configuration = swagger_client.Configuration()
configuration.api_key['_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['_token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.XigniteFactSetFundamentalsApi(swagger_client.ApiClient(configuration))
identifiers = 'identifiers_example' # str |  (optional)
identifier_type = 'identifier_type_example' # str |  (optional)
fundamental_types = 'fundamental_types_example' # str |  (optional)
report_type = 'report_type_example' # str |  (optional)
exclude_restated = 'exclude_restated_example' # str |  (optional)
as_of_date = 'as_of_date_example' # str |  (optional)
updated_since = 'updated_since_example' # str |  (optional)

try:
    api_response = api_instance.x_fact_set_fundamentals_get_fundamentals_get(identifiers=identifiers, identifier_type=identifier_type, fundamental_types=fundamental_types, report_type=report_type, exclude_restated=exclude_restated, as_of_date=as_of_date, updated_since=updated_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XigniteFactSetFundamentalsApi->x_fact_set_fundamentals_get_fundamentals_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifiers** | **str**|  | [optional] 
 **identifier_type** | **str**|  | [optional] 
 **fundamental_types** | **str**|  | [optional] 
 **report_type** | **str**|  | [optional] 
 **exclude_restated** | **str**|  | [optional] 
 **as_of_date** | **str**|  | [optional] 
 **updated_since** | **str**|  | [optional] 

### Return type

[**list[CompanyFundamentals]**](CompanyFundamentals.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **x_fact_set_fundamentals_get_income_statements_get**
> list[CompanyIncomeStatement] x_fact_set_fundamentals_get_income_statements_get(identifiers=identifiers, identifier_type=identifier_type, as_of_date=as_of_date, report_type=report_type, exclude_restated=exclude_restated, updated_since=updated_since)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: basic
configuration = swagger_client.Configuration()
configuration.api_key['_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['_token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.XigniteFactSetFundamentalsApi(swagger_client.ApiClient(configuration))
identifiers = 'identifiers_example' # str |  (optional)
identifier_type = 'identifier_type_example' # str |  (optional)
as_of_date = 'as_of_date_example' # str |  (optional)
report_type = 'report_type_example' # str |  (optional)
exclude_restated = 'exclude_restated_example' # str |  (optional)
updated_since = 'updated_since_example' # str |  (optional)

try:
    api_response = api_instance.x_fact_set_fundamentals_get_income_statements_get(identifiers=identifiers, identifier_type=identifier_type, as_of_date=as_of_date, report_type=report_type, exclude_restated=exclude_restated, updated_since=updated_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XigniteFactSetFundamentalsApi->x_fact_set_fundamentals_get_income_statements_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifiers** | **str**|  | [optional] 
 **identifier_type** | **str**|  | [optional] 
 **as_of_date** | **str**|  | [optional] 
 **report_type** | **str**|  | [optional] 
 **exclude_restated** | **str**|  | [optional] 
 **updated_since** | **str**|  | [optional] 

### Return type

[**list[CompanyIncomeStatement]**](CompanyIncomeStatement.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **x_fact_set_fundamentals_get_latest_fundamentals_get**
> list[CompanyFundamentals] x_fact_set_fundamentals_get_latest_fundamentals_get(identifiers=identifiers, identifier_type=identifier_type, fundamental_types=fundamental_types, updated_since=updated_since)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: basic
configuration = swagger_client.Configuration()
configuration.api_key['_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['_token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.XigniteFactSetFundamentalsApi(swagger_client.ApiClient(configuration))
identifiers = 'identifiers_example' # str |  (optional)
identifier_type = 'identifier_type_example' # str |  (optional)
fundamental_types = 'fundamental_types_example' # str |  (optional)
updated_since = 'updated_since_example' # str |  (optional)

try:
    api_response = api_instance.x_fact_set_fundamentals_get_latest_fundamentals_get(identifiers=identifiers, identifier_type=identifier_type, fundamental_types=fundamental_types, updated_since=updated_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XigniteFactSetFundamentalsApi->x_fact_set_fundamentals_get_latest_fundamentals_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifiers** | **str**|  | [optional] 
 **identifier_type** | **str**|  | [optional] 
 **fundamental_types** | **str**|  | [optional] 
 **updated_since** | **str**|  | [optional] 

### Return type

[**list[CompanyFundamentals]**](CompanyFundamentals.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **x_fact_set_fundamentals_list_companies_get**
> CompanyList x_fact_set_fundamentals_list_companies_get(market_identification_code=market_identification_code, start_symbol=start_symbol, end_symbol=end_symbol)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: basic
configuration = swagger_client.Configuration()
configuration.api_key['_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['_token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.XigniteFactSetFundamentalsApi(swagger_client.ApiClient(configuration))
market_identification_code = 'market_identification_code_example' # str |  (optional)
start_symbol = 'start_symbol_example' # str |  (optional)
end_symbol = 'end_symbol_example' # str |  (optional)

try:
    api_response = api_instance.x_fact_set_fundamentals_list_companies_get(market_identification_code=market_identification_code, start_symbol=start_symbol, end_symbol=end_symbol)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XigniteFactSetFundamentalsApi->x_fact_set_fundamentals_list_companies_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market_identification_code** | **str**|  | [optional] 
 **start_symbol** | **str**|  | [optional] 
 **end_symbol** | **str**|  | [optional] 

### Return type

[**CompanyList**](CompanyList.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **x_fact_set_fundamentals_list_exchanges_by_region_get**
> ExchangeList x_fact_set_fundamentals_list_exchanges_by_region_get(regions=regions)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: basic
configuration = swagger_client.Configuration()
configuration.api_key['_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['_token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.XigniteFactSetFundamentalsApi(swagger_client.ApiClient(configuration))
regions = 'regions_example' # str |  (optional)

try:
    api_response = api_instance.x_fact_set_fundamentals_list_exchanges_by_region_get(regions=regions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XigniteFactSetFundamentalsApi->x_fact_set_fundamentals_list_exchanges_by_region_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **regions** | **str**|  | [optional] 

### Return type

[**ExchangeList**](ExchangeList.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **x_fact_set_fundamentals_list_exchanges_get**
> ExchangeList x_fact_set_fundamentals_list_exchanges_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: basic
configuration = swagger_client.Configuration()
configuration.api_key['_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['_token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.XigniteFactSetFundamentalsApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.x_fact_set_fundamentals_list_exchanges_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XigniteFactSetFundamentalsApi->x_fact_set_fundamentals_list_exchanges_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ExchangeList**](ExchangeList.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **x_fact_set_fundamentals_list_fundamentals_by_data_group_get**
> FundamentalDescriptionList x_fact_set_fundamentals_list_fundamentals_by_data_group_get(data_groups=data_groups)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: basic
configuration = swagger_client.Configuration()
configuration.api_key['_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['_token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.XigniteFactSetFundamentalsApi(swagger_client.ApiClient(configuration))
data_groups = 'data_groups_example' # str |  (optional)

try:
    api_response = api_instance.x_fact_set_fundamentals_list_fundamentals_by_data_group_get(data_groups=data_groups)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XigniteFactSetFundamentalsApi->x_fact_set_fundamentals_list_fundamentals_by_data_group_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_groups** | **str**|  | [optional] 

### Return type

[**FundamentalDescriptionList**](FundamentalDescriptionList.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **x_fact_set_fundamentals_list_fundamentals_get**
> FundamentalDescriptionList x_fact_set_fundamentals_list_fundamentals_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: basic
configuration = swagger_client.Configuration()
configuration.api_key['_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['_token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.XigniteFactSetFundamentalsApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.x_fact_set_fundamentals_list_fundamentals_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XigniteFactSetFundamentalsApi->x_fact_set_fundamentals_list_fundamentals_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FundamentalDescriptionList**](FundamentalDescriptionList.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **x_fact_set_fundamentals_list_sectors_and_industries_get**
> SectorList x_fact_set_fundamentals_list_sectors_and_industries_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: basic
configuration = swagger_client.Configuration()
configuration.api_key['_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['_token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.XigniteFactSetFundamentalsApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.x_fact_set_fundamentals_list_sectors_and_industries_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XigniteFactSetFundamentalsApi->x_fact_set_fundamentals_list_sectors_and_industries_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SectorList**](SectorList.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **x_fact_set_fundamentals_search_fundamentals_get**
> FundamentalDescriptionList x_fact_set_fundamentals_search_fundamentals_get(pattern=pattern)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: basic
configuration = swagger_client.Configuration()
configuration.api_key['_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['_token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.XigniteFactSetFundamentalsApi(swagger_client.ApiClient(configuration))
pattern = 'pattern_example' # str |  (optional)

try:
    api_response = api_instance.x_fact_set_fundamentals_search_fundamentals_get(pattern=pattern)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XigniteFactSetFundamentalsApi->x_fact_set_fundamentals_search_fundamentals_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pattern** | **str**|  | [optional] 

### Return type

[**FundamentalDescriptionList**](FundamentalDescriptionList.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

