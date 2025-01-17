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


class RequiredCollaboratorListMealVouchersResponseMealVouchersItem(TypedDict):
    # Id of the collaborator.
    collaboratorId: str

    # Represents the number of days a collaborator worked during the month and for which he/she should receive meal vouchers.
    vouchersCount: typing.Union[int, float]

    # Represents the amount of a single meal voucher.
    voucherAmount: typing.Union[int, float]

    # Defines if the voucher can be used to pay a meal on a sunday and on a bank holiday or not.
    dayOffEligibility: bool

    # Represents the company part amount of a single meal voucher.
    voucherCompanyPartAmount: typing.Union[int, float]

    # Represents the employee part amount of a single meal voucher.
    voucherEmployeePartAmount: typing.Union[int, float]

class OptionalCollaboratorListMealVouchersResponseMealVouchersItem(TypedDict, total=False):
    pass

class CollaboratorListMealVouchersResponseMealVouchersItem(RequiredCollaboratorListMealVouchersResponseMealVouchersItem, OptionalCollaboratorListMealVouchersResponseMealVouchersItem):
    pass
