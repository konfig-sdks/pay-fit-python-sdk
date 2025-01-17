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


class RequiredGetCompanyPayrollStatusResponse(TypedDict):
    # The payroll status
    status: str

    # End execution date of the last payroll for the given month.
    executionEndDate: typing.Optional[datetime]

class OptionalGetCompanyPayrollStatusResponse(TypedDict, total=False):
    pass

class GetCompanyPayrollStatusResponse(RequiredGetCompanyPayrollStatusResponse, OptionalGetCompanyPayrollStatusResponse):
    pass
