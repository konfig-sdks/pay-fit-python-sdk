# coding: utf-8

"""
    Partner API

    A Semi-Private API to let third parties communicate with PayFit

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING


class RequiredGetCompanyAccountingV2ResponseItem(TypedDict):
    # Date of accounting operation.
    operationDate: date

    # The analyticCode allows to group operation by label.
    analyticCode: typing.Optional[str]

    # The fullname of the concerned employee.
    employeeFullName: str

    # Refers to an account's unique numerical identifier in an accounting system.
    accountId: str

    # Represents the textual description of the account.
    accountName: str

    # Amount of the debit operation.
    debit: typing.Optional[typing.Union[int, float]]

    # Amount of the credit operation.
    credit: typing.Optional[typing.Union[int, float]]

class OptionalGetCompanyAccountingV2ResponseItem(TypedDict, total=False):
    pass

class GetCompanyAccountingV2ResponseItem(RequiredGetCompanyAccountingV2ResponseItem, OptionalGetCompanyAccountingV2ResponseItem):
    pass
