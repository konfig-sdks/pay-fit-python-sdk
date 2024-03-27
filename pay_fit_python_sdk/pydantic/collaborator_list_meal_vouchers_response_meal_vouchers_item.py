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
from pydantic import BaseModel, Field, RootModel, ConfigDict


class CollaboratorListMealVouchersResponseMealVouchersItem(BaseModel):
    # Id of the collaborator.
    collaborator_id: str = Field(alias='collaboratorId')

    # Represents the number of days a collaborator worked during the month and for which he/she should receive meal vouchers.
    vouchers_count: typing.Union[int, float] = Field(alias='vouchersCount')

    # Represents the amount of a single meal voucher.
    voucher_amount: typing.Union[int, float] = Field(alias='voucherAmount')

    # Defines if the voucher can be used to pay a meal on a sunday and on a bank holiday or not.
    day_off_eligibility: bool = Field(alias='dayOffEligibility')

    # Represents the company part amount of a single meal voucher.
    voucher_company_part_amount: typing.Union[int, float] = Field(alias='voucherCompanyPartAmount')

    # Represents the employee part amount of a single meal voucher.
    voucher_employee_part_amount: typing.Union[int, float] = Field(alias='voucherEmployeePartAmount')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
