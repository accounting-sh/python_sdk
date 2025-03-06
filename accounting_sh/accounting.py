# coding: utf-8

"""
Accounting API


The version of the OpenAPI document: 7.5.11
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


import datetime
import uuid
from typing import Any
from urllib.parse import urljoin

import requests

from accounting_sh.api.account_connections_api import AccountConnectionsApi
from accounting_sh.api.accounting_codes_api import AccountingCodesApi
from accounting_sh.api.accounts_api import AccountsApi
from accounting_sh.api.attachments_api import AttachmentsApi
from accounting_sh.api.bills_api import BillsApi
from accounting_sh.api.categories_api import CategoriesApi
from accounting_sh.api.companies_api import CompaniesApi
from accounting_sh.api.company_statistics_api import CompanyStatisticsApi
from accounting_sh.api.contacts_api import ContactsApi
from accounting_sh.api.countries_api import CountriesApi
from accounting_sh.api.credentials_api import CredentialsApi
from accounting_sh.api.currency_api import CurrencyApi
from accounting_sh.api.documents_api import DocumentsApi
from accounting_sh.api.expense_reports_api import ExpenseReportsApi
from accounting_sh.api.export_api import ExportApi
from accounting_sh.api.invoices_api import InvoicesApi
from accounting_sh.api.logs_api import LogsApi
from accounting_sh.api.notification_api import NotificationApi
from accounting_sh.api.notification_types_api import NotificationTypesApi
from accounting_sh.api.o_auth_config_api import OAuthConfigApi
from accounting_sh.api.payments_api import PaymentsApi
from accounting_sh.api.quotes_api import QuotesApi
from accounting_sh.api.receipts_api import ReceiptsApi
from accounting_sh.api.revenues_api import RevenuesApi
from accounting_sh.api.rossum_api import RossumApi
from accounting_sh.api.search_api import SearchApi
from accounting_sh.api.settings_api import SettingsApi
from accounting_sh.api.tags_api import TagsApi
from accounting_sh.api.tax_api import TaxApi
from accounting_sh.api.transactions_api import TransactionsApi
from accounting_sh.api.transfers_api import TransfersApi
from accounting_sh.api.vatid_api import VATIDApi
from accounting_sh.api.webhooks_api import WebhooksApi
from accounting_sh.exceptions import ApiException


class Accounting:
    def __init__(
        self,
        token: str,
        url: str = "https://api.accounting.sh",
        throw_errors: bool = True,
    ):
        self.token = token
        self.url = url
        self.throw_errors = throw_errors

    @property
    def account_connections_api(self) -> AccountConnectionsApi:
        """
        :return: AccountConnectionsApi instance
        """
        return AccountConnectionsApi(self)

    @property
    def accounting_codes_api(self) -> AccountingCodesApi:
        """
        :return: AccountingCodesApi instance
        """
        return AccountingCodesApi(self)

    @property
    def accounts_api(self) -> AccountsApi:
        """
        :return: AccountsApi instance
        """
        return AccountsApi(self)

    @property
    def attachments_api(self) -> AttachmentsApi:
        """
        :return: AttachmentsApi instance
        """
        return AttachmentsApi(self)

    @property
    def bills_api(self) -> BillsApi:
        """
        :return: BillsApi instance
        """
        return BillsApi(self)

    @property
    def categories_api(self) -> CategoriesApi:
        """
        :return: CategoriesApi instance
        """
        return CategoriesApi(self)

    @property
    def companies_api(self) -> CompaniesApi:
        """
        :return: CompaniesApi instance
        """
        return CompaniesApi(self)

    @property
    def company_statistics_api(self) -> CompanyStatisticsApi:
        """
        :return: CompanyStatisticsApi instance
        """
        return CompanyStatisticsApi(self)

    @property
    def contacts_api(self) -> ContactsApi:
        """
        :return: ContactsApi instance
        """
        return ContactsApi(self)

    @property
    def countries_api(self) -> CountriesApi:
        """
        :return: CountriesApi instance
        """
        return CountriesApi(self)

    @property
    def credentials_api(self) -> CredentialsApi:
        """
        :return: CredentialsApi instance
        """
        return CredentialsApi(self)

    @property
    def currency_api(self) -> CurrencyApi:
        """
        :return: CurrencyApi instance
        """
        return CurrencyApi(self)

    @property
    def documents_api(self) -> DocumentsApi:
        """
        :return: DocumentsApi instance
        """
        return DocumentsApi(self)

    @property
    def expense_reports_api(self) -> ExpenseReportsApi:
        """
        :return: ExpenseReportsApi instance
        """
        return ExpenseReportsApi(self)

    @property
    def export_api(self) -> ExportApi:
        """
        :return: ExportApi instance
        """
        return ExportApi(self)

    @property
    def invoices_api(self) -> InvoicesApi:
        """
        :return: InvoicesApi instance
        """
        return InvoicesApi(self)

    @property
    def logs_api(self) -> LogsApi:
        """
        :return: LogsApi instance
        """
        return LogsApi(self)

    @property
    def notification_api(self) -> NotificationApi:
        """
        :return: NotificationApi instance
        """
        return NotificationApi(self)

    @property
    def notification_types_api(self) -> NotificationTypesApi:
        """
        :return: NotificationTypesApi instance
        """
        return NotificationTypesApi(self)

    @property
    def o_auth_config_api(self) -> OAuthConfigApi:
        """
        :return: OAuthConfigApi instance
        """
        return OAuthConfigApi(self)

    @property
    def payments_api(self) -> PaymentsApi:
        """
        :return: PaymentsApi instance
        """
        return PaymentsApi(self)

    @property
    def quotes_api(self) -> QuotesApi:
        """
        :return: QuotesApi instance
        """
        return QuotesApi(self)

    @property
    def receipts_api(self) -> ReceiptsApi:
        """
        :return: ReceiptsApi instance
        """
        return ReceiptsApi(self)

    @property
    def revenues_api(self) -> RevenuesApi:
        """
        :return: RevenuesApi instance
        """
        return RevenuesApi(self)

    @property
    def rossum_api(self) -> RossumApi:
        """
        :return: RossumApi instance
        """
        return RossumApi(self)

    @property
    def search_api(self) -> SearchApi:
        """
        :return: SearchApi instance
        """
        return SearchApi(self)

    @property
    def settings_api(self) -> SettingsApi:
        """
        :return: SettingsApi instance
        """
        return SettingsApi(self)

    @property
    def tags_api(self) -> TagsApi:
        """
        :return: TagsApi instance
        """
        return TagsApi(self)

    @property
    def tax_api(self) -> TaxApi:
        """
        :return: TaxApi instance
        """
        return TaxApi(self)

    @property
    def transactions_api(self) -> TransactionsApi:
        """
        :return: TransactionsApi instance
        """
        return TransactionsApi(self)

    @property
    def transfers_api(self) -> TransfersApi:
        """
        :return: TransfersApi instance
        """
        return TransfersApi(self)

    @property
    def vatid_api(self) -> VATIDApi:
        """
        :return: VATIDApi instance
        """
        return VATIDApi(self)

    @property
    def webhooks_api(self) -> WebhooksApi:
        """
        :return: WebhooksApi instance
        """
        return WebhooksApi(self)

    def _serialize(self, data):
        if isinstance(data, list):
            for i in range(len(data)):
                data[i] = self._serialize(data[i])
        elif isinstance(data, dict):
            for key, value in data.items():
                data[key] = self._serialize(value)
        elif isinstance(data, datetime.datetime):
            return data.isoformat()
        elif isinstance(data, datetime.date):
            return data.strftime("%Y-%m-%d")
        elif isinstance(data, uuid.UUID):
            return str(data)

        return data

    def request(
        self, method: str, path: str, comment: str = None, **kwargs
    ) -> Any | None:
        """
        :param method:
        :param path:
        :param comment:
        :param kwargs:
        :return:
        """
        kwargs.setdefault("headers", {})
        kwargs["headers"]["Authorization"] = f"Bearer {self.token}"
        kwargs["headers"]["User-Agent"] = "AccountingSh/0.6.0/python"

        if comment is not None:
            kwargs["headers"]["X-Audit-Comment"] = comment

        if "json" in kwargs:
            kwargs["json"] = self._serialize(kwargs["json"])

        resp = requests.request(method, urljoin(self.url, path), **kwargs)

        if 200 <= resp.status_code <= 300:
            if resp.headers.get("Content-Type") == "application/json":
                return resp.json()
            else:
                return resp.text

        if self.throw_errors:
            raise ApiException(resp.status_code, resp.text, resp.headers)

        return None
