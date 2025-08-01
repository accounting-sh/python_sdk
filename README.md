# accounting-sh


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 8.3.3
- Package version: 1.3.2
- Generator version: 7.6.0-SNAPSHOT
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

For more information, please visit [https://accounting.sh](https://accounting.sh)

## Requirements.

Python 3.10+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install accounting_sh
```

Then import the package:
```python
import accounting_sh
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import accounting_sh
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint


uuid = 'uuid_example' # str | The account uuid
connection = 'connection_example' # str | The connection uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete an account's connection
    api_response = accounting.account_connections_api.delete_account_connection(uuid, connection)
    print("The response of AccountConnectionsApi->delete_account_connection:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountConnectionsApi->delete_account_connection: %s\n" % e)


```

## Documentation for API Endpoints

All URIs are relative to *https://api.accounting.sh*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountConnectionsApi* | [**delete_account_connection**](docs/AccountConnectionsApi.md#delete_account_connection) | **DELETE** /accounts/{uuid}/connect/{connection} | Delete an account&#39;s connection
*AccountConnectionsApi* | [**list_account_connections**](docs/AccountConnectionsApi.md#list_account_connections) | **GET** /accounts/{uuid}/connect | List account&#39;s connections
*AccountConnectionsApi* | [**list_banks**](docs/AccountConnectionsApi.md#list_banks) | **GET** /accounts/{uuid}/connect/banks | List available bank connections
*AccountConnectionsApi* | [**list_connectable_bank_accounts**](docs/AccountConnectionsApi.md#list_connectable_bank_accounts) | **GET** /accounts/{uuid}/connect/accounts | List connectable bank accounts
*AccountConnectionsApi* | [**list_connected_account_transactions**](docs/AccountConnectionsApi.md#list_connected_account_transactions) | **GET** /accounts/{uuid}/connect/{connection} | List the connected account&#39;s transactions
*AccountConnectionsApi* | [**request_bank_connection**](docs/AccountConnectionsApi.md#request_bank_connection) | **POST** /accounts/{uuid}/connect/request | Request a new bank connection
*AccountConnectionsApi* | [**select_bank_account**](docs/AccountConnectionsApi.md#select_bank_account) | **POST** /accounts/{uuid}/connect/accounts | Select a bank account to connect
*AccountingCodesApi* | [**add_accounting_code**](docs/AccountingCodesApi.md#add_accounting_code) | **POST** /accounting/codes | Add an accounting code
*AccountingCodesApi* | [**delete_accounting_code**](docs/AccountingCodesApi.md#delete_accounting_code) | **DELETE** /accounting/codes/{uuid} | Delete an accounting code
*AccountingCodesApi* | [**get_accounting_code**](docs/AccountingCodesApi.md#get_accounting_code) | **GET** /accounting/codes/{uuid} | Get an accounting code
*AccountingCodesApi* | [**list_accounting_codes**](docs/AccountingCodesApi.md#list_accounting_codes) | **GET** /accounting/codes | List company&#39;s accounting code
*AccountingCodesApi* | [**update_accounting_code**](docs/AccountingCodesApi.md#update_accounting_code) | **PUT** /accounting/codes/{uuid} | Update an accounting code
*AccountsApi* | [**add_account**](docs/AccountsApi.md#add_account) | **POST** /accounts | Add an account
*AccountsApi* | [**delete_account**](docs/AccountsApi.md#delete_account) | **DELETE** /accounts/{uuid} | Delete an account
*AccountsApi* | [**get_account**](docs/AccountsApi.md#get_account) | **GET** /accounts/{uuid} | Get an account
*AccountsApi* | [**list_accounts**](docs/AccountsApi.md#list_accounts) | **GET** /accounts | List company&#39;s accounts
*AccountsApi* | [**update_account**](docs/AccountsApi.md#update_account) | **PUT** /accounts/{uuid} | Update an account
*AttachmentsApi* | [**add_attachment**](docs/AttachmentsApi.md#add_attachment) | **POST** /attachments | Add an attachment
*AttachmentsApi* | [**delete_attachment**](docs/AttachmentsApi.md#delete_attachment) | **DELETE** /attachments/{uuid} | Delete an attachment
*AttachmentsApi* | [**get_attachment**](docs/AttachmentsApi.md#get_attachment) | **GET** /attachments/{uuid} | Get an attachment
*AttachmentsApi* | [**list_attachments**](docs/AttachmentsApi.md#list_attachments) | **GET** /attachments | List company&#39;s attachments
*AttachmentsApi* | [**retrieve_attachments**](docs/AttachmentsApi.md#retrieve_attachments) | **GET** /attachments/resource/{resource} | List company&#39;s attachments link to resource
*AttachmentsApi* | [**update_attachment**](docs/AttachmentsApi.md#update_attachment) | **PUT** /attachments/{uuid} | Update an attachment
*AuthApi* | [**auth_init**](docs/AuthApi.md#auth_init) | **GET** /auth/init | Init authentication process
*AuthApi* | [**login**](docs/AuthApi.md#login) | **POST** /auth/login | Login user
*AuthApi* | [**logout**](docs/AuthApi.md#logout) | **GET** /auth/logout | Logout current user
*AuthApi* | [**switch_company**](docs/AuthApi.md#switch_company) | **POST** /auth/switch | Switch to a different company
*BillsApi* | [**add_bill**](docs/BillsApi.md#add_bill) | **POST** /expenses/bills | Add a bill
*BillsApi* | [**add_bill_payment**](docs/BillsApi.md#add_bill_payment) | **POST** /expenses/bills/{uuid}/payments | Add a bill payment
*BillsApi* | [**delete_bill**](docs/BillsApi.md#delete_bill) | **DELETE** /expenses/bills/{uuid} | Delete a bill
*BillsApi* | [**get_bill**](docs/BillsApi.md#get_bill) | **GET** /expenses/bills/{uuid} | Get a bill
*BillsApi* | [**get_bill_document**](docs/BillsApi.md#get_bill_document) | **GET** /expenses/bills/{uuid}/document | Get a bill in PDF
*BillsApi* | [**list_bills**](docs/BillsApi.md#list_bills) | **GET** /expenses/bills | List company&#39;s bills
*BillsApi* | [**update_bill**](docs/BillsApi.md#update_bill) | **PUT** /expenses/bills/{uuid} | Update a bill
*BillsApi* | [**update_bill_payment**](docs/BillsApi.md#update_bill_payment) | **PUT** /expenses/bills/{uuid}/payments/{payment} | Update a bill payment
*CategoriesApi* | [**add_category**](docs/CategoriesApi.md#add_category) | **POST** /categories | Add a category
*CategoriesApi* | [**delete_category**](docs/CategoriesApi.md#delete_category) | **DELETE** /categories/{uuid} | Delete a category
*CategoriesApi* | [**get_category**](docs/CategoriesApi.md#get_category) | **GET** /categories/{uuid} | Get a category
*CategoriesApi* | [**list_categories**](docs/CategoriesApi.md#list_categories) | **GET** /categories | List company&#39;s categories
*CategoriesApi* | [**update_category**](docs/CategoriesApi.md#update_category) | **PUT** /categories/{uuid} | Update a category
*CompaniesApi* | [**add_company**](docs/CompaniesApi.md#add_company) | **POST** /companies | Add a company
*CompaniesApi* | [**delete_company**](docs/CompaniesApi.md#delete_company) | **DELETE** /companies/{uuid} | Delete a company
*CompaniesApi* | [**get_company**](docs/CompaniesApi.md#get_company) | **GET** /companies/{uuid} | Get a company
*CompaniesApi* | [**get_company_customization**](docs/CompaniesApi.md#get_company_customization) | **GET** /companies/{uuid}/customization | Get a company&#39;s customization parameters
*CompaniesApi* | [**get_company_feature_set**](docs/CompaniesApi.md#get_company_feature_set) | **GET** /companies/{uuid}/features | List a company&#39;s feature set
*CompaniesApi* | [**list_companies**](docs/CompaniesApi.md#list_companies) | **GET** /companies | List companies on this instance
*CompaniesApi* | [**update_company**](docs/CompaniesApi.md#update_company) | **PUT** /companies/{uuid} | Update a company
*CompanyStatisticsApi* | [**get_statistics**](docs/CompanyStatisticsApi.md#get_statistics) | **GET** /companies/{uuid}/statistics/period | Get company&#39;s statistic
*ContactsApi* | [**add_contact**](docs/ContactsApi.md#add_contact) | **POST** /contacts | Create a new contact
*ContactsApi* | [**delete_contact**](docs/ContactsApi.md#delete_contact) | **DELETE** /contacts/{uuid} | Delete a contact
*ContactsApi* | [**get_contact**](docs/ContactsApi.md#get_contact) | **GET** /contacts/{uuid} | Retrieve a contact
*ContactsApi* | [**list_contact_bills**](docs/ContactsApi.md#list_contact_bills) | **GET** /contacts/{uuid}/bills | List a contact&#39;s bills
*ContactsApi* | [**list_contact_invoices**](docs/ContactsApi.md#list_contact_invoices) | **GET** /contacts/{uuid}/invoices | List a contact&#39;s invoices
*ContactsApi* | [**list_contacts**](docs/ContactsApi.md#list_contacts) | **GET** /contacts | List company&#39;s contacts
*ContactsApi* | [**update_contact**](docs/ContactsApi.md#update_contact) | **PUT** /contacts/{uuid} | Update a contact
*CountriesApi* | [**get_translated_countries**](docs/CountriesApi.md#get_translated_countries) | **GET** /countries/{lang} | Get translated list of countries
*CredentialsApi* | [**add_credential**](docs/CredentialsApi.md#add_credential) | **POST** /credentials | Add a credential
*CredentialsApi* | [**delete_credential**](docs/CredentialsApi.md#delete_credential) | **DELETE** /credentials/{uuid} | Delete a credential
*CredentialsApi* | [**get_credential**](docs/CredentialsApi.md#get_credential) | **GET** /credentials/{uuid} | Get a credential
*CredentialsApi* | [**list_credentials**](docs/CredentialsApi.md#list_credentials) | **GET** /credentials | List company&#39;s credentials
*CredentialsApi* | [**list_permissions**](docs/CredentialsApi.md#list_permissions) | **GET** /credentials/permissions | List available permissions
*CredentialsApi* | [**me**](docs/CredentialsApi.md#me) | **GET** /me | Get current credential informations
*CredentialsApi* | [**update_credential**](docs/CredentialsApi.md#update_credential) | **PUT** /credentials/{uuid} | Update a credential
*CredentialsApi* | [**userveria**](docs/CredentialsApi.md#userveria) | **POST** /userveria | Exchange a my stantabcorp (userveria) token for an Accounting Token
*CurrencyApi* | [**get_exchange_rate**](docs/CurrencyApi.md#get_exchange_rate) | **GET** /currency/{from}/{to} | Get the latest currency exchange rate
*DocumentsApi* | [**cancel_review**](docs/DocumentsApi.md#cancel_review) | **DELETE** /documents/{uuid}/review | Cancel document review
*DocumentsApi* | [**delete_document**](docs/DocumentsApi.md#delete_document) | **DELETE** /documents/{uuid} | Delete a document
*DocumentsApi* | [**get_document**](docs/DocumentsApi.md#get_document) | **GET** /documents/{uuid} | Get a document
*DocumentsApi* | [**list_documents**](docs/DocumentsApi.md#list_documents) | **GET** /documents | List company&#39;s documents
*DocumentsApi* | [**process_document**](docs/DocumentsApi.md#process_document) | **GET** /documents/{uuid}/process | Process a document
*DocumentsApi* | [**review_url**](docs/DocumentsApi.md#review_url) | **GET** /documents/{uuid}/review | Get url to review a document
*DocumentsApi* | [**update_document**](docs/DocumentsApi.md#update_document) | **PUT** /documents/{uuid} | Update a document
*DocumentsApi* | [**upload_document**](docs/DocumentsApi.md#upload_document) | **POST** /documents | Upload a document
*DocumentsApi* | [**view_document**](docs/DocumentsApi.md#view_document) | **GET** /documents/{uuid}/view | View a document
*ExpenseReportsApi* | [**add_expense_report**](docs/ExpenseReportsApi.md#add_expense_report) | **POST** /expenses/expense-reports | Add an expense report
*ExpenseReportsApi* | [**delete_expense_report**](docs/ExpenseReportsApi.md#delete_expense_report) | **DELETE** /expenses/expense-reports/{uuid} | Delete an expense report
*ExpenseReportsApi* | [**expense_report_o_auth_login**](docs/ExpenseReportsApi.md#expense_report_o_auth_login) | **GET** /expenses/expense-reports/login/{method} | OAuth Login
*ExpenseReportsApi* | [**get_expense_report**](docs/ExpenseReportsApi.md#get_expense_report) | **GET** /expenses/expense-reports/{uuid} | Get an expense report
*ExpenseReportsApi* | [**get_expense_report_account**](docs/ExpenseReportsApi.md#get_expense_report_account) | **GET** /expenses/expense-reports/me | Get the currently connected expense report user details
*ExpenseReportsApi* | [**get_expense_report_user**](docs/ExpenseReportsApi.md#get_expense_report_user) | **GET** /expenses/expense-reports/users/{uuid} | Get an user details
*ExpenseReportsApi* | [**list_expense_reports**](docs/ExpenseReportsApi.md#list_expense_reports) | **GET** /expenses/expense-reports | List company&#39;s expense reports.
*ExpenseReportsApi* | [**send_expense_report_login_email**](docs/ExpenseReportsApi.md#send_expense_report_login_email) | **POST** /expenses/expense-reports/login | Request login email
*ExpenseReportsApi* | [**update_expense_report**](docs/ExpenseReportsApi.md#update_expense_report) | **PUT** /expenses/expense-reports/{uuid} | Update an expense report
*ExpenseReportsApi* | [**update_expense_report_account**](docs/ExpenseReportsApi.md#update_expense_report_account) | **PUT** /expenses/expense-reports/me | Update the currently connected expense report user
*ExpenseReportsApi* | [**update_expense_report_settings**](docs/ExpenseReportsApi.md#update_expense_report_settings) | **POST** /expenses/expense-reports/settings | Retrieve company settings for expense reports
*ExpenseReportsApi* | [**verify_expense_report_settings**](docs/ExpenseReportsApi.md#verify_expense_report_settings) | **POST** /expenses/expense-reports/verify | Verify expense reports settings
*ExportApi* | [**list_exports**](docs/ExportApi.md#list_exports) | **GET** /export | List company&#39;s exports
*ExportApi* | [**request_export**](docs/ExportApi.md#request_export) | **POST** /export | Request an export
*InvoicesApi* | [**add_invoice**](docs/InvoicesApi.md#add_invoice) | **POST** /incomes/invoices | Add an invoice
*InvoicesApi* | [**add_invoice_payment**](docs/InvoicesApi.md#add_invoice_payment) | **POST** /incomes/invoices/{uuid}/payments | Add an invoice payment
*InvoicesApi* | [**delete_invoice**](docs/InvoicesApi.md#delete_invoice) | **DELETE** /incomes/invoices/{uuid} | Delete an invoice
*InvoicesApi* | [**get_invoice**](docs/InvoicesApi.md#get_invoice) | **GET** /incomes/invoices/{uuid} | Get an invoice
*InvoicesApi* | [**get_invoice_document**](docs/InvoicesApi.md#get_invoice_document) | **GET** /incomes/invoices/{uuid}/document | Get an invoice in PDF
*InvoicesApi* | [**list_invoices**](docs/InvoicesApi.md#list_invoices) | **GET** /incomes/invoices | List company&#39;s invoices
*InvoicesApi* | [**list_unpaid_invoices**](docs/InvoicesApi.md#list_unpaid_invoices) | **GET** /incomes/invoices/unpaid | List company&#39;s unpaid invoices
*InvoicesApi* | [**update_invoice**](docs/InvoicesApi.md#update_invoice) | **PUT** /incomes/invoices/{uuid} | Update an invoice
*InvoicesApi* | [**update_invoice_payment**](docs/InvoicesApi.md#update_invoice_payment) | **PUT** /incomes/invoices/{uuid}/payments/{payment} | Update an invoice payment
*LogsApi* | [**logs**](docs/LogsApi.md#logs) | **GET** /logs | List company&#39;s logs
*NotificationApi* | [**list_notification_preferences**](docs/NotificationApi.md#list_notification_preferences) | **GET** /notifications/preferences/{notification} | List notification preferences
*NotificationApi* | [**list_notifications**](docs/NotificationApi.md#list_notifications) | **GET** /notifications | List company&#39;s notifications
*NotificationApi* | [**send_notification**](docs/NotificationApi.md#send_notification) | **POST** /notifications/send | Send a notification
*NotificationApi* | [**update_notification_preferences**](docs/NotificationApi.md#update_notification_preferences) | **PUT** /notifications/preferences/{notification} | Update notification preferences
*NotificationTypesApi* | [**add_notification_type**](docs/NotificationTypesApi.md#add_notification_type) | **POST** /notifications/types | Add a notification type
*NotificationTypesApi* | [**delete_notification_type**](docs/NotificationTypesApi.md#delete_notification_type) | **DELETE** /notifications/types/{uuid} | Delete a notification type
*NotificationTypesApi* | [**get_notification_type**](docs/NotificationTypesApi.md#get_notification_type) | **GET** /notifications/types/{uuid} | Get a notification type
*NotificationTypesApi* | [**list_notification_types**](docs/NotificationTypesApi.md#list_notification_types) | **GET** /notifications/types | List company&#39;s notification types
*NotificationTypesApi* | [**update_notification_type**](docs/NotificationTypesApi.md#update_notification_type) | **PUT** /notifications/types/{uuid} | Update a notification type
*OAuthConfigApi* | [**add_o_auth_configuration**](docs/OAuthConfigApi.md#add_o_auth_configuration) | **POST** /oauth | Add an OAuth configuration
*OAuthConfigApi* | [**delete_o_auth_configuration**](docs/OAuthConfigApi.md#delete_o_auth_configuration) | **DELETE** /oauth/{uuid} | Delete an oauth configuration
*OAuthConfigApi* | [**get_o_auth_configuration**](docs/OAuthConfigApi.md#get_o_auth_configuration) | **GET** /oauth/{uuid} | Get an OAuth configuration
*OAuthConfigApi* | [**list_o_auth_configurations**](docs/OAuthConfigApi.md#list_o_auth_configurations) | **GET** /oauth | List company&#39;s oauth configurations
*OAuthConfigApi* | [**list_providers**](docs/OAuthConfigApi.md#list_providers) | **GET** /oauth/providers | List available providers
*OAuthConfigApi* | [**update_o_auth_configuration**](docs/OAuthConfigApi.md#update_o_auth_configuration) | **PUT** /oauth/{uuid} | Update an oauth configuration
*PaymentsApi* | [**add_payment**](docs/PaymentsApi.md#add_payment) | **POST** /expenses/payments | Add a payment
*PaymentsApi* | [**delete_payment**](docs/PaymentsApi.md#delete_payment) | **DELETE** /expenses/payments/{uuid} | Delete a payment
*PaymentsApi* | [**get_payment**](docs/PaymentsApi.md#get_payment) | **GET** /expenses/payments/{uuid} | Get a payment
*PaymentsApi* | [**list_payments**](docs/PaymentsApi.md#list_payments) | **GET** /expenses/payments | List company&#39;s payments
*PaymentsApi* | [**update_payment**](docs/PaymentsApi.md#update_payment) | **PUT** /expenses/payments/{uuid} | Update a payment
*QuotesApi* | [**add_quote**](docs/QuotesApi.md#add_quote) | **POST** /quotes | Add a quote
*QuotesApi* | [**delete_quote**](docs/QuotesApi.md#delete_quote) | **DELETE** /quotes/{uuid} | Delete a quote
*QuotesApi* | [**get_quote**](docs/QuotesApi.md#get_quote) | **GET** /quotes/{uuid} | Get a quote
*QuotesApi* | [**get_quote_document**](docs/QuotesApi.md#get_quote_document) | **GET** /quotes/{uuid}/document | Get a quote in PDF
*QuotesApi* | [**list_quotes**](docs/QuotesApi.md#list_quotes) | **GET** /quotes | List company&#39;s quotes
*QuotesApi* | [**update_quote**](docs/QuotesApi.md#update_quote) | **PUT** /quotes/{uuid} | Update a quote
*ReceiptsApi* | [**add_receipt**](docs/ReceiptsApi.md#add_receipt) | **POST** /receipts | Add a receipt
*ReceiptsApi* | [**delete_receipt**](docs/ReceiptsApi.md#delete_receipt) | **DELETE** /receipts/{uuid} | Delete a receipt
*ReceiptsApi* | [**get_receipt**](docs/ReceiptsApi.md#get_receipt) | **GET** /receipts/{uuid} | Get a receipt
*ReceiptsApi* | [**get_receipt_document**](docs/ReceiptsApi.md#get_receipt_document) | **GET** /receipts/{uuid}/document | Get a receipt in PDF
*ReceiptsApi* | [**list_receipts**](docs/ReceiptsApi.md#list_receipts) | **GET** /receipts | List company&#39;s receipts
*ReceiptsApi* | [**update_receipt**](docs/ReceiptsApi.md#update_receipt) | **PUT** /receipts/{uuid} | Update a receipt
*RevenuesApi* | [**add_revenue**](docs/RevenuesApi.md#add_revenue) | **POST** /incomes/revenues | Add a revenue
*RevenuesApi* | [**delete_revenue**](docs/RevenuesApi.md#delete_revenue) | **DELETE** /incomes/revenues/{uuid} | Delete a revenue
*RevenuesApi* | [**get_revenue**](docs/RevenuesApi.md#get_revenue) | **GET** /incomes/revenues/{uuid} | Get a revenue
*RevenuesApi* | [**list_revenues**](docs/RevenuesApi.md#list_revenues) | **GET** /incomes/revenues | List company&#39;s revenues
*RevenuesApi* | [**update_revenue**](docs/RevenuesApi.md#update_revenue) | **PUT** /incomes/revenues/{uuid} | Update a revenue
*RossumApi* | [**list_reviews**](docs/RossumApi.md#list_reviews) | **GET** /external/rossum/reviews | List documents to be reviewed
*SearchApi* | [**search**](docs/SearchApi.md#search) | **GET** /search | Search
*SettingsApi* | [**get_settings**](docs/SettingsApi.md#get_settings) | **GET** /companies/{uuid}/settings/{key} | Get a company&#39;s settings
*SettingsApi* | [**list_settings**](docs/SettingsApi.md#list_settings) | **GET** /companies/{uuid}/settings | List company&#39;s settings
*SettingsApi* | [**update_settings**](docs/SettingsApi.md#update_settings) | **PUT** /companies/{uuid}/settings/{key} | Update a company&#39;s settings
*TagsApi* | [**add_tag**](docs/TagsApi.md#add_tag) | **POST** /tags | Add a tag
*TagsApi* | [**delete_tag**](docs/TagsApi.md#delete_tag) | **DELETE** /tags/{uuid} | Delete a tag
*TagsApi* | [**get_tag**](docs/TagsApi.md#get_tag) | **GET** /tags/{uuid} | Get a tag
*TagsApi* | [**list_tags**](docs/TagsApi.md#list_tags) | **GET** /tags | List company&#39;s tags
*TagsApi* | [**list_tags_by_resource**](docs/TagsApi.md#list_tags_by_resource) | **GET** /tags/attachments/{resource} | List company&#39;s tags by resource attachment
*TagsApi* | [**update_tag**](docs/TagsApi.md#update_tag) | **PUT** /tags/{uuid} | Update a tag
*TaxApi* | [**get_tax_rate**](docs/TaxApi.md#get_tax_rate) | **GET** /tax/{country} | Get the latest tax rate for a country
*TaxApi* | [**verify_vat_id**](docs/TaxApi.md#verify_vat_id) | **GET** /vat/verify/{number} | Verify a VAT ID
*TransactionsApi* | [**add_link**](docs/TransactionsApi.md#add_link) | **POST** /transactions/{uuid}/links | Add a new transaction link
*TransactionsApi* | [**add_transaction**](docs/TransactionsApi.md#add_transaction) | **POST** /transactions | Add a transaction
*TransactionsApi* | [**add_transaction_code**](docs/TransactionsApi.md#add_transaction_code) | **POST** /transactions/{uuid}/codes | Add a transaction&#39;s code
*TransactionsApi* | [**delete_link**](docs/TransactionsApi.md#delete_link) | **DELETE** /transactions/{uuid}/links/{link_uuid} | Delete a transaction link
*TransactionsApi* | [**delete_transaction**](docs/TransactionsApi.md#delete_transaction) | **DELETE** /transactions/{uuid} | Delete a transaction
*TransactionsApi* | [**delete_transaction_code**](docs/TransactionsApi.md#delete_transaction_code) | **DELETE** /transactions/{uuid}/codes/{code} | Delete a transaction&#39;s code
*TransactionsApi* | [**get_transaction**](docs/TransactionsApi.md#get_transaction) | **GET** /transactions/{uuid} | Get a transaction
*TransactionsApi* | [**import_transactions**](docs/TransactionsApi.md#import_transactions) | **POST** /transactions/import | Import transactions - INTERNAL
*TransactionsApi* | [**ledger**](docs/TransactionsApi.md#ledger) | **GET** /transactions/ledger | List company&#39;s transactions and transfers
*TransactionsApi* | [**list_links**](docs/TransactionsApi.md#list_links) | **GET** /transactions/{uuid}/links | List a transaction links
*TransactionsApi* | [**list_transaction_codes**](docs/TransactionsApi.md#list_transaction_codes) | **GET** /transactions/{uuid}/codes | List transaction&#39;s codes
*TransactionsApi* | [**list_transactions**](docs/TransactionsApi.md#list_transactions) | **GET** /transactions | List company&#39;s transactions
*TransactionsApi* | [**update_link**](docs/TransactionsApi.md#update_link) | **PUT** /transactions/{uuid}/links/{link_uuid} | Update a transaction link
*TransactionsApi* | [**update_transaction**](docs/TransactionsApi.md#update_transaction) | **PUT** /transactions/{uuid} | Update a transaction
*TransactionsApi* | [**update_transaction_code**](docs/TransactionsApi.md#update_transaction_code) | **PUT** /transactions/{uuid}/codes | Update a transaction&#39;s code
*TransactionsApi* | [**view_link**](docs/TransactionsApi.md#view_link) | **GET** /transactions/{uuid}/links/{link_uuid} | View a transaction link
*TransfersApi* | [**add_transfer**](docs/TransfersApi.md#add_transfer) | **POST** /transfers | Add a transfer
*TransfersApi* | [**delete_transfer**](docs/TransfersApi.md#delete_transfer) | **DELETE** /transfers/{uuid} | Delete a transfer
*TransfersApi* | [**get_transfer**](docs/TransfersApi.md#get_transfer) | **GET** /transfers/{uuid} | Get a transfer
*TransfersApi* | [**list_transfers**](docs/TransfersApi.md#list_transfers) | **GET** /transfers | List company&#39;s transfers
*TransfersApi* | [**update_transfer**](docs/TransfersApi.md#update_transfer) | **PUT** /transfers/{uuid} | Update a transfer
*UsersApi* | [**add_user**](docs/UsersApi.md#add_user) | **POST** /users | Add user
*UsersApi* | [**delete_user**](docs/UsersApi.md#delete_user) | **DELETE** /users/{uuid} | Delete user
*UsersApi* | [**get_user**](docs/UsersApi.md#get_user) | **GET** /users/{uuid} | View user
*UsersApi* | [**list_users**](docs/UsersApi.md#list_users) | **GET** /users | List company&#39;s users
*UsersApi* | [**update_user**](docs/UsersApi.md#update_user) | **PUT** /users/{uuid} | Update user
*UsersApi* | [**users_companies**](docs/UsersApi.md#users_companies) | **GET** /users/me/companies | List current user companies
*UsersApi* | [**users_me**](docs/UsersApi.md#users_me) | **GET** /users/me | View current user details
*VATIDApi* | [**add_company_vat_id**](docs/VATIDApi.md#add_company_vat_id) | **POST** /companies/{uuid}/vat | Add a company&#39;s Vat Id
*VATIDApi* | [**delete_company_vat_id**](docs/VATIDApi.md#delete_company_vat_id) | **DELETE** /companies/{uuid}/vat/{key} | Delete a company&#39;s Vat Id
*VATIDApi* | [**get_company_vat_id**](docs/VATIDApi.md#get_company_vat_id) | **GET** /companies/{uuid}/vat/{key} | Get a company&#39;s Vat Id
*VATIDApi* | [**list_company_vat_id**](docs/VATIDApi.md#list_company_vat_id) | **GET** /companies/{uuid}/vat | List company&#39;s Vat Id
*VATIDApi* | [**update_company_vat_id**](docs/VATIDApi.md#update_company_vat_id) | **PUT** /companies/{uuid}/vat/{key} | Update a company&#39;s Vat Id
*WebhooksApi* | [**add_webhook**](docs/WebhooksApi.md#add_webhook) | **POST** /webhooks | Add a webhook
*WebhooksApi* | [**delete_webhook**](docs/WebhooksApi.md#delete_webhook) | **DELETE** /webhooks/{uuid} | Delete a webhook
*WebhooksApi* | [**get_webhook**](docs/WebhooksApi.md#get_webhook) | **GET** /webhooks/{uuid} | Get a webhook
*WebhooksApi* | [**get_webhook_history**](docs/WebhooksApi.md#get_webhook_history) | **GET** /webhooks/{uuid}/history | Get webhook&#39;s history
*WebhooksApi* | [**list_webhook_events**](docs/WebhooksApi.md#list_webhook_events) | **GET** /webhooks/events | List available webhook events
*WebhooksApi* | [**list_webhooks**](docs/WebhooksApi.md#list_webhooks) | **GET** /webhooks | List company&#39;s webhooks
*WebhooksApi* | [**update_webhook**](docs/WebhooksApi.md#update_webhook) | **PUT** /webhooks/{uuid} | Update a webhook


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="bearer"></a>
### bearer

- **Type**: Bearer authentication (Api Key)

<a id="cookie"></a>
### cookie

- **Type**: API key
- **API key parameter name**: accounting_auth
- **Location**: 



