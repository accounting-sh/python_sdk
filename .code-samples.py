# ..delete_account_connection
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The account uuid
connection = "connection_example"  # str | The connection uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete an account's connection
    api_response = accounting.account_connections_api.delete_account_connection(
        uuid, connection
    )
    print("The response of AccountConnectionsApi->delete_account_connection:\n")
    pprint(api_response)
except ApiException as e:
    print(
        "Exception when calling AccountConnectionsApi->delete_account_connection: %s\n"
        % e
    )


# ..import_account_transactions
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The account UUID

accounting = accounting_sh.Accounting("access_token")
try:
    # Import all available bank transaction history asynchronously
    api_response = accounting.account_connections_api.import_account_transactions(uuid)
    print("The response of AccountConnectionsApi->import_account_transactions:\n")
    pprint(api_response)
except ApiException as e:
    print(
        "Exception when calling AccountConnectionsApi->import_account_transactions: %s\n"
        % e
    )


# ..list_account_connections
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The account uuid
fields = "fields_example"  # str | A comma separated list of fields requested in the response (optional)
page = "page_example"  # str | The response page (optional)
per_page = "per_page_example"  # str | The number of items per page (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List account's connections
    api_response = accounting.account_connections_api.list_account_connections(
        uuid, fields=fields, page=page, per_page=per_page
    )
    print("The response of AccountConnectionsApi->list_account_connections:\n")
    pprint(api_response)
except ApiException as e:
    print(
        "Exception when calling AccountConnectionsApi->list_account_connections: %s\n"
        % e
    )


# ..list_banks
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The account uuid
country = "country_example"  # str | A two letter country code, if none are specified, the company's country is used (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List available bank connections
    api_response = accounting.account_connections_api.list_banks(uuid, country=country)
    print("The response of AccountConnectionsApi->list_banks:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountConnectionsApi->list_banks: %s\n" % e)


# ..list_connectable_bank_accounts
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The account uuid
connection = "connection_example"  # str | The connection request UUID (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List connectable bank accounts
    api_response = accounting.account_connections_api.list_connectable_bank_accounts(
        uuid, connection=connection
    )
    print("The response of AccountConnectionsApi->list_connectable_bank_accounts:\n")
    pprint(api_response)
except ApiException as e:
    print(
        "Exception when calling AccountConnectionsApi->list_connectable_bank_accounts: %s\n"
        % e
    )


# ..list_connected_account_transactions
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The account uuid
connection = "connection_example"  # str | The connection uuid
period = 3.4  # float | The number of days to look back for transactions. Default is 7 days. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List the connected account's transactions
    api_response = (
        accounting.account_connections_api.list_connected_account_transactions(
            uuid, connection, period=period
        )
    )
    print(
        "The response of AccountConnectionsApi->list_connected_account_transactions:\n"
    )
    pprint(api_response)
except ApiException as e:
    print(
        "Exception when calling AccountConnectionsApi->list_connected_account_transactions: %s\n"
        % e
    )


# ..request_bank_connection
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The account uuid
request_bank_connection_request = (
    accounting_sh.RequestBankConnectionRequest()
)  # RequestBankConnectionRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Request a new bank connection
    api_response = accounting.account_connections_api.request_bank_connection(
        uuid, request_bank_connection_request
    )
    print("The response of AccountConnectionsApi->request_bank_connection:\n")
    pprint(api_response)
except ApiException as e:
    print(
        "Exception when calling AccountConnectionsApi->request_bank_connection: %s\n"
        % e
    )


# ..select_bank_account
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The account uuid
select_bank_account_request = (
    accounting_sh.SelectBankAccountRequest()
)  # SelectBankAccountRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Select a bank account to connect
    api_response = accounting.account_connections_api.select_bank_account(
        uuid, select_bank_account_request
    )
    print("The response of AccountConnectionsApi->select_bank_account:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountConnectionsApi->select_bank_account: %s\n" % e)


# ..add_accounting_code
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_accounting_code_request = (
    accounting_sh.AddAccountingCodeRequest()
)  # AddAccountingCodeRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Add an accounting code
    api_response = accounting.accounting_codes_api.add_accounting_code(
        add_accounting_code_request
    )
    print("The response of AccountingCodesApi->add_accounting_code:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingCodesApi->add_accounting_code: %s\n" % e)


# ..delete_accounting_code
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The accounting code uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete an accounting code
    api_response = accounting.accounting_codes_api.delete_accounting_code(uuid)
    print("The response of AccountingCodesApi->delete_accounting_code:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingCodesApi->delete_accounting_code: %s\n" % e)


# ..get_accounting_code
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The accounting code uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get an accounting code
    api_response = accounting.accounting_codes_api.get_accounting_code(uuid)
    print("The response of AccountingCodesApi->get_accounting_code:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingCodesApi->get_accounting_code: %s\n" % e)


# ..list_accounting_codes
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's accounting code
    api_response = accounting.accounting_codes_api.list_accounting_codes()
    print("The response of AccountingCodesApi->list_accounting_codes:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingCodesApi->list_accounting_codes: %s\n" % e)


# ..update_accounting_code
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The accounting code uuid
add_accounting_code_request = (
    accounting_sh.AddAccountingCodeRequest()
)  # AddAccountingCodeRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update an accounting code
    api_response = accounting.accounting_codes_api.update_accounting_code(
        uuid, add_accounting_code_request
    )
    print("The response of AccountingCodesApi->update_accounting_code:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingCodesApi->update_accounting_code: %s\n" % e)


# ..add_account
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_account_request = (
    accounting_sh.AddAccountRequest()
)  # AddAccountRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Add an account
    api_response = accounting.accounts_api.add_account(add_account_request)
    print("The response of AccountsApi->add_account:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->add_account: %s\n" % e)


# ..delete_account
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The account uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete an account
    api_response = accounting.accounts_api.delete_account(uuid)
    print("The response of AccountsApi->delete_account:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->delete_account: %s\n" % e)


# ..get_account
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The account uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get an account
    api_response = accounting.accounts_api.get_account(uuid)
    print("The response of AccountsApi->get_account:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_account: %s\n" % e)


# ..list_accounts
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = "uuid,name,bank,currency,journal_number"  # str | Comma-separated fields to include in each record. Default fields: uuid, name, bank, currency, journal_number. (optional)
page = 1  # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10  # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = "created_at:desc"  # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's accounts
    api_response = accounting.accounts_api.list_accounts(
        fields=fields, page=page, per_page=per_page, order_by=order_by
    )
    print("The response of AccountsApi->list_accounts:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->list_accounts: %s\n" % e)


# ..update_account
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The account uuid
add_account_request = (
    accounting_sh.AddAccountRequest()
)  # AddAccountRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update an account
    api_response = accounting.accounts_api.update_account(uuid, add_account_request)
    print("The response of AccountsApi->update_account:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->update_account: %s\n" % e)


# ..add_attachment
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_attachment_request = (
    accounting_sh.AddAttachmentRequest()
)  # AddAttachmentRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Add an attachment
    api_response = accounting.attachments_api.add_attachment(add_attachment_request)
    print("The response of AttachmentsApi->add_attachment:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentsApi->add_attachment: %s\n" % e)


# ..delete_attachment
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The attachment uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete an attachment
    api_response = accounting.attachments_api.delete_attachment(uuid)
    print("The response of AttachmentsApi->delete_attachment:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentsApi->delete_attachment: %s\n" % e)


# ..get_attachment
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The attachment uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get an attachment
    api_response = accounting.attachments_api.get_attachment(uuid)
    print("The response of AttachmentsApi->get_attachment:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentsApi->get_attachment: %s\n" % e)


# ..list_attachments
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = "uuid,document,attached_to"  # str | Comma-separated fields to include in each record. Default fields: uuid, document, attached_to. (optional)
page = 1  # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10  # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = "created_at:desc"  # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's attachments
    api_response = accounting.attachments_api.list_attachments(
        fields=fields, page=page, per_page=per_page, order_by=order_by
    )
    print("The response of AttachmentsApi->list_attachments:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentsApi->list_attachments: %s\n" % e)


# ..retrieve_attachments
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

resource = "resource_example"  # str | The resource
fields = "uuid,document,attached_to"  # str | Comma-separated fields to include in each record. Default fields: uuid, document, attached_to. (optional)
page = 1  # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10  # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = "created_at:desc"  # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's attachments link to resource
    api_response = accounting.attachments_api.retrieve_attachments(
        resource, fields=fields, page=page, per_page=per_page, order_by=order_by
    )
    print("The response of AttachmentsApi->retrieve_attachments:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentsApi->retrieve_attachments: %s\n" % e)


# ..update_attachment
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The attachment uuid
add_attachment_request = (
    accounting_sh.AddAttachmentRequest()
)  # AddAttachmentRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update an attachment
    api_response = accounting.attachments_api.update_attachment(
        uuid, add_attachment_request
    )
    print("The response of AttachmentsApi->update_attachment:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentsApi->update_attachment: %s\n" % e)


# ..auth_init
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

accounting = accounting_sh.Accounting("access_token")
try:
    # Init authentication process
    api_response = accounting.auth_api.auth_init()
    print("The response of AuthApi->auth_init:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_init: %s\n" % e)


# ..login
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

login_get_alias_request = (
    accounting_sh.LoginGetAliasRequest()
)  # LoginGetAliasRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Login user
    api_response = accounting.auth_api.login(login_get_alias_request)
    print("The response of AuthApi->login:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->login: %s\n" % e)


# ..login_get_alias
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

login_get_alias_request = (
    accounting_sh.LoginGetAliasRequest()
)  # LoginGetAliasRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Login user
    api_response = accounting.auth_api.login_get_alias(login_get_alias_request)
    print("The response of AuthApi->login_get_alias:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->login_get_alias: %s\n" % e)


# ..logout
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

accounting = accounting_sh.Accounting("access_token")
try:
    # Logout current user
    api_response = accounting.auth_api.logout()
    print("The response of AuthApi->logout:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->logout: %s\n" % e)


# ..switch_company
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

switch_company_request = (
    accounting_sh.SwitchCompanyRequest()
)  # SwitchCompanyRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Switch to a different company
    api_response = accounting.auth_api.switch_company(switch_company_request)
    print("The response of AuthApi->switch_company:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->switch_company: %s\n" % e)


# ..add_bill
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_bill_request = (
    accounting_sh.AddBillRequest()
)  # AddBillRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Add a bill
    api_response = accounting.bills_api.add_bill(add_bill_request)
    print("The response of BillsApi->add_bill:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillsApi->add_bill: %s\n" % e)


# ..add_bill_payment
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The bill uuid
add_bill_payment_request = (
    accounting_sh.AddBillPaymentRequest()
)  # AddBillPaymentRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Add a bill payment
    api_response = accounting.bills_api.add_bill_payment(uuid, add_bill_payment_request)
    print("The response of BillsApi->add_bill_payment:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillsApi->add_bill_payment: %s\n" % e)


# ..delete_bill
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The bill uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete a bill
    api_response = accounting.bills_api.delete_bill(uuid)
    print("The response of BillsApi->delete_bill:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillsApi->delete_bill: %s\n" % e)


# ..get_bill
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The bill uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a bill
    api_response = accounting.bills_api.get_bill(uuid)
    print("The response of BillsApi->get_bill:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillsApi->get_bill: %s\n" % e)


# ..get_bill_document
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The invoice uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a bill in PDF
    api_response = accounting.bills_api.get_bill_document(uuid)
    print("The response of BillsApi->get_bill_document:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillsApi->get_bill_document: %s\n" % e)


# ..list_bills
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = "uuid,contact,bill_number,status"  # str | Comma-separated fields to include in each record. Default fields: uuid, contact, bill_number, status. (optional)
page = 1  # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10  # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = "created_at:desc"  # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's bills
    api_response = accounting.bills_api.list_bills(
        fields=fields, page=page, per_page=per_page, order_by=order_by
    )
    print("The response of BillsApi->list_bills:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillsApi->list_bills: %s\n" % e)


# ..update_bill
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The bill uuid
update_bill_request = (
    accounting_sh.UpdateBillRequest()
)  # UpdateBillRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a bill
    api_response = accounting.bills_api.update_bill(uuid, update_bill_request)
    print("The response of BillsApi->update_bill:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillsApi->update_bill: %s\n" % e)


# ..update_bill_payment
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The bill uuid
payment = "payment_example"  # str | The bill payment uuid
add_bill_payment_request = (
    accounting_sh.AddBillPaymentRequest()
)  # AddBillPaymentRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a bill payment
    api_response = accounting.bills_api.update_bill_payment(
        uuid, payment, add_bill_payment_request
    )
    print("The response of BillsApi->update_bill_payment:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillsApi->update_bill_payment: %s\n" % e)


# ..add_category
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_category_request = (
    accounting_sh.AddCategoryRequest()
)  # AddCategoryRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Add a category
    api_response = accounting.categories_api.add_category(add_category_request)
    print("The response of CategoriesApi->add_category:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->add_category: %s\n" % e)


# ..delete_category
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The category uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete a category
    api_response = accounting.categories_api.delete_category(uuid)
    print("The response of CategoriesApi->delete_category:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->delete_category: %s\n" % e)


# ..get_category
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The category uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a category
    api_response = accounting.categories_api.get_category(uuid)
    print("The response of CategoriesApi->get_category:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->get_category: %s\n" % e)


# ..list_categories
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = "uuid,name,type,color"  # str | Comma-separated fields to include in each record. Default fields: uuid, name, type, color. (optional)
page = 1  # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10  # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = "created_at:desc"  # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's categories
    api_response = accounting.categories_api.list_categories(
        fields=fields, page=page, per_page=per_page, order_by=order_by
    )
    print("The response of CategoriesApi->list_categories:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->list_categories: %s\n" % e)


# ..update_category
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The category uuid
add_category_request = (
    accounting_sh.AddCategoryRequest()
)  # AddCategoryRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a category
    api_response = accounting.categories_api.update_category(uuid, add_category_request)
    print("The response of CategoriesApi->update_category:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->update_category: %s\n" % e)


# ..add_company
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_company_request = (
    accounting_sh.AddCompanyRequest()
)  # AddCompanyRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Add a company (resellers only)
    api_response = accounting.companies_api.add_company(add_company_request)
    print("The response of CompaniesApi->add_company:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompaniesApi->add_company: %s\n" % e)


# ..delete_company
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The company uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete a company
    api_response = accounting.companies_api.delete_company(uuid)
    print("The response of CompaniesApi->delete_company:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompaniesApi->delete_company: %s\n" % e)


# ..get_company
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The company uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a company
    api_response = accounting.companies_api.get_company(uuid)
    print("The response of CompaniesApi->get_company:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompaniesApi->get_company: %s\n" % e)


# ..get_company_customization
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The company uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a company's customization parameters
    api_response = accounting.companies_api.get_company_customization(uuid)
    print("The response of CompaniesApi->get_company_customization:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompaniesApi->get_company_customization: %s\n" % e)


# ..get_company_feature_set
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | Identifier of the authenticated company.

accounting = accounting_sh.Accounting("access_token")
try:
    # List a company's feature set
    api_response = accounting.companies_api.get_company_feature_set(uuid)
    print("The response of CompaniesApi->get_company_feature_set:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompaniesApi->get_company_feature_set: %s\n" % e)


# ..get_company_onboarding
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The authenticated company's UUID.

accounting = accounting_sh.Accounting("access_token")
try:
    # Get company onboarding status
    api_response = accounting.companies_api.get_company_onboarding(uuid)
    print("The response of CompaniesApi->get_company_onboarding:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompaniesApi->get_company_onboarding: %s\n" % e)


# ..list_companies
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = "uuid,name,currency,prefix"  # str | Comma-separated fields to include in each record. Default fields: uuid, name, currency, prefix. (optional)
page = 1  # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10  # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = "created_at:desc"  # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List companies on this instance (resellers only)
    api_response = accounting.companies_api.list_companies(
        fields=fields, page=page, per_page=per_page, order_by=order_by
    )
    print("The response of CompaniesApi->list_companies:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompaniesApi->list_companies: %s\n" % e)


# ..update_company
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The company uuid
add_company_request = (
    accounting_sh.AddCompanyRequest()
)  # AddCompanyRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a company
    api_response = accounting.companies_api.update_company(uuid, add_company_request)
    print("The response of CompaniesApi->update_company:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompaniesApi->update_company: %s\n" % e)


# ..add_contact
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_contact_request = (
    accounting_sh.AddContactRequest()
)  # AddContactRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Create a new contact
    api_response = accounting.contacts_api.add_contact(add_contact_request)
    print("The response of ContactsApi->add_contact:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->add_contact: %s\n" % e)


# ..delete_contact
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The contact uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete a contact
    api_response = accounting.contacts_api.delete_contact(uuid)
    print("The response of ContactsApi->delete_contact:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->delete_contact: %s\n" % e)


# ..get_contact
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The contact uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Retrieve a contact
    api_response = accounting.contacts_api.get_contact(uuid)
    print("The response of ContactsApi->get_contact:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->get_contact: %s\n" % e)


# ..list_contact_bills
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The contact uuid
fields = "uuid,vendor,bill_number,status"  # str | Comma-separated fields to include in each record. Default fields: uuid, vendor, bill_number, status. (optional)
page = 1  # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10  # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = "created_at:desc"  # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List a contact's bills
    api_response = accounting.contacts_api.list_contact_bills(
        uuid, fields=fields, page=page, per_page=per_page, order_by=order_by
    )
    print("The response of ContactsApi->list_contact_bills:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->list_contact_bills: %s\n" % e)


# ..list_contact_invoices
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The contact uuid
fields = "uuid,customer,status,emitted"  # str | Comma-separated fields to include in each record. Default fields: uuid, customer, status, emitted. (optional)
page = 1  # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10  # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = "created_at:desc"  # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List a contact's invoices
    api_response = accounting.contacts_api.list_contact_invoices(
        uuid, fields=fields, page=page, per_page=per_page, order_by=order_by
    )
    print("The response of ContactsApi->list_contact_invoices:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->list_contact_invoices: %s\n" % e)


# ..list_contacts
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = "uuid,name,prefix,currency,registration_number"  # str | Comma-separated fields to include in each record. Default fields: uuid, name, prefix, currency, registration_number. Optional buyer_type is the explicit business/consumer override; null uses automatic inference. (optional)
page = 1  # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10  # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = "created_at:desc"  # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's contacts
    api_response = accounting.contacts_api.list_contacts(
        fields=fields, page=page, per_page=per_page, order_by=order_by
    )
    print("The response of ContactsApi->list_contacts:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->list_contacts: %s\n" % e)


# ..update_contact
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The contact uuid
add_contact_request = (
    accounting_sh.AddContactRequest()
)  # AddContactRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a contact
    api_response = accounting.contacts_api.update_contact(uuid, add_contact_request)
    print("The response of ContactsApi->update_contact:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->update_contact: %s\n" % e)


# ..get_translated_countries
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

lang = "lang_example"  # str | The target language

accounting = accounting_sh.Accounting("access_token")
try:
    # Get translated list of countries
    api_response = accounting.countries_api.get_translated_countries(lang)
    print("The response of CountriesApi->get_translated_countries:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountriesApi->get_translated_countries: %s\n" % e)


# ..add_credential
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_credential_request = (
    accounting_sh.AddCredentialRequest()
)  # AddCredentialRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Add a credential
    api_response = accounting.credentials_api.add_credential(add_credential_request)
    print("The response of CredentialsApi->add_credential:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->add_credential: %s\n" % e)


# ..delete_credential
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The credential uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete a credential
    api_response = accounting.credentials_api.delete_credential(uuid)
    print("The response of CredentialsApi->delete_credential:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->delete_credential: %s\n" % e)


# ..get_credential
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The credential uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a credential
    api_response = accounting.credentials_api.get_credential(uuid)
    print("The response of CredentialsApi->get_credential:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->get_credential: %s\n" % e)


# ..list_credentials
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = "uuid,permissions,expired_at"  # str | Comma-separated fields to include in each record. Default fields: uuid, permissions, expired_at. (optional)
page = 1  # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10  # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = "created_at:desc"  # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's credentials
    api_response = accounting.credentials_api.list_credentials(
        fields=fields, page=page, per_page=per_page, order_by=order_by
    )
    print("The response of CredentialsApi->list_credentials:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->list_credentials: %s\n" % e)


# ..list_permissions
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

accounting = accounting_sh.Accounting("access_token")
try:
    # List available permissions
    api_response = accounting.credentials_api.list_permissions()
    print("The response of CredentialsApi->list_permissions:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->list_permissions: %s\n" % e)


# ..me
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

accounting = accounting_sh.Accounting("access_token")
try:
    # Get current credential informations
    api_response = accounting.credentials_api.me()
    print("The response of CredentialsApi->me:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->me: %s\n" % e)


# ..update_credential
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The credential uuid
add_credential_request = (
    accounting_sh.AddCredentialRequest()
)  # AddCredentialRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a credential
    api_response = accounting.credentials_api.update_credential(
        uuid, add_credential_request
    )
    print("The response of CredentialsApi->update_credential:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->update_credential: %s\n" % e)


# ..add_credit_note
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_credit_note_request = accounting_sh.AddCreditNoteRequest()  # AddCreditNoteRequest |

accounting = accounting_sh.Accounting("access_token")
try:
    # Issue a partial credit note or credit the remaining invoice balance
    api_response = accounting.credit_notes_api.add_credit_note(add_credit_note_request)
    print("The response of CreditNotesApi->add_credit_note:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditNotesApi->add_credit_note: %s\n" % e)


# ..delete_credit_note
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str |

accounting = accounting_sh.Accounting("access_token")
try:
    # Issued credit notes cannot be deleted
    accounting.credit_notes_api.delete_credit_note(uuid)
except ApiException as e:
    print("Exception when calling CreditNotesApi->delete_credit_note: %s\n" % e)


# ..get_credit_note
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str |

accounting = accounting_sh.Accounting("access_token")
try:
    # Retrieve an issued credit note
    api_response = accounting.credit_notes_api.get_credit_note(uuid)
    print("The response of CreditNotesApi->get_credit_note:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditNotesApi->get_credit_note: %s\n" % e)


# ..get_credit_note_document
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str |

accounting = accounting_sh.Accounting("access_token")
try:
    # Download the immutable credit note PDF
    api_response = accounting.credit_notes_api.get_credit_note_document(uuid)
    print("The response of CreditNotesApi->get_credit_note_document:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditNotesApi->get_credit_note_document: %s\n" % e)


# ..list_credit_notes
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

page = 56  # int |  (optional)
per_page = 56  # int |  (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List this company's issued credit notes
    api_response = accounting.credit_notes_api.list_credit_notes(
        page=page, per_page=per_page
    )
    print("The response of CreditNotesApi->list_credit_notes:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditNotesApi->list_credit_notes: %s\n" % e)


# ..update_credit_note
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str |

accounting = accounting_sh.Accounting("access_token")
try:
    # Issued credit notes cannot be updated
    accounting.credit_notes_api.update_credit_note(uuid)
except ApiException as e:
    print("Exception when calling CreditNotesApi->update_credit_note: %s\n" % e)


# ..get_exchange_rate
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

var_from = "var_from_example"  # str | The currency to convert from
to = "to_example"  # str | The currency to convert to

accounting = accounting_sh.Accounting("access_token")
try:
    # Get the latest currency exchange rate
    api_response = accounting.currency_api.get_exchange_rate(var_from, to)
    print("The response of CurrencyApi->get_exchange_rate:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurrencyApi->get_exchange_rate: %s\n" % e)


# ..delete_document
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The document uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete a document
    api_response = accounting.documents_api.delete_document(uuid)
    print("The response of DocumentsApi->delete_document:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->delete_document: %s\n" % e)


# ..get_document
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The document uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a document
    api_response = accounting.documents_api.get_document(uuid)
    print("The response of DocumentsApi->get_document:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->get_document: %s\n" % e)


# ..list_documents
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = "uuid,name,mimetype"  # str | Comma-separated fields to include in each record. Default fields: uuid, name, mimetype. (optional)
page = 1  # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10  # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = "created_at:desc"  # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's documents
    api_response = accounting.documents_api.list_documents(
        fields=fields, page=page, per_page=per_page, order_by=order_by
    )
    print("The response of DocumentsApi->list_documents:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->list_documents: %s\n" % e)


# ..process_document
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The document uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Process a document
    api_response = accounting.documents_api.process_document(uuid)
    print("The response of DocumentsApi->process_document:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->process_document: %s\n" % e)


# ..review_document_retention
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str |
review_document_retention_request = (
    accounting_sh.ReviewDocumentRetentionRequest()
)  # ReviewDocumentRetentionRequest |

accounting = accounting_sh.Accounting("access_token")
try:
    # Review accounting retention or a legal hold
    api_response = accounting.documents_api.review_document_retention(
        uuid, review_document_retention_request
    )
    print("The response of DocumentsApi->review_document_retention:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->review_document_retention: %s\n" % e)


# ..update_document
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The document uuid
update_document_request = (
    accounting_sh.UpdateDocumentRequest()
)  # UpdateDocumentRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a document
    api_response = accounting.documents_api.update_document(
        uuid, update_document_request
    )
    print("The response of DocumentsApi->update_document:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->update_document: %s\n" % e)


# ..upload_document
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

name = "name_example"  # str | Human-readable name or label.
file = None  # bytearray | File to upload. Send this field as a file part in a multipart/form-data request.

accounting = accounting_sh.Accounting("access_token")
try:
    # Upload a document
    api_response = accounting.documents_api.upload_document(name, file)
    print("The response of DocumentsApi->upload_document:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->upload_document: %s\n" % e)


# ..view_document
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The document uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # View a document
    accounting.documents_api.view_document(uuid)
except ApiException as e:
    print("Exception when calling DocumentsApi->view_document: %s\n" % e)


# ..add_expense_report
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_expense_report_request = (
    accounting_sh.AddExpenseReportRequest()
)  # AddExpenseReportRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Add an expense report
    api_response = accounting.expense_reports_api.add_expense_report(
        add_expense_report_request
    )
    print("The response of ExpenseReportsApi->add_expense_report:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpenseReportsApi->add_expense_report: %s\n" % e)


# ..delete_expense_report
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The expense report uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete an expense report
    api_response = accounting.expense_reports_api.delete_expense_report(uuid)
    print("The response of ExpenseReportsApi->delete_expense_report:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpenseReportsApi->delete_expense_report: %s\n" % e)


# ..expense_report_o_auth_login
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

method = "method_example"  # str | The OAuth Provider to use

accounting = accounting_sh.Accounting("access_token")
try:
    # OAuth Login
    api_response = accounting.expense_reports_api.expense_report_o_auth_login(method)
    print("The response of ExpenseReportsApi->expense_report_o_auth_login:\n")
    pprint(api_response)
except ApiException as e:
    print(
        "Exception when calling ExpenseReportsApi->expense_report_o_auth_login: %s\n"
        % e
    )


# ..get_expense_report
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The expense report uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get an expense report
    api_response = accounting.expense_reports_api.get_expense_report(uuid)
    print("The response of ExpenseReportsApi->get_expense_report:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpenseReportsApi->get_expense_report: %s\n" % e)


# ..get_expense_report_account
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
    print(
        "Exception when calling ExpenseReportsApi->get_expense_report_account: %s\n" % e
    )


# ..get_expense_report_user
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The expense report user uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get an user details
    api_response = accounting.expense_reports_api.get_expense_report_user(uuid)
    print("The response of ExpenseReportsApi->get_expense_report_user:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpenseReportsApi->get_expense_report_user: %s\n" % e)


# ..list_expense_reports
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = "uuid,user,status"  # str | Comma-separated fields to include in each record. Default fields: uuid, user, status. (optional)
page = 1  # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10  # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = "created_at:desc"  # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's expense reports.
    api_response = accounting.expense_reports_api.list_expense_reports(
        fields=fields, page=page, per_page=per_page, order_by=order_by
    )
    print("The response of ExpenseReportsApi->list_expense_reports:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpenseReportsApi->list_expense_reports: %s\n" % e)


# ..send_expense_report_login_email
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

send_expense_report_login_email_request = (
    accounting_sh.SendExpenseReportLoginEmailRequest()
)  # SendExpenseReportLoginEmailRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Request login email
    api_response = accounting.expense_reports_api.send_expense_report_login_email(
        send_expense_report_login_email_request
    )
    print("The response of ExpenseReportsApi->send_expense_report_login_email:\n")
    pprint(api_response)
except ApiException as e:
    print(
        "Exception when calling ExpenseReportsApi->send_expense_report_login_email: %s\n"
        % e
    )


# ..update_expense_report
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The expense report uuid
add_expense_report_request = (
    accounting_sh.AddExpenseReportRequest()
)  # AddExpenseReportRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update an expense report
    api_response = accounting.expense_reports_api.update_expense_report(
        uuid, add_expense_report_request
    )
    print("The response of ExpenseReportsApi->update_expense_report:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpenseReportsApi->update_expense_report: %s\n" % e)


# ..update_expense_report_account
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

update_expense_report_account_request = (
    accounting_sh.UpdateExpenseReportAccountRequest()
)  # UpdateExpenseReportAccountRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update the currently connected expense report user
    api_response = accounting.expense_reports_api.update_expense_report_account(
        update_expense_report_account_request
    )
    print("The response of ExpenseReportsApi->update_expense_report_account:\n")
    pprint(api_response)
except ApiException as e:
    print(
        "Exception when calling ExpenseReportsApi->update_expense_report_account: %s\n"
        % e
    )


# ..update_expense_report_settings
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

update_expense_report_settings_request = (
    accounting_sh.UpdateExpenseReportSettingsRequest()
)  # UpdateExpenseReportSettingsRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Retrieve company settings for expense reports
    api_response = accounting.expense_reports_api.update_expense_report_settings(
        update_expense_report_settings_request
    )
    print("The response of ExpenseReportsApi->update_expense_report_settings:\n")
    pprint(api_response)
except ApiException as e:
    print(
        "Exception when calling ExpenseReportsApi->update_expense_report_settings: %s\n"
        % e
    )


# ..verify_expense_report_settings
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

verify_expense_report_settings_request = (
    accounting_sh.VerifyExpenseReportSettingsRequest()
)  # VerifyExpenseReportSettingsRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Verify expense reports settings
    api_response = accounting.expense_reports_api.verify_expense_report_settings(
        verify_expense_report_settings_request
    )
    print("The response of ExpenseReportsApi->verify_expense_report_settings:\n")
    pprint(api_response)
except ApiException as e:
    print(
        "Exception when calling ExpenseReportsApi->verify_expense_report_settings: %s\n"
        % e
    )


# ..list_exports
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = "uuid,status,document,created_at,updated_at"  # str | Comma-separated fields to include in each record. Default fields: uuid, status, document, created_at, updated_at. (optional)
page = 1  # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10  # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = "created_at:desc"  # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's exports
    api_response = accounting.export_api.list_exports(
        fields=fields, page=page, per_page=per_page, order_by=order_by
    )
    print("The response of ExportApi->list_exports:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportApi->list_exports: %s\n" % e)


# ..request_export
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

request_export_request = (
    accounting_sh.RequestExportRequest()
)  # RequestExportRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Request an export
    api_response = accounting.export_api.request_export(request_export_request)
    print("The response of ExportApi->request_export:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportApi->request_export: %s\n" % e)


# ..add_invoice
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_invoice_request = (
    accounting_sh.AddInvoiceRequest()
)  # AddInvoiceRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Add an invoice
    api_response = accounting.invoices_api.add_invoice(add_invoice_request)
    print("The response of InvoicesApi->add_invoice:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->add_invoice: %s\n" % e)


# ..add_invoice_payment
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The invoice uuid
add_bill_payment_request = (
    accounting_sh.AddBillPaymentRequest()
)  # AddBillPaymentRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Add an invoice payment
    api_response = accounting.invoices_api.add_invoice_payment(
        uuid, add_bill_payment_request
    )
    print("The response of InvoicesApi->add_invoice_payment:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->add_invoice_payment: %s\n" % e)


# ..delete_invoice
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The invoice uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete an invoice
    api_response = accounting.invoices_api.delete_invoice(uuid)
    print("The response of InvoicesApi->delete_invoice:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->delete_invoice: %s\n" % e)


# ..get_invoice
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The invoice uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get an invoice
    api_response = accounting.invoices_api.get_invoice(uuid)
    print("The response of InvoicesApi->get_invoice:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_invoice: %s\n" % e)


# ..get_invoice_document
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The invoice uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get an invoice in PDF
    api_response = accounting.invoices_api.get_invoice_document(uuid)
    print("The response of InvoicesApi->get_invoice_document:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_invoice_document: %s\n" % e)


# ..get_invoice_issuance
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str |

accounting = accounting_sh.Accounting("access_token")
try:
    # Retrieve the immutable source snapshot and original document fingerprints
    api_response = accounting.invoices_api.get_invoice_issuance(uuid)
    print("The response of InvoicesApi->get_invoice_issuance:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_invoice_issuance: %s\n" % e)


# ..list_invoices
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = "uuid,contact,status,emitted"  # str | Comma-separated fields to include in each record. Default fields: uuid, contact, status, emitted. (optional)
page = 1  # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10  # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = "created_at:desc"  # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's invoices
    api_response = accounting.invoices_api.list_invoices(
        fields=fields, page=page, per_page=per_page, order_by=order_by
    )
    print("The response of InvoicesApi->list_invoices:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->list_invoices: %s\n" % e)


# ..list_unpaid_invoices
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's unpaid invoices
    api_response = accounting.invoices_api.list_unpaid_invoices()
    print("The response of InvoicesApi->list_unpaid_invoices:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->list_unpaid_invoices: %s\n" % e)


# ..update_invoice
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The invoice uuid
update_invoice_request = (
    accounting_sh.UpdateInvoiceRequest()
)  # UpdateInvoiceRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update an invoice
    api_response = accounting.invoices_api.update_invoice(uuid, update_invoice_request)
    print("The response of InvoicesApi->update_invoice:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->update_invoice: %s\n" % e)


# ..update_invoice_payment
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The invoice uuid
payment = "payment_example"  # str | The invoice payment uuid
add_bill_payment_request = (
    accounting_sh.AddBillPaymentRequest()
)  # AddBillPaymentRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update an invoice payment
    api_response = accounting.invoices_api.update_invoice_payment(
        uuid, payment, add_bill_payment_request
    )
    print("The response of InvoicesApi->update_invoice_payment:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->update_invoice_payment: %s\n" % e)


# ..journal_balances
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

var_from = "2013-10-20"  # date |  (optional)
to = "2013-10-20"  # date |  (optional)
code = "code_example"  # str |  (optional)
contact = "contact_example"  # str |  (optional)
journal = "journal_example"  # str |  (optional)
period = "period_example"  # str |  (optional)
bank_account = "bank_account_example"  # str |  (optional)
group_by_contact = True  # bool |  (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # Account balances
    api_response = accounting.journal_api.journal_balances(
        var_from=var_from,
        to=to,
        code=code,
        contact=contact,
        journal=journal,
        period=period,
        bank_account=bank_account,
        group_by_contact=group_by_contact,
    )
    print("The response of JournalApi->journal_balances:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_balances: %s\n" % e)


# ..journal_balancesheet
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

var_from = "2013-10-20"  # date |  (optional)
to = "2013-10-20"  # date |  (optional)
code = "code_example"  # str |  (optional)
contact = "contact_example"  # str |  (optional)
journal = "journal_example"  # str |  (optional)
period = "period_example"  # str |  (optional)
bank_account = "bank_account_example"  # str |  (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # Balance sheet
    api_response = accounting.journal_api.journal_balancesheet(
        var_from=var_from,
        to=to,
        code=code,
        contact=contact,
        journal=journal,
        period=period,
        bank_account=bank_account,
    )
    print("The response of JournalApi->journal_balancesheet:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_balancesheet: %s\n" % e)


# ..journal_correction_add
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

journal_correction_add_request = (
    accounting_sh.JournalCorrectionAddRequest()
)  # JournalCorrectionAddRequest |

accounting = accounting_sh.Accounting("access_token")
try:
    # Add correction
    api_response = accounting.journal_api.journal_correction_add(
        journal_correction_add_request
    )
    print("The response of JournalApi->journal_correction_add:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_correction_add: %s\n" % e)


# ..journal_correction_delete
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str |

accounting = accounting_sh.Accounting("access_token")
try:
    # Reject changes to immutable correction
    accounting.journal_api.journal_correction_delete(uuid)
except ApiException as e:
    print("Exception when calling JournalApi->journal_correction_delete: %s\n" % e)


# ..journal_correction_details
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str |

accounting = accounting_sh.Accounting("access_token")
try:
    # Details correction
    api_response = accounting.journal_api.journal_correction_details(uuid)
    print("The response of JournalApi->journal_correction_details:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_correction_details: %s\n" % e)


# ..journal_correction_list
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

page = 56  # int |  (optional)
per_page = 56  # int |  (optional)
original_entry = "original_entry_example"  # str |  (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List correction
    api_response = accounting.journal_api.journal_correction_list(
        page=page, per_page=per_page, original_entry=original_entry
    )
    print("The response of JournalApi->journal_correction_list:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_correction_list: %s\n" % e)


# ..journal_correction_update
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str |

accounting = accounting_sh.Accounting("access_token")
try:
    # Reject changes to immutable correction
    accounting.journal_api.journal_correction_update(uuid)
except ApiException as e:
    print("Exception when calling JournalApi->journal_correction_update: %s\n" % e)


# ..journal_entry_add
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

journal_uuid = "journal_uuid_example"  # str |
journal_entry_add_request = (
    accounting_sh.JournalEntryAddRequest()
)  # JournalEntryAddRequest |

accounting = accounting_sh.Accounting("access_token")
try:
    # Add entry
    api_response = accounting.journal_api.journal_entry_add(
        journal_uuid, journal_entry_add_request
    )
    print("The response of JournalApi->journal_entry_add:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_entry_add: %s\n" % e)


# ..journal_entry_delete
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

journal_uuid = "journal_uuid_example"  # str |
entry_uuid = "entry_uuid_example"  # str |

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete entry
    api_response = accounting.journal_api.journal_entry_delete(journal_uuid, entry_uuid)
    print("The response of JournalApi->journal_entry_delete:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_entry_delete: %s\n" % e)


# ..journal_entry_details
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

journal_uuid = "journal_uuid_example"  # str |
entry_uuid = "entry_uuid_example"  # str |

accounting = accounting_sh.Accounting("access_token")
try:
    # Details entry
    api_response = accounting.journal_api.journal_entry_details(
        journal_uuid, entry_uuid
    )
    print("The response of JournalApi->journal_entry_details:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_entry_details: %s\n" % e)


# ..journal_entry_list
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

journal_uuid = "journal_uuid_example"  # str |
page = 56  # int |  (optional)
per_page = 56  # int |  (optional)
status = "status_example"  # str |  (optional)
origin = "origin_example"  # str |  (optional)
period = "period_example"  # str |  (optional)
accounting_date = "accounting_date_example"  # str |  (optional)
var_from = "var_from_example"  # str |  (optional)
to = "to_example"  # str |  (optional)
source_type = "source_type_example"  # str |  (optional)
source_uuid = "source_uuid_example"  # str |  (optional)
code = "code_example"  # str |  (optional)
contact = "contact_example"  # str |  (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List entry
    api_response = accounting.journal_api.journal_entry_list(
        journal_uuid,
        page=page,
        per_page=per_page,
        status=status,
        origin=origin,
        period=period,
        accounting_date=accounting_date,
        var_from=var_from,
        to=to,
        source_type=source_type,
        source_uuid=source_uuid,
        code=code,
        contact=contact,
    )
    print("The response of JournalApi->journal_entry_list:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_entry_list: %s\n" % e)


# ..journal_entry_update
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

journal_uuid = "journal_uuid_example"  # str |
entry_uuid = "entry_uuid_example"  # str |
journal_entry_update_request = (
    accounting_sh.JournalEntryUpdateRequest()
)  # JournalEntryUpdateRequest |

accounting = accounting_sh.Accounting("access_token")
try:
    # Update entry
    api_response = accounting.journal_api.journal_entry_update(
        journal_uuid, entry_uuid, journal_entry_update_request
    )
    print("The response of JournalApi->journal_entry_update:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_entry_update: %s\n" % e)


# ..journal_evidence_add
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

journal_uuid = "journal_uuid_example"  # str |
entry_uuid = "entry_uuid_example"  # str |
journal_evidence_add_request = (
    accounting_sh.JournalEvidenceAddRequest()
)  # JournalEvidenceAddRequest |

accounting = accounting_sh.Accounting("access_token")
try:
    # Add evidence
    api_response = accounting.journal_api.journal_evidence_add(
        journal_uuid, entry_uuid, journal_evidence_add_request
    )
    print("The response of JournalApi->journal_evidence_add:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_evidence_add: %s\n" % e)


# ..journal_evidence_delete
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

journal_uuid = "journal_uuid_example"  # str |
entry_uuid = "entry_uuid_example"  # str |
uuid = "uuid_example"  # str |

accounting = accounting_sh.Accounting("access_token")
try:
    # Reject changes to immutable evidence
    accounting.journal_api.journal_evidence_delete(journal_uuid, entry_uuid, uuid)
except ApiException as e:
    print("Exception when calling JournalApi->journal_evidence_delete: %s\n" % e)


# ..journal_evidence_details
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

journal_uuid = "journal_uuid_example"  # str |
entry_uuid = "entry_uuid_example"  # str |
uuid = "uuid_example"  # str |

accounting = accounting_sh.Accounting("access_token")
try:
    # Details evidence
    api_response = accounting.journal_api.journal_evidence_details(
        journal_uuid, entry_uuid, uuid
    )
    print("The response of JournalApi->journal_evidence_details:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_evidence_details: %s\n" % e)


# ..journal_evidence_list
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

journal_uuid = "journal_uuid_example"  # str |
entry_uuid = "entry_uuid_example"  # str |
page = 56  # int |  (optional)
per_page = 56  # int |  (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List evidence
    api_response = accounting.journal_api.journal_evidence_list(
        journal_uuid, entry_uuid, page=page, per_page=per_page
    )
    print("The response of JournalApi->journal_evidence_list:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_evidence_list: %s\n" % e)


# ..journal_evidence_update
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

journal_uuid = "journal_uuid_example"  # str |
entry_uuid = "entry_uuid_example"  # str |
uuid = "uuid_example"  # str |

accounting = accounting_sh.Accounting("access_token")
try:
    # Reject changes to immutable evidence
    accounting.journal_api.journal_evidence_update(journal_uuid, entry_uuid, uuid)
except ApiException as e:
    print("Exception when calling JournalApi->journal_evidence_update: %s\n" % e)


# ..journal_export_add
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

journal_export_add_request = (
    accounting_sh.JournalExportAddRequest()
)  # JournalExportAddRequest |

accounting = accounting_sh.Accounting("access_token")
try:
    # Add export
    api_response = accounting.journal_api.journal_export_add(journal_export_add_request)
    print("The response of JournalApi->journal_export_add:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_export_add: %s\n" % e)


# ..journal_export_delete
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str |

accounting = accounting_sh.Accounting("access_token")
try:
    # Reject changes to immutable export
    accounting.journal_api.journal_export_delete(uuid)
except ApiException as e:
    print("Exception when calling JournalApi->journal_export_delete: %s\n" % e)


# ..journal_export_details
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str |

accounting = accounting_sh.Accounting("access_token")
try:
    # Details export
    api_response = accounting.journal_api.journal_export_details(uuid)
    print("The response of JournalApi->journal_export_details:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_export_details: %s\n" % e)


# ..journal_export_list
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

page = 56  # int |  (optional)
per_page = 56  # int |  (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List export
    api_response = accounting.journal_api.journal_export_list(
        page=page, per_page=per_page
    )
    print("The response of JournalApi->journal_export_list:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_export_list: %s\n" % e)


# ..journal_export_update
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str |

accounting = accounting_sh.Accounting("access_token")
try:
    # Reject changes to immutable export
    accounting.journal_api.journal_export_update(uuid)
except ApiException as e:
    print("Exception when calling JournalApi->journal_export_update: %s\n" % e)


# ..journal_initialization_add
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

journal_initialization_add_request = (
    accounting_sh.JournalInitializationAddRequest()
)  # JournalInitializationAddRequest |

accounting = accounting_sh.Accounting("access_token")
try:
    # Add initialization
    api_response = accounting.journal_api.journal_initialization_add(
        journal_initialization_add_request
    )
    print("The response of JournalApi->journal_initialization_add:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_initialization_add: %s\n" % e)


# ..journal_initialization_delete
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str |

accounting = accounting_sh.Accounting("access_token")
try:
    # Reject changes to immutable initialization
    accounting.journal_api.journal_initialization_delete(uuid)
except ApiException as e:
    print("Exception when calling JournalApi->journal_initialization_delete: %s\n" % e)


# ..journal_initialization_details
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str |

accounting = accounting_sh.Accounting("access_token")
try:
    # Details initialization
    api_response = accounting.journal_api.journal_initialization_details(uuid)
    print("The response of JournalApi->journal_initialization_details:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_initialization_details: %s\n" % e)


# ..journal_initialization_list
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

page = 56  # int |  (optional)
per_page = 56  # int |  (optional)
status = "status_example"  # str |  (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List initialization
    api_response = accounting.journal_api.journal_initialization_list(
        page=page, per_page=per_page, status=status
    )
    print("The response of JournalApi->journal_initialization_list:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_initialization_list: %s\n" % e)


# ..journal_initialization_update
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str |

accounting = accounting_sh.Accounting("access_token")
try:
    # Reject changes to immutable initialization
    accounting.journal_api.journal_initialization_update(uuid)
except ApiException as e:
    print("Exception when calling JournalApi->journal_initialization_update: %s\n" % e)


# ..journal_issue_add
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

accounting = accounting_sh.Accounting("access_token")
try:
    # Reject changes to immutable issue
    accounting.journal_api.journal_issue_add()
except ApiException as e:
    print("Exception when calling JournalApi->journal_issue_add: %s\n" % e)


# ..journal_issue_delete
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str |

accounting = accounting_sh.Accounting("access_token")
try:
    # Reject changes to immutable issue
    accounting.journal_api.journal_issue_delete(uuid)
except ApiException as e:
    print("Exception when calling JournalApi->journal_issue_delete: %s\n" % e)


# ..journal_issue_details
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str |

accounting = accounting_sh.Accounting("access_token")
try:
    # Details issue
    api_response = accounting.journal_api.journal_issue_details(uuid)
    print("The response of JournalApi->journal_issue_details:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_issue_details: %s\n" % e)


# ..journal_issue_list
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

page = 56  # int |  (optional)
per_page = 56  # int |  (optional)
status = "status_example"  # str |  (optional)
source_type = "source_type_example"  # str |  (optional)
source_uuid = "source_uuid_example"  # str |  (optional)
event = "event_example"  # str |  (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List issue
    api_response = accounting.journal_api.journal_issue_list(
        page=page,
        per_page=per_page,
        status=status,
        source_type=source_type,
        source_uuid=source_uuid,
        event=event,
    )
    print("The response of JournalApi->journal_issue_list:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_issue_list: %s\n" % e)


# ..journal_issue_update
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str |

accounting = accounting_sh.Accounting("access_token")
try:
    # Reject changes to immutable issue
    accounting.journal_api.journal_issue_update(uuid)
except ApiException as e:
    print("Exception when calling JournalApi->journal_issue_update: %s\n" % e)


# ..journal_journal_add
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

journal_journal_add_request = (
    accounting_sh.JournalJournalAddRequest()
)  # JournalJournalAddRequest |

accounting = accounting_sh.Accounting("access_token")
try:
    # Add journal
    api_response = accounting.journal_api.journal_journal_add(
        journal_journal_add_request
    )
    print("The response of JournalApi->journal_journal_add:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_journal_add: %s\n" % e)


# ..journal_journal_delete
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

journal_uuid = "journal_uuid_example"  # str |

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete journal
    api_response = accounting.journal_api.journal_journal_delete(journal_uuid)
    print("The response of JournalApi->journal_journal_delete:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_journal_delete: %s\n" % e)


# ..journal_journal_details
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

journal_uuid = "journal_uuid_example"  # str |

accounting = accounting_sh.Accounting("access_token")
try:
    # Details journal
    api_response = accounting.journal_api.journal_journal_details(journal_uuid)
    print("The response of JournalApi->journal_journal_details:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_journal_details: %s\n" % e)


# ..journal_journal_list
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

page = 56  # int |  (optional)
per_page = 56  # int |  (optional)
status = "status_example"  # str |  (optional)
type = "type_example"  # str |  (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List journal
    api_response = accounting.journal_api.journal_journal_list(
        page=page, per_page=per_page, status=status, type=type
    )
    print("The response of JournalApi->journal_journal_list:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_journal_list: %s\n" % e)


# ..journal_journal_update
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

journal_uuid = "journal_uuid_example"  # str |
journal_journal_update_request = (
    accounting_sh.JournalJournalUpdateRequest()
)  # JournalJournalUpdateRequest |

accounting = accounting_sh.Accounting("access_token")
try:
    # Update journal
    api_response = accounting.journal_api.journal_journal_update(
        journal_uuid, journal_journal_update_request
    )
    print("The response of JournalApi->journal_journal_update:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_journal_update: %s\n" % e)


# ..journal_mapping_add
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

journal_mapping_add_request = (
    accounting_sh.JournalMappingAddRequest()
)  # JournalMappingAddRequest |

accounting = accounting_sh.Accounting("access_token")
try:
    # Add mapping
    api_response = accounting.journal_api.journal_mapping_add(
        journal_mapping_add_request
    )
    print("The response of JournalApi->journal_mapping_add:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_mapping_add: %s\n" % e)


# ..journal_mapping_delete
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str |

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete mapping
    api_response = accounting.journal_api.journal_mapping_delete(uuid)
    print("The response of JournalApi->journal_mapping_delete:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_mapping_delete: %s\n" % e)


# ..journal_mapping_details
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str |

accounting = accounting_sh.Accounting("access_token")
try:
    # Details mapping
    api_response = accounting.journal_api.journal_mapping_details(uuid)
    print("The response of JournalApi->journal_mapping_details:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_mapping_details: %s\n" % e)


# ..journal_mapping_list
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

page = 56  # int |  (optional)
per_page = 56  # int |  (optional)
role = "role_example"  # str |  (optional)
scope = "scope_example"  # str |  (optional)
status = "status_example"  # str |  (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List mapping
    api_response = accounting.journal_api.journal_mapping_list(
        page=page, per_page=per_page, role=role, scope=scope, status=status
    )
    print("The response of JournalApi->journal_mapping_list:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_mapping_list: %s\n" % e)


# ..journal_mapping_update
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str |
journal_mapping_update_request = (
    accounting_sh.JournalMappingUpdateRequest()
)  # JournalMappingUpdateRequest |

accounting = accounting_sh.Accounting("access_token")
try:
    # Update mapping
    api_response = accounting.journal_api.journal_mapping_update(
        uuid, journal_mapping_update_request
    )
    print("The response of JournalApi->journal_mapping_update:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_mapping_update: %s\n" % e)


# ..journal_movements
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

code = "code_example"  # str |
var_from = "2013-10-20"  # date |  (optional)
to = "2013-10-20"  # date |  (optional)
contact = "contact_example"  # str |  (optional)
journal = "journal_example"  # str |  (optional)
period = "period_example"  # str |  (optional)
bank_account = "bank_account_example"  # str |  (optional)
page = 56  # int |  (optional)
per_page = 56  # int |  (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # Posted account movements
    api_response = accounting.journal_api.journal_movements(
        code,
        var_from=var_from,
        to=to,
        contact=contact,
        journal=journal,
        period=period,
        bank_account=bank_account,
        page=page,
        per_page=per_page,
    )
    print("The response of JournalApi->journal_movements:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_movements: %s\n" % e)


# ..journal_period_add
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

journal_period_add_request = (
    accounting_sh.JournalPeriodAddRequest()
)  # JournalPeriodAddRequest |

accounting = accounting_sh.Accounting("access_token")
try:
    # Add period
    api_response = accounting.journal_api.journal_period_add(journal_period_add_request)
    print("The response of JournalApi->journal_period_add:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_period_add: %s\n" % e)


# ..journal_period_delete
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str |

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete period
    api_response = accounting.journal_api.journal_period_delete(uuid)
    print("The response of JournalApi->journal_period_delete:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_period_delete: %s\n" % e)


# ..journal_period_details
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str |

accounting = accounting_sh.Accounting("access_token")
try:
    # Details period
    api_response = accounting.journal_api.journal_period_details(uuid)
    print("The response of JournalApi->journal_period_details:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_period_details: %s\n" % e)


# ..journal_period_list
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

page = 56  # int |  (optional)
per_page = 56  # int |  (optional)
status = "status_example"  # str |  (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List period
    api_response = accounting.journal_api.journal_period_list(
        page=page, per_page=per_page, status=status
    )
    print("The response of JournalApi->journal_period_list:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_period_list: %s\n" % e)


# ..journal_period_update
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str |
journal_period_update_request = (
    accounting_sh.JournalPeriodUpdateRequest()
)  # JournalPeriodUpdateRequest |

accounting = accounting_sh.Accounting("access_token")
try:
    # Update period
    api_response = accounting.journal_api.journal_period_update(
        uuid, journal_period_update_request
    )
    print("The response of JournalApi->journal_period_update:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_period_update: %s\n" % e)


# ..journal_profitandloss
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

var_from = "2013-10-20"  # date |  (optional)
to = "2013-10-20"  # date |  (optional)
code = "code_example"  # str |  (optional)
contact = "contact_example"  # str |  (optional)
journal = "journal_example"  # str |  (optional)
period = "period_example"  # str |  (optional)
bank_account = "bank_account_example"  # str |  (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # Profit and loss
    api_response = accounting.journal_api.journal_profitandloss(
        var_from=var_from,
        to=to,
        code=code,
        contact=contact,
        journal=journal,
        period=period,
        bank_account=bank_account,
    )
    print("The response of JournalApi->journal_profitandloss:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_profitandloss: %s\n" % e)


# ..journal_trialbalance
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

var_from = "2013-10-20"  # date |  (optional)
to = "2013-10-20"  # date |  (optional)
code = "code_example"  # str |  (optional)
contact = "contact_example"  # str |  (optional)
journal = "journal_example"  # str |  (optional)
period = "period_example"  # str |  (optional)
bank_account = "bank_account_example"  # str |  (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # Trial balance
    api_response = accounting.journal_api.journal_trialbalance(
        var_from=var_from,
        to=to,
        code=code,
        contact=contact,
        journal=journal,
        period=period,
        bank_account=bank_account,
    )
    print("The response of JournalApi->journal_trialbalance:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalApi->journal_trialbalance: %s\n" % e)


# ..logs
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = "uuid,channel,level,message,recorded_at"  # str | Comma-separated fields to include in each record. Default fields: uuid, channel, level, message, recorded_at. (optional)
page = 1  # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10  # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
channel = "channel_example"  # str | The channel to retrieve the logs from (optional)
level = "level_example"  # str | The log level to retrieve (optional)
resource = "resource_example"  # str | Retrive logs linked to that resource (optional)
before = "before_example"  # str | Retrive logs before the provided date (optional)
after = "after_example"  # str | Retrive logs after the provided date (optional)
format = "format_example"  # str | In which format to retrieve the logs, available: json or txt (optional)
order_by = "created_at:desc"  # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's logs
    api_response = accounting.logs_api.logs(
        fields=fields,
        page=page,
        per_page=per_page,
        channel=channel,
        level=level,
        resource=resource,
        before=before,
        after=after,
        format=format,
        order_by=order_by,
    )
    print("The response of LogsApi->logs:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogsApi->logs: %s\n" % e)


# ..list_notification_preferences
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

notification = "notification_example"  # str | The notification name

accounting = accounting_sh.Accounting("access_token")
try:
    # List notification preferences
    api_response = accounting.notification_api.list_notification_preferences(
        notification
    )
    print("The response of NotificationApi->list_notification_preferences:\n")
    pprint(api_response)
except ApiException as e:
    print(
        "Exception when calling NotificationApi->list_notification_preferences: %s\n"
        % e
    )


# ..list_notifications
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = "uuid,notification"  # str | Comma-separated fields to include in each record. Default fields: uuid, notification. (optional)
page = 1  # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10  # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = "created_at:desc"  # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's notifications
    api_response = accounting.notification_api.list_notifications(
        fields=fields, page=page, per_page=per_page, order_by=order_by
    )
    print("The response of NotificationApi->list_notifications:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->list_notifications: %s\n" % e)


# ..send_notification
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

send_notification_request = (
    accounting_sh.SendNotificationRequest()
)  # SendNotificationRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Send a notification
    api_response = accounting.notification_api.send_notification(
        send_notification_request
    )
    print("The response of NotificationApi->send_notification:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->send_notification: %s\n" % e)


# ..update_notification_preferences
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

notification = "notification_example"  # str | The notification name
update_notification_preferences_request = (
    accounting_sh.UpdateNotificationPreferencesRequest()
)  # UpdateNotificationPreferencesRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update notification preferences
    api_response = accounting.notification_api.update_notification_preferences(
        notification, update_notification_preferences_request
    )
    print("The response of NotificationApi->update_notification_preferences:\n")
    pprint(api_response)
except ApiException as e:
    print(
        "Exception when calling NotificationApi->update_notification_preferences: %s\n"
        % e
    )


# ..add_notification_type
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_notification_type_request = (
    accounting_sh.AddNotificationTypeRequest()
)  # AddNotificationTypeRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Add a notification type
    api_response = accounting.notification_types_api.add_notification_type(
        add_notification_type_request
    )
    print("The response of NotificationTypesApi->add_notification_type:\n")
    pprint(api_response)
except ApiException as e:
    print(
        "Exception when calling NotificationTypesApi->add_notification_type: %s\n" % e
    )


# ..delete_notification_type
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The notification type uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete a notification type
    api_response = accounting.notification_types_api.delete_notification_type(uuid)
    print("The response of NotificationTypesApi->delete_notification_type:\n")
    pprint(api_response)
except ApiException as e:
    print(
        "Exception when calling NotificationTypesApi->delete_notification_type: %s\n"
        % e
    )


# ..get_notification_type
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The notification type uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a notification type
    api_response = accounting.notification_types_api.get_notification_type(uuid)
    print("The response of NotificationTypesApi->get_notification_type:\n")
    pprint(api_response)
except ApiException as e:
    print(
        "Exception when calling NotificationTypesApi->get_notification_type: %s\n" % e
    )


# ..list_notification_types
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = "name,title,description,allowed_methods,internal"  # str | Comma-separated fields to include in each record. Default fields: name, title, description, allowed_methods, internal. (optional)
page = 1  # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10  # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = "created_at:desc"  # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's notification types
    api_response = accounting.notification_types_api.list_notification_types(
        fields=fields, page=page, per_page=per_page, order_by=order_by
    )
    print("The response of NotificationTypesApi->list_notification_types:\n")
    pprint(api_response)
except ApiException as e:
    print(
        "Exception when calling NotificationTypesApi->list_notification_types: %s\n" % e
    )


# ..update_notification_type
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The notification type uuid
update_notification_type_request = (
    accounting_sh.UpdateNotificationTypeRequest()
)  # UpdateNotificationTypeRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a notification type
    api_response = accounting.notification_types_api.update_notification_type(
        uuid, update_notification_type_request
    )
    print("The response of NotificationTypesApi->update_notification_type:\n")
    pprint(api_response)
except ApiException as e:
    print(
        "Exception when calling NotificationTypesApi->update_notification_type: %s\n"
        % e
    )


# ..add_o_auth_configuration
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_o_auth_configuration_request = (
    accounting_sh.AddOAuthConfigurationRequest()
)  # AddOAuthConfigurationRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Add an OAuth configuration
    api_response = accounting.o_auth_config_api.add_o_auth_configuration(
        add_o_auth_configuration_request
    )
    print("The response of OAuthConfigApi->add_o_auth_configuration:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthConfigApi->add_o_auth_configuration: %s\n" % e)


# ..delete_o_auth_configuration
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The oauth configuration uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete an oauth configuration
    api_response = accounting.o_auth_config_api.delete_o_auth_configuration(uuid)
    print("The response of OAuthConfigApi->delete_o_auth_configuration:\n")
    pprint(api_response)
except ApiException as e:
    print(
        "Exception when calling OAuthConfigApi->delete_o_auth_configuration: %s\n" % e
    )


# ..get_o_auth_configuration
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The oauth configuration uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get an OAuth configuration
    api_response = accounting.o_auth_config_api.get_o_auth_configuration(uuid)
    print("The response of OAuthConfigApi->get_o_auth_configuration:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthConfigApi->get_o_auth_configuration: %s\n" % e)


# ..list_o_auth_configurations
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = "uuid,provider,client_id"  # str | Comma-separated fields to include in each record. Default fields: uuid, provider, client_id. (optional)
page = 1  # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10  # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = "created_at:desc"  # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's oauth configurations
    api_response = accounting.o_auth_config_api.list_o_auth_configurations(
        fields=fields, page=page, per_page=per_page, order_by=order_by
    )
    print("The response of OAuthConfigApi->list_o_auth_configurations:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthConfigApi->list_o_auth_configurations: %s\n" % e)


# ..list_providers
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

accounting = accounting_sh.Accounting("access_token")
try:
    # List available providers
    api_response = accounting.o_auth_config_api.list_providers()
    print("The response of OAuthConfigApi->list_providers:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthConfigApi->list_providers: %s\n" % e)


# ..update_o_auth_configuration
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The oauth configuration uuid
add_o_auth_configuration_request = (
    accounting_sh.AddOAuthConfigurationRequest()
)  # AddOAuthConfigurationRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update an oauth configuration
    api_response = accounting.o_auth_config_api.update_o_auth_configuration(
        uuid, add_o_auth_configuration_request
    )
    print("The response of OAuthConfigApi->update_o_auth_configuration:\n")
    pprint(api_response)
except ApiException as e:
    print(
        "Exception when calling OAuthConfigApi->update_o_auth_configuration: %s\n" % e
    )


# ..add_payment
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_payment_request = (
    accounting_sh.AddPaymentRequest()
)  # AddPaymentRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Add a payment
    api_response = accounting.payments_api.add_payment(add_payment_request)
    print("The response of PaymentsApi->add_payment:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->add_payment: %s\n" % e)


# ..delete_payment
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The payment uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete a payment
    api_response = accounting.payments_api.delete_payment(uuid)
    print("The response of PaymentsApi->delete_payment:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->delete_payment: %s\n" % e)


# ..get_payment
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The payment uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a payment
    api_response = accounting.payments_api.get_payment(uuid)
    print("The response of PaymentsApi->get_payment:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->get_payment: %s\n" % e)


# ..list_payments
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = "uuid,amount,currency,contact"  # str | Comma-separated fields to include in each record. Default fields: uuid, amount, currency, contact. (optional)
page = 1  # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10  # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = "created_at:desc"  # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's payments
    api_response = accounting.payments_api.list_payments(
        fields=fields, page=page, per_page=per_page, order_by=order_by
    )
    print("The response of PaymentsApi->list_payments:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->list_payments: %s\n" % e)


# ..update_payment
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The payment uuid
add_payment_request = (
    accounting_sh.AddPaymentRequest()
)  # AddPaymentRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a payment
    api_response = accounting.payments_api.update_payment(uuid, add_payment_request)
    print("The response of PaymentsApi->update_payment:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->update_payment: %s\n" % e)


# ..add_quote
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_quote_request = (
    accounting_sh.AddQuoteRequest()
)  # AddQuoteRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Add a quote
    api_response = accounting.quotes_api.add_quote(add_quote_request)
    print("The response of QuotesApi->add_quote:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotesApi->add_quote: %s\n" % e)


# ..delete_quote
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The quote uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete a quote
    api_response = accounting.quotes_api.delete_quote(uuid)
    print("The response of QuotesApi->delete_quote:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotesApi->delete_quote: %s\n" % e)


# ..get_quote
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The quote uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a quote
    api_response = accounting.quotes_api.get_quote(uuid)
    print("The response of QuotesApi->get_quote:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotesApi->get_quote: %s\n" % e)


# ..get_quote_document
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The quote uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a quote in PDF
    api_response = accounting.quotes_api.get_quote_document(uuid)
    print("The response of QuotesApi->get_quote_document:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotesApi->get_quote_document: %s\n" % e)


# ..list_quotes
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = "uuid,contact,quote_number,status"  # str | Comma-separated fields to include in each record. Default fields: uuid, contact, quote_number, status. (optional)
page = 1  # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10  # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = "created_at:desc"  # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's quotes
    api_response = accounting.quotes_api.list_quotes(
        fields=fields, page=page, per_page=per_page, order_by=order_by
    )
    print("The response of QuotesApi->list_quotes:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotesApi->list_quotes: %s\n" % e)


# ..update_quote
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The quote uuid
update_quote_request = (
    accounting_sh.UpdateQuoteRequest()
)  # UpdateQuoteRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a quote
    api_response = accounting.quotes_api.update_quote(uuid, update_quote_request)
    print("The response of QuotesApi->update_quote:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotesApi->update_quote: %s\n" % e)


# ..add_receipt
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_receipt_request = (
    accounting_sh.AddReceiptRequest()
)  # AddReceiptRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Add a receipt
    api_response = accounting.receipts_api.add_receipt(add_receipt_request)
    print("The response of ReceiptsApi->add_receipt:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceiptsApi->add_receipt: %s\n" % e)


# ..delete_receipt
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The receipt uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete a receipt
    api_response = accounting.receipts_api.delete_receipt(uuid)
    print("The response of ReceiptsApi->delete_receipt:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceiptsApi->delete_receipt: %s\n" % e)


# ..get_receipt
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The receipt uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a receipt
    api_response = accounting.receipts_api.get_receipt(uuid)
    print("The response of ReceiptsApi->get_receipt:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceiptsApi->get_receipt: %s\n" % e)


# ..get_receipt_document
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The receipt uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a receipt in PDF
    api_response = accounting.receipts_api.get_receipt_document(uuid)
    print("The response of ReceiptsApi->get_receipt_document:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceiptsApi->get_receipt_document: %s\n" % e)


# ..list_receipts
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = "uuid,for,from,receipt_number"  # str | Comma-separated fields to include in each record. Default fields: uuid, for, from, receipt_number. (optional)
page = 1  # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10  # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = "created_at:desc"  # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's receipts
    api_response = accounting.receipts_api.list_receipts(
        fields=fields, page=page, per_page=per_page, order_by=order_by
    )
    print("The response of ReceiptsApi->list_receipts:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceiptsApi->list_receipts: %s\n" % e)


# ..update_receipt
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The receipt uuid
update_receipt_request = (
    accounting_sh.UpdateReceiptRequest()
)  # UpdateReceiptRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a receipt
    api_response = accounting.receipts_api.update_receipt(uuid, update_receipt_request)
    print("The response of ReceiptsApi->update_receipt:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceiptsApi->update_receipt: %s\n" % e)


# ..add_revenue
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_revenue_request = (
    accounting_sh.AddRevenueRequest()
)  # AddRevenueRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Add a revenue
    api_response = accounting.revenues_api.add_revenue(add_revenue_request)
    print("The response of RevenuesApi->add_revenue:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevenuesApi->add_revenue: %s\n" % e)


# ..delete_revenue
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The revenue uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete a revenue
    api_response = accounting.revenues_api.delete_revenue(uuid)
    print("The response of RevenuesApi->delete_revenue:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevenuesApi->delete_revenue: %s\n" % e)


# ..get_revenue
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The revenue uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a revenue
    api_response = accounting.revenues_api.get_revenue(uuid)
    print("The response of RevenuesApi->get_revenue:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevenuesApi->get_revenue: %s\n" % e)


# ..list_revenues
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = "uuid,paid_at,amount,currency"  # str | Comma-separated fields to include in each record. Default fields: uuid, paid_at, amount, currency. (optional)
page = 1  # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10  # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = "created_at:desc"  # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's revenues
    api_response = accounting.revenues_api.list_revenues(
        fields=fields, page=page, per_page=per_page, order_by=order_by
    )
    print("The response of RevenuesApi->list_revenues:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevenuesApi->list_revenues: %s\n" % e)


# ..update_revenue
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The revenue uuid
add_revenue_request = (
    accounting_sh.AddRevenueRequest()
)  # AddRevenueRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a revenue
    api_response = accounting.revenues_api.update_revenue(uuid, add_revenue_request)
    print("The response of RevenuesApi->update_revenue:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevenuesApi->update_revenue: %s\n" % e)


# ..list_reviews
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = "uuid,name,process_status"  # str | Comma-separated fields to include in each record. Default fields: uuid, name, process_status. (optional)
page = 1  # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10  # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = "created_at:desc"  # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List documents to be reviewed
    api_response = accounting.rossum_api.list_reviews(
        fields=fields, page=page, per_page=per_page, order_by=order_by
    )
    print("The response of RossumApi->list_reviews:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RossumApi->list_reviews: %s\n" % e)


# ..search
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

q = "q_example"  # str | Query string
exclude = "exclude_example"  # str | Exclude specific types. This is a comma separated list. (optional)
only = "only_example"  # str | Perfom search only on those types. This is a comma separated list. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # Search
    api_response = accounting.search_api.search(q, exclude=exclude, only=only)
    print("The response of SearchApi->search:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search: %s\n" % e)


# ..get_settings
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The company uuid
key = "key_example"  # str | The setting key

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a company's settings
    api_response = accounting.settings_api.get_settings(uuid, key)
    print("The response of SettingsApi->get_settings:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->get_settings: %s\n" % e)


# ..list_settings
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The company uuid
fields = "uuid,key,value"  # str | Comma-separated fields to include in each record. Default fields: uuid, key, value. (optional)
page = 1  # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10  # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = "created_at:desc"  # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's settings
    api_response = accounting.settings_api.list_settings(
        uuid, fields=fields, page=page, per_page=per_page, order_by=order_by
    )
    print("The response of SettingsApi->list_settings:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->list_settings: %s\n" % e)


# ..update_settings
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The company uuid
key = "key_example"  # str | The setting key
update_settings_request = (
    accounting_sh.UpdateSettingsRequest()
)  # UpdateSettingsRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a company's settings
    api_response = accounting.settings_api.update_settings(
        uuid, key, update_settings_request
    )
    print("The response of SettingsApi->update_settings:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->update_settings: %s\n" % e)


# ..summary_statistics_period
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The company uuid
start = "2013-10-20"  # date | The start date (optional)
end = "2013-10-20"  # date | The end date (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # Company's summary statistics
    api_response = accounting.statistics_api.summary_statistics_period(
        uuid, start=start, end=end
    )
    print("The response of StatisticsApi->summary_statistics_period:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->summary_statistics_period: %s\n" % e)


# ..add_tag
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_tag_request = (
    accounting_sh.AddTagRequest()
)  # AddTagRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Add a tag
    api_response = accounting.tags_api.add_tag(add_tag_request)
    print("The response of TagsApi->add_tag:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->add_tag: %s\n" % e)


# ..delete_tag
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The tag uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete a tag
    api_response = accounting.tags_api.delete_tag(uuid)
    print("The response of TagsApi->delete_tag:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->delete_tag: %s\n" % e)


# ..get_tag
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The tag uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a tag
    api_response = accounting.tags_api.get_tag(uuid)
    print("The response of TagsApi->get_tag:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->get_tag: %s\n" % e)


# ..list_tags
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = "uuid,key,value,attached_at"  # str | Comma-separated fields to include in each record. Default fields: uuid, key, value, attached_at. (optional)
page = 1  # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10  # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = "created_at:desc"  # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's tags
    api_response = accounting.tags_api.list_tags(
        fields=fields, page=page, per_page=per_page, order_by=order_by
    )
    print("The response of TagsApi->list_tags:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->list_tags: %s\n" % e)


# ..list_tags_by_resource
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

resource = "resource_example"  # str | The resource
fields = "uuid,key,value,attached_at"  # str | Comma-separated fields to include in each record. Default fields: uuid, key, value, attached_at. (optional)
page = 1  # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10  # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = "created_at:desc"  # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's tags by resource attachment
    api_response = accounting.tags_api.list_tags_by_resource(
        resource, fields=fields, page=page, per_page=per_page, order_by=order_by
    )
    print("The response of TagsApi->list_tags_by_resource:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->list_tags_by_resource: %s\n" % e)


# ..update_tag
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The tag uuid
add_tag_request = (
    accounting_sh.AddTagRequest()
)  # AddTagRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a tag
    api_response = accounting.tags_api.update_tag(uuid, add_tag_request)
    print("The response of TagsApi->update_tag:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->update_tag: %s\n" % e)


# ..get_tax_rate
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

country = "country_example"  # str | The country

accounting = accounting_sh.Accounting("access_token")
try:
    # Get the latest tax rate for a country
    api_response = accounting.tax_api.get_tax_rate(country)
    print("The response of TaxApi->get_tax_rate:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxApi->get_tax_rate: %s\n" % e)


# ..verify_vat_id
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

number = "number_example"  # str | The VAT ID

accounting = accounting_sh.Accounting("access_token")
try:
    # Verify a VAT ID
    api_response = accounting.tax_api.verify_vat_id(number)
    print("The response of TaxApi->verify_vat_id:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxApi->verify_vat_id: %s\n" % e)


# ..add_link
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | A transaction uuid
add_link_request = (
    accounting_sh.AddLinkRequest()
)  # AddLinkRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Add a new transaction link
    api_response = accounting.transactions_api.add_link(uuid, add_link_request)
    print("The response of TransactionsApi->add_link:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->add_link: %s\n" % e)


# ..add_transaction
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_transaction_request = (
    accounting_sh.AddTransactionRequest()
)  # AddTransactionRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Add a transaction
    api_response = accounting.transactions_api.add_transaction(add_transaction_request)
    print("The response of TransactionsApi->add_transaction:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->add_transaction: %s\n" % e)


# ..add_transaction_code
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The transaction uuid
add_transaction_code_request = (
    accounting_sh.AddTransactionCodeRequest()
)  # AddTransactionCodeRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Add a transaction's code
    api_response = accounting.transactions_api.add_transaction_code(
        uuid, add_transaction_code_request
    )
    print("The response of TransactionsApi->add_transaction_code:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->add_transaction_code: %s\n" % e)


# ..delete_link
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | A transaction uuid
link_uuid = "link_uuid_example"  # str | A transaction link uuid OR the target uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete a transaction link
    api_response = accounting.transactions_api.delete_link(uuid, link_uuid)
    print("The response of TransactionsApi->delete_link:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->delete_link: %s\n" % e)


# ..delete_transaction
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The transaction uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete a transaction
    api_response = accounting.transactions_api.delete_transaction(uuid)
    print("The response of TransactionsApi->delete_transaction:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->delete_transaction: %s\n" % e)


# ..delete_transaction_code
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The transaction uuid
code = "code_example"  # str | The transaction's code uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete a transaction's code
    api_response = accounting.transactions_api.delete_transaction_code(uuid, code)
    print("The response of TransactionsApi->delete_transaction_code:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->delete_transaction_code: %s\n" % e)


# ..get_transaction
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The transaction uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a transaction
    api_response = accounting.transactions_api.get_transaction(uuid)
    print("The response of TransactionsApi->get_transaction:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->get_transaction: %s\n" % e)


# ..import_transactions
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

import_transactions_request = (
    accounting_sh.ImportTransactionsRequest()
)  # ImportTransactionsRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Import transactions - INTERNAL
    api_response = accounting.transactions_api.import_transactions(
        import_transactions_request
    )
    print("The response of TransactionsApi->import_transactions:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->import_transactions: %s\n" % e)


# ..ledger
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = "uuid,account,amount,event_date"  # str | Comma-separated fields to include in each record. Default fields: uuid, account, amount, event_date. (optional)
page = 1  # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10  # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
account = "account_example"  # str | An account uuid to filter results (optional)
order_by = "created_at:desc"  # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's transactions and transfers
    api_response = accounting.transactions_api.ledger(
        fields=fields, page=page, per_page=per_page, account=account, order_by=order_by
    )
    print("The response of TransactionsApi->ledger:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->ledger: %s\n" % e)


# ..list_links
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | A transaction uuid
fields = "target_type,target,link_status"  # str | Comma-separated fields to include in each record. Default fields: target_type, target, link_status. (optional)
page = 1  # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10  # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = "created_at:desc"  # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List a transaction links
    api_response = accounting.transactions_api.list_links(
        uuid, fields=fields, page=page, per_page=per_page, order_by=order_by
    )
    print("The response of TransactionsApi->list_links:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->list_links: %s\n" % e)


# ..list_transaction_codes
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The transaction uuid
fields = "uuid,code,description,amount"  # str | Comma-separated fields to include in each record. Default fields: uuid, code, description, amount. (optional)
page = 1  # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10  # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
account = "account_example"  # str | List to the specified account (optional)
order_by = "created_at:desc"  # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List transaction's codes
    api_response = accounting.transactions_api.list_transaction_codes(
        uuid,
        fields=fields,
        page=page,
        per_page=per_page,
        account=account,
        order_by=order_by,
    )
    print("The response of TransactionsApi->list_transaction_codes:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->list_transaction_codes: %s\n" % e)


# ..list_transactions
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = "uuid,account,amount,transaction_date"  # str | Comma-separated fields to include in each record. Default fields: uuid, account, amount, transaction_date. (optional)
page = 1  # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10  # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
account = "account_example"  # str | List to the specified account (optional)
order_by = "created_at:desc"  # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's transactions
    api_response = accounting.transactions_api.list_transactions(
        fields=fields, page=page, per_page=per_page, account=account, order_by=order_by
    )
    print("The response of TransactionsApi->list_transactions:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->list_transactions: %s\n" % e)


# ..reconciliation_reject
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str |
reconciliation_reject_request = (
    accounting_sh.ReconciliationRejectRequest()
)  # ReconciliationRejectRequest |

accounting = accounting_sh.Accounting("access_token")
try:
    # Remember a rejected transaction/document candidate
    api_response = accounting.transactions_api.reconciliation_reject(
        uuid, reconciliation_reject_request
    )
    print("The response of TransactionsApi->reconciliation_reject:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->reconciliation_reject: %s\n" % e)


# ..reconciliation_run
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str |

accounting = accounting_sh.Accounting("access_token")
try:
    # Schedule background matching for human review
    api_response = accounting.transactions_api.reconciliation_run(uuid)
    print("The response of TransactionsApi->reconciliation_run:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->reconciliation_run: %s\n" % e)


# ..reconciliation_suggestions
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str |

accounting = accounting_sh.Accounting("access_token")
try:
    # Rank document and payment matches without creating links
    api_response = accounting.transactions_api.reconciliation_suggestions(uuid)
    print("The response of TransactionsApi->reconciliation_suggestions:\n")
    pprint(api_response)
except ApiException as e:
    print(
        "Exception when calling TransactionsApi->reconciliation_suggestions: %s\n" % e
    )


# ..reverse_transaction_link
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str |
link_uuid = "link_uuid_example"  # str |

accounting = accounting_sh.Accounting("access_token")
try:
    # Reverse a human-confirmed match and its generated payment
    api_response = accounting.transactions_api.reverse_transaction_link(uuid, link_uuid)
    print("The response of TransactionsApi->reverse_transaction_link:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->reverse_transaction_link: %s\n" % e)


# ..update_link
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | A transaction uuid
link_uuid = "link_uuid_example"  # str | A transaction link uuid OR the target uuid
add_link_request = (
    accounting_sh.AddLinkRequest()
)  # AddLinkRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a transaction link
    api_response = accounting.transactions_api.update_link(
        uuid, link_uuid, add_link_request
    )
    print("The response of TransactionsApi->update_link:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->update_link: %s\n" % e)


# ..update_transaction
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The transaction uuid
add_transaction_request = (
    accounting_sh.AddTransactionRequest()
)  # AddTransactionRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a transaction
    api_response = accounting.transactions_api.update_transaction(
        uuid, add_transaction_request
    )
    print("The response of TransactionsApi->update_transaction:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->update_transaction: %s\n" % e)


# ..update_transaction_code
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The transaction uuid
code = "code_example"  # str | Identifier of the code selected by this route.
add_transaction_code_request = (
    accounting_sh.AddTransactionCodeRequest()
)  # AddTransactionCodeRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a transaction's code
    api_response = accounting.transactions_api.update_transaction_code(
        uuid, code, add_transaction_code_request
    )
    print("The response of TransactionsApi->update_transaction_code:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->update_transaction_code: %s\n" % e)


# ..view_link
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | A transaction uuid
link_uuid = "link_uuid_example"  # str | A transaction link uuid OR the target uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # View a transaction link
    api_response = accounting.transactions_api.view_link(uuid, link_uuid)
    print("The response of TransactionsApi->view_link:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->view_link: %s\n" % e)


# ..add_transfer
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_transfer_request = (
    accounting_sh.AddTransferRequest()
)  # AddTransferRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Add a transfer
    api_response = accounting.transfers_api.add_transfer(add_transfer_request)
    print("The response of TransfersApi->add_transfer:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransfersApi->add_transfer: %s\n" % e)


# ..delete_transfer
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The transfer uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete a transfer
    api_response = accounting.transfers_api.delete_transfer(uuid)
    print("The response of TransfersApi->delete_transfer:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransfersApi->delete_transfer: %s\n" % e)


# ..get_transfer
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The transfer uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a transfer
    api_response = accounting.transfers_api.get_transfer(uuid)
    print("The response of TransfersApi->get_transfer:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransfersApi->get_transfer: %s\n" % e)


# ..list_transfers
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = "uuid,from,to,amount"  # str | Comma-separated fields to include in each record. Default fields: uuid, from, to, amount. (optional)
page = 1  # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10  # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = "created_at:desc"  # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's transfers
    api_response = accounting.transfers_api.list_transfers(
        fields=fields, page=page, per_page=per_page, order_by=order_by
    )
    print("The response of TransfersApi->list_transfers:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransfersApi->list_transfers: %s\n" % e)


# ..update_transfer
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The transfer uuid
add_transfer_request = (
    accounting_sh.AddTransferRequest()
)  # AddTransferRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a transfer
    api_response = accounting.transfers_api.update_transfer(uuid, add_transfer_request)
    print("The response of TransfersApi->update_transfer:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransfersApi->update_transfer: %s\n" % e)


# ..add_user
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

accounting = accounting_sh.Accounting("access_token")
try:
    # Add user
    api_response = accounting.users_api.add_user()
    print("The response of UsersApi->add_user:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->add_user: %s\n" % e)


# ..delete_user
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The user uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete user
    api_response = accounting.users_api.delete_user(uuid)
    print("The response of UsersApi->delete_user:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->delete_user: %s\n" % e)


# ..get_user
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The user uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # View user
    api_response = accounting.users_api.get_user(uuid)
    print("The response of UsersApi->get_user:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user: %s\n" % e)


# ..list_users
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = "uuid,user,permissions"  # str | Comma-separated fields to include in each record. Default fields: uuid, user, permissions. (optional)
page = 1  # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10  # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = "created_at:desc"  # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's users
    api_response = accounting.users_api.list_users(
        fields=fields, page=page, per_page=per_page, order_by=order_by
    )
    print("The response of UsersApi->list_users:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->list_users: %s\n" % e)


# ..update_me_put_alias
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

accounting = accounting_sh.Accounting("access_token")
try:
    # Update current user details
    api_response = accounting.users_api.update_me_put_alias()
    print("The response of UsersApi->update_me_put_alias:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_me_put_alias: %s\n" % e)


# ..update_user
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The user uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Update user
    api_response = accounting.users_api.update_user(uuid)
    print("The response of UsersApi->update_user:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_user: %s\n" % e)


# ..users_companies
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

accounting = accounting_sh.Accounting("access_token")
try:
    # List current user companies
    api_response = accounting.users_api.users_companies()
    print("The response of UsersApi->users_companies:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_companies: %s\n" % e)


# ..users_me
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

accounting = accounting_sh.Accounting("access_token")
try:
    # View current user details
    api_response = accounting.users_api.users_me()
    print("The response of UsersApi->users_me:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_me: %s\n" % e)


# ..add_company_vat_id
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The company uuid
add_company_vat_id_request = (
    accounting_sh.AddCompanyVatIdRequest()
)  # AddCompanyVatIdRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Add a company's Vat Id
    api_response = accounting.vatid_api.add_company_vat_id(
        uuid, add_company_vat_id_request
    )
    print("The response of VATIDApi->add_company_vat_id:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VATIDApi->add_company_vat_id: %s\n" % e)


# ..delete_company_vat_id
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The company uuid
key = "key_example"  # str | The VAT ID uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete a company's Vat Id
    api_response = accounting.vatid_api.delete_company_vat_id(uuid, key)
    print("The response of VATIDApi->delete_company_vat_id:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VATIDApi->delete_company_vat_id: %s\n" % e)


# ..get_company_vat_id
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The company uuid
key = "key_example"  # str | The VAT ID uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a company's Vat Id
    api_response = accounting.vatid_api.get_company_vat_id(uuid, key)
    print("The response of VATIDApi->get_company_vat_id:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VATIDApi->get_company_vat_id: %s\n" % e)


# ..list_company_vat_id
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The company uuid
fields = "uuid,vat_id,country"  # str | Comma-separated fields to include in each record. Default fields: uuid, vat_id, country. (optional)
page = 1  # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10  # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = "created_at:desc"  # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's Vat Id
    api_response = accounting.vatid_api.list_company_vat_id(
        uuid, fields=fields, page=page, per_page=per_page, order_by=order_by
    )
    print("The response of VATIDApi->list_company_vat_id:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VATIDApi->list_company_vat_id: %s\n" % e)


# ..update_company_vat_id
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The company uuid
key = "key_example"  # str | The VAT ID uuid
add_company_vat_id_request = (
    accounting_sh.AddCompanyVatIdRequest()
)  # AddCompanyVatIdRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a company's Vat Id
    api_response = accounting.vatid_api.update_company_vat_id(
        uuid, key, add_company_vat_id_request
    )
    print("The response of VATIDApi->update_company_vat_id:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VATIDApi->update_company_vat_id: %s\n" % e)


# ..add_webhook
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_webhook_request = (
    accounting_sh.AddWebhookRequest()
)  # AddWebhookRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Add a webhook
    api_response = accounting.webhooks_api.add_webhook(add_webhook_request)
    print("The response of WebhooksApi->add_webhook:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->add_webhook: %s\n" % e)


# ..delete_webhook
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The webhook uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete a webhook
    api_response = accounting.webhooks_api.delete_webhook(uuid)
    print("The response of WebhooksApi->delete_webhook:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->delete_webhook: %s\n" % e)


# ..get_webhook
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The webhook uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a webhook
    api_response = accounting.webhooks_api.get_webhook(uuid)
    print("The response of WebhooksApi->get_webhook:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->get_webhook: %s\n" % e)


# ..get_webhook_history
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The webhook uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get webhook's history
    api_response = accounting.webhooks_api.get_webhook_history(uuid)
    print("The response of WebhooksApi->get_webhook_history:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->get_webhook_history: %s\n" % e)


# ..list_webhook_events
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


# ..list_webhooks
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = "uuid,link,events"  # str | Comma-separated fields to include in each record. Default fields: uuid, link, events. (optional)
page = 1  # int | Page number, starting at 1. Values below 1 are treated as 1. (optional) (default to 1)
per_page = 10  # int | Records per page. The server caps page size to 100. Values below 1 use that maximum. (optional) (default to 10)
order_by = "created_at:desc"  # str | Sort by a supported field and direction, using field:asc or field:desc. (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's webhooks
    api_response = accounting.webhooks_api.list_webhooks(
        fields=fields, page=page, per_page=per_page, order_by=order_by
    )
    print("The response of WebhooksApi->list_webhooks:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->list_webhooks: %s\n" % e)


# ..update_webhook
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The webhook uuid
add_webhook_request = (
    accounting_sh.AddWebhookRequest()
)  # AddWebhookRequest | Send a JSON object with the fields below. Fields marked required must be supplied.

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a webhook
    api_response = accounting.webhooks_api.update_webhook(uuid, add_webhook_request)
    print("The response of WebhooksApi->update_webhook:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->update_webhook: %s\n" % e)
