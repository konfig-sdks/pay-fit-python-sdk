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


class RequiredGetCompanyResponse(TypedDict):
    # Id of the company.
    id: str

    # Name of the company.
    name: str

    # Country of the company.
    country: str

    # Number of current active contracts within the company.
    nbActiveContracts: int

class OptionalGetCompanyResponse(TypedDict, total=False):
    pass

class GetCompanyResponse(RequiredGetCompanyResponse, OptionalGetCompanyResponse):
    pass
