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
)  # RequestBankConnectionRequest |

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
)  # SelectBankAccountRequest |

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
)  # AddAccountingCodeRequest |

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
)  # AddAccountingCodeRequest |

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

add_account_request = accounting_sh.AddAccountRequest()  # AddAccountRequest |

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

fields = "fields_example"  # str | A comma separated list of fields requested in the response (optional)
page = "page_example"  # str | The response page (optional)
per_page = "per_page_example"  # str | The number of items per page (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's accounts
    api_response = accounting.accounts_api.list_accounts(
        fields=fields, page=page, per_page=per_page
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
add_account_request = accounting_sh.AddAccountRequest()  # AddAccountRequest |

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

add_attachment_request = accounting_sh.AddAttachmentRequest()  # AddAttachmentRequest |

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

fields = "fields_example"  # str | A comma separated list of fields requested in the response (optional)
page = "page_example"  # str | The response page (optional)
per_page = "per_page_example"  # str | The number of items per page (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's attachments
    api_response = accounting.attachments_api.list_attachments(
        fields=fields, page=page, per_page=per_page
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
fields = "fields_example"  # str | A comma separated list of fields requested in the response (optional)
page = "page_example"  # str | The response page (optional)
per_page = "per_page_example"  # str | The number of items per page (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's attachments link to resource
    api_response = accounting.attachments_api.retrieve_attachments(
        resource, fields=fields, page=page, per_page=per_page
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
add_attachment_request = accounting_sh.AddAttachmentRequest()  # AddAttachmentRequest |

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

login_request = accounting_sh.LoginRequest()  # LoginRequest |

accounting = accounting_sh.Accounting("access_token")
try:
    # Login user
    api_response = accounting.auth_api.login(login_request)
    print("The response of AuthApi->login:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->login: %s\n" % e)


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

switch_company_request = accounting_sh.SwitchCompanyRequest()  # SwitchCompanyRequest |

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

add_bill_request = accounting_sh.AddBillRequest()  # AddBillRequest |

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
)  # AddBillPaymentRequest |

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
    accounting.bills_api.get_bill_document(uuid)
except ApiException as e:
    print("Exception when calling BillsApi->get_bill_document: %s\n" % e)


# ..list_bills
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = "fields_example"  # str | A comma separated list of fields requested in the response (optional)
page = "page_example"  # str | The response page (optional)
per_page = "per_page_example"  # str | The number of items per page (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's bills
    api_response = accounting.bills_api.list_bills(
        fields=fields, page=page, per_page=per_page
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
add_bill_request = accounting_sh.AddBillRequest()  # AddBillRequest |

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a bill
    api_response = accounting.bills_api.update_bill(uuid, add_bill_request)
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
)  # AddBillPaymentRequest |

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

add_category_request = accounting_sh.AddCategoryRequest()  # AddCategoryRequest |

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

fields = "fields_example"  # str | A comma separated list of fields requested in the response (optional)
page = "page_example"  # str | The response page (optional)
per_page = "per_page_example"  # str | The number of items per page (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's categories
    api_response = accounting.categories_api.list_categories(
        fields=fields, page=page, per_page=per_page
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
add_category_request = accounting_sh.AddCategoryRequest()  # AddCategoryRequest |

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

add_company_request = accounting_sh.AddCompanyRequest()  # AddCompanyRequest |

accounting = accounting_sh.Accounting("access_token")
try:
    # Add a company
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

uuid = "uuid_example"  # str | The company uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # List a company's feature set
    api_response = accounting.companies_api.get_company_feature_set(uuid)
    print("The response of CompaniesApi->get_company_feature_set:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompaniesApi->get_company_feature_set: %s\n" % e)


# ..list_companies
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = "fields_example"  # str | A comma separated list of fields requested in the response (optional)
page = "page_example"  # str | The response page (optional)
per_page = "per_page_example"  # str | The number of items per page (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List companies on this instance
    api_response = accounting.companies_api.list_companies(
        fields=fields, page=page, per_page=per_page
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
add_company_request = accounting_sh.AddCompanyRequest()  # AddCompanyRequest |

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a company
    api_response = accounting.companies_api.update_company(uuid, add_company_request)
    print("The response of CompaniesApi->update_company:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompaniesApi->update_company: %s\n" % e)


# ..get_statistics
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The company uuid
start = "start_example"  # str | Start date (optional)
end = "end_example"  # str | End date (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # Get company's statistic
    api_response = accounting.company_statistics_api.get_statistics(
        uuid, start=start, end=end
    )
    print("The response of CompanyStatisticsApi->get_statistics:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyStatisticsApi->get_statistics: %s\n" % e)


# ..add_contact
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_contact_request = accounting_sh.AddContactRequest()  # AddContactRequest |

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

uuid = "uuid_example"  # str | The contact uuid (optional)
fields = "fields_example"  # str | A comma separated list of fields requested in the response (optional)
page = "page_example"  # str | The response page (optional)
per_page = "per_page_example"  # str | The number of items per page (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List a contact's bills
    api_response = accounting.contacts_api.list_contact_bills(
        uuid=uuid, fields=fields, page=page, per_page=per_page
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
fields = "fields_example"  # str | A comma separated list of fields requested in the response (optional)
page = "page_example"  # str | The response page (optional)
per_page = "per_page_example"  # str | The number of items per page (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List a contact's invoices
    api_response = accounting.contacts_api.list_contact_invoices(
        uuid, fields=fields, page=page, per_page=per_page
    )
    print("The response of ContactsApi->list_contact_invoices:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->list_contact_invoices: %s\n" % e)


# ..list_contacts
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = "fields_example"  # str | A comma separated list of fields requested in the response (optional)
page = "page_example"  # str | The response page (optional)
per_page = "per_page_example"  # str | The number of items per page (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's contacts
    api_response = accounting.contacts_api.list_contacts(
        fields=fields, page=page, per_page=per_page
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
add_contact_request = accounting_sh.AddContactRequest()  # AddContactRequest |

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

add_credential_request = accounting_sh.AddCredentialRequest()  # AddCredentialRequest |

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

fields = "fields_example"  # str | A comma separated list of fields requested in the response (optional)
page = "page_example"  # str | The response page (optional)
per_page = "per_page_example"  # str | The number of items per page (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's credentials
    api_response = accounting.credentials_api.list_credentials(
        fields=fields, page=page, per_page=per_page
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
add_credential_request = accounting_sh.AddCredentialRequest()  # AddCredentialRequest |

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


# ..userveria
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint


accounting = accounting_sh.Accounting("access_token")
try:
    # Exchange a my stantabcorp (userveria) token for an Accounting Token
    api_response = accounting.credentials_api.userveria()
    print("The response of CredentialsApi->userveria:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->userveria: %s\n" % e)


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


# ..cancel_review
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The document uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Cancel document review
    api_response = accounting.documents_api.cancel_review(uuid)
    print("The response of DocumentsApi->cancel_review:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->cancel_review: %s\n" % e)


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

fields = "fields_example"  # str | A comma separated list of fields requested in the response (optional)
page = "page_example"  # str | The response page (optional)
per_page = "per_page_example"  # str | The number of items per page (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's documents
    api_response = accounting.documents_api.list_documents(
        fields=fields, page=page, per_page=per_page
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


# ..review_url
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The document uuid

accounting = accounting_sh.Accounting("access_token")
try:
    # Get url to review a document
    api_response = accounting.documents_api.review_url(uuid)
    print("The response of DocumentsApi->review_url:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->review_url: %s\n" % e)


# ..update_document
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The document uuid
update_document_request = (
    accounting_sh.UpdateDocumentRequest()
)  # UpdateDocumentRequest |

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

name = "name_example"  # str |
file = None  # bytearray |

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
)  # AddExpenseReportRequest |

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

fields = "fields_example"  # str | A comma separated list of fields requested in the response (optional)
page = "page_example"  # str | The response page (optional)
per_page = "per_page_example"  # str | The number of items per page (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's expense reports.
    api_response = accounting.expense_reports_api.list_expense_reports(
        fields=fields, page=page, per_page=per_page
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
)  # SendExpenseReportLoginEmailRequest |

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
)  # AddExpenseReportRequest |

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
)  # UpdateExpenseReportAccountRequest |

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
)  # UpdateExpenseReportSettingsRequest |

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
)  # VerifyExpenseReportSettingsRequest |

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

fields = "fields_example"  # str | A comma separated list of fields requested in the response (optional)
page = "page_example"  # str | The response page (optional)
per_page = "per_page_example"  # str | The number of items per page (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's exports
    api_response = accounting.export_api.list_exports(
        fields=fields, page=page, per_page=per_page
    )
    print("The response of ExportApi->list_exports:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportApi->list_exports: %s\n" % e)


# ..request_export
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

request_export_request = accounting_sh.RequestExportRequest()  # RequestExportRequest |

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

add_invoice_request = accounting_sh.AddInvoiceRequest()  # AddInvoiceRequest |

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
)  # AddBillPaymentRequest |

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
    accounting.invoices_api.get_invoice_document(uuid)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_invoice_document: %s\n" % e)


# ..list_invoices
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = "fields_example"  # str | A comma separated list of fields requested in the response (optional)
page = "page_example"  # str | The response page (optional)
per_page = "per_page_example"  # str | The number of items per page (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's invoices
    api_response = accounting.invoices_api.list_invoices(
        fields=fields, page=page, per_page=per_page
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
add_invoice_request = accounting_sh.AddInvoiceRequest()  # AddInvoiceRequest |

accounting = accounting_sh.Accounting("access_token")
try:
    # Update an invoice
    api_response = accounting.invoices_api.update_invoice(uuid, add_invoice_request)
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
)  # AddBillPaymentRequest |

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


# ..logs
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = "fields_example"  # str | A comma separated list of fields requested in the response (optional)
page = "page_example"  # str | The response page (optional)
per_page = "per_page_example"  # str | The number of items per page (optional)
channel = "channel_example"  # str | The channel to retrieve the logs from (optional)
level = "level_example"  # str | The log level to retrieve (optional)
resource = "resource_example"  # str | Retrive logs linked to that resource (optional)
before = "before_example"  # str | Retrive logs before the provided date (optional)
after = "after_example"  # str | Retrive logs after the provided date (optional)
format = "format_example"  # str | In which format to retrieve the logs, available: json or txt (optional)

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

fields = "fields_example"  # str | A comma separated list of fields requested in the response (optional)
page = "page_example"  # str | The response page (optional)
per_page = "per_page_example"  # str | The number of items per page (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's notifications
    api_response = accounting.notification_api.list_notifications(
        fields=fields, page=page, per_page=per_page
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
)  # SendNotificationRequest |

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
)  # UpdateNotificationPreferencesRequest |

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
)  # AddNotificationTypeRequest |

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

fields = "fields_example"  # str | A comma separated list of fields requested in the response (optional)
page = "page_example"  # str | The response page (optional)
per_page = "per_page_example"  # str | The number of items per page (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's notification types
    api_response = accounting.notification_types_api.list_notification_types(
        fields=fields, page=page, per_page=per_page
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
add_notification_type_request = (
    accounting_sh.AddNotificationTypeRequest()
)  # AddNotificationTypeRequest |

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a notification type
    api_response = accounting.notification_types_api.update_notification_type(
        uuid, add_notification_type_request
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
)  # AddOAuthConfigurationRequest |

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

fields = "fields_example"  # str | A comma separated list of fields requested in the response (optional)
page = "page_example"  # str | The response page (optional)
per_page = "per_page_example"  # str | The number of items per page (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's oauth configurations
    api_response = accounting.o_auth_config_api.list_o_auth_configurations(
        fields=fields, page=page, per_page=per_page
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
)  # AddOAuthConfigurationRequest |

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

add_payment_request = accounting_sh.AddPaymentRequest()  # AddPaymentRequest |

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

fields = "fields_example"  # str | A comma separated list of fields requested in the response (optional)
page = "page_example"  # str | The response page (optional)
per_page = "per_page_example"  # str | The number of items per page (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's payments
    api_response = accounting.payments_api.list_payments(
        fields=fields, page=page, per_page=per_page
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
add_payment_request = accounting_sh.AddPaymentRequest()  # AddPaymentRequest |

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

add_quote_request = accounting_sh.AddQuoteRequest()  # AddQuoteRequest |

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
    accounting.quotes_api.get_quote_document(uuid)
except ApiException as e:
    print("Exception when calling QuotesApi->get_quote_document: %s\n" % e)


# ..list_quotes
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = "fields_example"  # str | A comma separated list of fields requested in the response (optional)
page = "page_example"  # str | The response page (optional)
per_page = "per_page_example"  # str | The number of items per page (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's quotes
    api_response = accounting.quotes_api.list_quotes(
        fields=fields, page=page, per_page=per_page
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
add_quote_request = accounting_sh.AddQuoteRequest()  # AddQuoteRequest |

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a quote
    api_response = accounting.quotes_api.update_quote(uuid, add_quote_request)
    print("The response of QuotesApi->update_quote:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotesApi->update_quote: %s\n" % e)


# ..add_receipt
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_receipt_request = accounting_sh.AddReceiptRequest()  # AddReceiptRequest |

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
    accounting.receipts_api.get_receipt_document(uuid)
except ApiException as e:
    print("Exception when calling ReceiptsApi->get_receipt_document: %s\n" % e)


# ..list_receipts
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = "fields_example"  # str | A comma separated list of fields requested in the response (optional)
page = "page_example"  # str | The response page (optional)
per_page = "per_page_example"  # str | The number of items per page (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's receipts
    api_response = accounting.receipts_api.list_receipts(
        fields=fields, page=page, per_page=per_page
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
add_receipt_request = accounting_sh.AddReceiptRequest()  # AddReceiptRequest |

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a receipt
    api_response = accounting.receipts_api.update_receipt(uuid, add_receipt_request)
    print("The response of ReceiptsApi->update_receipt:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceiptsApi->update_receipt: %s\n" % e)


# ..add_revenue
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_revenue_request = accounting_sh.AddRevenueRequest()  # AddRevenueRequest |

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

fields = "fields_example"  # str | A comma separated list of fields requested in the response (optional)
page = "page_example"  # str | The response page (optional)
per_page = "per_page_example"  # str | The number of items per page (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's revenues
    api_response = accounting.revenues_api.list_revenues(
        fields=fields, page=page, per_page=per_page
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
add_revenue_request = accounting_sh.AddRevenueRequest()  # AddRevenueRequest |

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

fields = "fields_example"  # str | A comma separated list of fields requested in the response (optional)
page = "page_example"  # str | The response page (optional)
per_page = "per_page_example"  # str | The number of items per page (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List documents to be reviewed
    api_response = accounting.rossum_api.list_reviews(
        fields=fields, page=page, per_page=per_page
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

fields = "fields_example"  # str | A comma separated list of fields requested in the response (optional)
page = "page_example"  # str | The response page (optional)
per_page = "per_page_example"  # str | The number of items per page (optional)
uuid = "uuid_example"  # str | The company uuid (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's settings
    api_response = accounting.settings_api.list_settings(
        fields=fields, page=page, per_page=per_page, uuid=uuid
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
)  # UpdateSettingsRequest |

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


# ..add_tag
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_tag_request = accounting_sh.AddTagRequest()  # AddTagRequest |

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

fields = "fields_example"  # str | A comma separated list of fields requested in the response (optional)
page = "page_example"  # str | The response page (optional)
per_page = "per_page_example"  # str | The number of items per page (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's tags
    api_response = accounting.tags_api.list_tags(
        fields=fields, page=page, per_page=per_page
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
fields = "fields_example"  # str | A comma separated list of fields requested in the response (optional)
page = "page_example"  # str | The response page (optional)
per_page = "per_page_example"  # str | The number of items per page (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's tags by resource attachment
    api_response = accounting.tags_api.list_tags_by_resource(
        resource, fields=fields, page=page, per_page=per_page
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
add_tag_request = accounting_sh.AddTagRequest()  # AddTagRequest |

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

list_links200_response_links_inner = (
    accounting_sh.ListLinks200ResponseLinksInner()
)  # ListLinks200ResponseLinksInner |
uuid = "uuid_example"  # str | A transaction uuid (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # Add a new transaction link
    api_response = accounting.transactions_api.add_link(
        list_links200_response_links_inner, uuid=uuid
    )
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
)  # AddTransactionRequest |

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
update_transaction_code_request = (
    accounting_sh.UpdateTransactionCodeRequest()
)  # UpdateTransactionCodeRequest |

accounting = accounting_sh.Accounting("access_token")
try:
    # Add a transaction's code
    api_response = accounting.transactions_api.add_transaction_code(
        uuid, update_transaction_code_request
    )
    print("The response of TransactionsApi->add_transaction_code:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->add_transaction_code: %s\n" % e)


# ..delete_link
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | A transaction uuid (optional)
link_uuid = (
    "link_uuid_example"  # str | A transaction link uuid OR the target uuid (optional)
)

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete a transaction link
    api_response = accounting.transactions_api.delete_link(
        uuid=uuid, link_uuid=link_uuid
    )
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
)  # ImportTransactionsRequest |

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

fields = "fields_example"  # str | A comma separated list of fields requested in the response (optional)
page = "page_example"  # str | The response page (optional)
per_page = "per_page_example"  # str | The number of items per page (optional)
account = "account_example"  # str | An account uuid to filter results (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's transactions and transfers
    api_response = accounting.transactions_api.ledger(
        fields=fields, page=page, per_page=per_page, account=account
    )
    print("The response of TransactionsApi->ledger:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->ledger: %s\n" % e)


# ..list_links
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = "fields_example"  # str | A comma separated list of fields requested in the response (optional)
page = "page_example"  # str | The response page (optional)
per_page = "per_page_example"  # str | The number of items per page (optional)
uuid = "uuid_example"  # str | A transaction uuid (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List a transaction links
    api_response = accounting.transactions_api.list_links(
        fields=fields, page=page, per_page=per_page, uuid=uuid
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
fields = "fields_example"  # str | A comma separated list of fields requested in the response (optional)
page = "page_example"  # str | The response page (optional)
per_page = "per_page_example"  # str | The number of items per page (optional)
account = "account_example"  # str | List to the specified account (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List transaction's codes
    api_response = accounting.transactions_api.list_transaction_codes(
        uuid, fields=fields, page=page, per_page=per_page, account=account
    )
    print("The response of TransactionsApi->list_transaction_codes:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->list_transaction_codes: %s\n" % e)


# ..list_transactions
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = "fields_example"  # str | A comma separated list of fields requested in the response (optional)
page = "page_example"  # str | The response page (optional)
per_page = "per_page_example"  # str | The number of items per page (optional)
account = "account_example"  # str | List to the specified account (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's transactions
    api_response = accounting.transactions_api.list_transactions(
        fields=fields, page=page, per_page=per_page, account=account
    )
    print("The response of TransactionsApi->list_transactions:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->list_transactions: %s\n" % e)


# ..update_link
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

list_links200_response_links_inner = (
    accounting_sh.ListLinks200ResponseLinksInner()
)  # ListLinks200ResponseLinksInner |
uuid = "uuid_example"  # str | A transaction uuid (optional)
link_uuid = (
    "link_uuid_example"  # str | A transaction link uuid OR the target uuid (optional)
)

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a transaction link
    api_response = accounting.transactions_api.update_link(
        list_links200_response_links_inner, uuid=uuid, link_uuid=link_uuid
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
)  # AddTransactionRequest |

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
update_transaction_code_request = (
    accounting_sh.UpdateTransactionCodeRequest()
)  # UpdateTransactionCodeRequest |

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a transaction's code
    api_response = accounting.transactions_api.update_transaction_code(
        uuid, update_transaction_code_request
    )
    print("The response of TransactionsApi->update_transaction_code:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->update_transaction_code: %s\n" % e)


# ..view_link
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | A transaction uuid (optional)
link_uuid = (
    "link_uuid_example"  # str | A transaction link uuid OR the target uuid (optional)
)

accounting = accounting_sh.Accounting("access_token")
try:
    # View a transaction link
    api_response = accounting.transactions_api.view_link(uuid=uuid, link_uuid=link_uuid)
    print("The response of TransactionsApi->view_link:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->view_link: %s\n" % e)


# ..add_transfer
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_transfer_request = accounting_sh.AddTransferRequest()  # AddTransferRequest |

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

fields = "fields_example"  # str | A comma separated list of fields requested in the response (optional)
page = "page_example"  # str | The response page (optional)
per_page = "per_page_example"  # str | The number of items per page (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's transfers
    api_response = accounting.transfers_api.list_transfers(
        fields=fields, page=page, per_page=per_page
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
add_transfer_request = accounting_sh.AddTransferRequest()  # AddTransferRequest |

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

add_user_request = accounting_sh.AddUserRequest()  # AddUserRequest |

accounting = accounting_sh.Accounting("access_token")
try:
    # Add user
    api_response = accounting.users_api.add_user(add_user_request)
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

fields = "fields_example"  # str | A comma separated list of fields requested in the response (optional)
page = "page_example"  # str | The response page (optional)
per_page = "per_page_example"  # str | The number of items per page (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's users
    api_response = accounting.users_api.list_users(
        fields=fields, page=page, per_page=per_page
    )
    print("The response of UsersApi->list_users:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->list_users: %s\n" % e)


# ..update_user
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The user uuid
update_user_request = accounting_sh.UpdateUserRequest()  # UpdateUserRequest |

accounting = accounting_sh.Accounting("access_token")
try:
    # Update user
    api_response = accounting.users_api.update_user(uuid, update_user_request)
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

add_company_vat_id_request = (
    accounting_sh.AddCompanyVatIdRequest()
)  # AddCompanyVatIdRequest |
uuid = "uuid_example"  # str | The company uuid (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # Add a company's Vat Id
    api_response = accounting.vatid_api.add_company_vat_id(
        add_company_vat_id_request, uuid=uuid
    )
    print("The response of VATIDApi->add_company_vat_id:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VATIDApi->add_company_vat_id: %s\n" % e)


# ..delete_company_vat_id
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

key = "key_example"  # str | The VAT ID uuid
uuid = "uuid_example"  # str | The company uuid (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete a company's Vat Id
    api_response = accounting.vatid_api.delete_company_vat_id(key, uuid=uuid)
    print("The response of VATIDApi->delete_company_vat_id:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VATIDApi->delete_company_vat_id: %s\n" % e)


# ..get_company_vat_id
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

key = "key_example"  # str | The VAT ID uuid
uuid = "uuid_example"  # str | The company uuid (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a company's Vat Id
    api_response = accounting.vatid_api.get_company_vat_id(key, uuid=uuid)
    print("The response of VATIDApi->get_company_vat_id:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VATIDApi->get_company_vat_id: %s\n" % e)


# ..list_company_vat_id
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

fields = "fields_example"  # str | A comma separated list of fields requested in the response (optional)
page = "page_example"  # str | The response page (optional)
per_page = "per_page_example"  # str | The number of items per page (optional)
uuid = "uuid_example"  # str | The company uuid (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's Vat Id
    api_response = accounting.vatid_api.list_company_vat_id(
        fields=fields, page=page, per_page=per_page, uuid=uuid
    )
    print("The response of VATIDApi->list_company_vat_id:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VATIDApi->list_company_vat_id: %s\n" % e)


# ..update_company_vat_id
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

key = "key_example"  # str | The VAT ID uuid
add_company_vat_id_request = (
    accounting_sh.AddCompanyVatIdRequest()
)  # AddCompanyVatIdRequest |
uuid = "uuid_example"  # str | The company uuid (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a company's Vat Id
    api_response = accounting.vatid_api.update_company_vat_id(
        key, add_company_vat_id_request, uuid=uuid
    )
    print("The response of VATIDApi->update_company_vat_id:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VATIDApi->update_company_vat_id: %s\n" % e)


# ..add_webhook
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_webhook_request = accounting_sh.AddWebhookRequest()  # AddWebhookRequest |

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

uuid = "uuid_example"  # str | The webhook uuid (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # Delete a webhook
    api_response = accounting.webhooks_api.delete_webhook(uuid=uuid)
    print("The response of WebhooksApi->delete_webhook:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->delete_webhook: %s\n" % e)


# ..get_webhook
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The webhook uuid (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # Get a webhook
    api_response = accounting.webhooks_api.get_webhook(uuid=uuid)
    print("The response of WebhooksApi->get_webhook:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->get_webhook: %s\n" % e)


# ..get_webhook_history
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

uuid = "uuid_example"  # str | The webhook uuid (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # Get webhook's history
    api_response = accounting.webhooks_api.get_webhook_history(uuid=uuid)
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

fields = "fields_example"  # str | A comma separated list of fields requested in the response (optional)
page = "page_example"  # str | The response page (optional)
per_page = "per_page_example"  # str | The number of items per page (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # List company's webhooks
    api_response = accounting.webhooks_api.list_webhooks(
        fields=fields, page=page, per_page=per_page
    )
    print("The response of WebhooksApi->list_webhooks:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->list_webhooks: %s\n" % e)


# ..update_webhook
import accounting_sh
from accounting_sh.exceptions import ApiException
from pprint import pprint

add_webhook_request = accounting_sh.AddWebhookRequest()  # AddWebhookRequest |
uuid = "uuid_example"  # str | The webhook uuid (optional)

accounting = accounting_sh.Accounting("access_token")
try:
    # Update a webhook
    api_response = accounting.webhooks_api.update_webhook(
        add_webhook_request, uuid=uuid
    )
    print("The response of WebhooksApi->update_webhook:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->update_webhook: %s\n" % e)
