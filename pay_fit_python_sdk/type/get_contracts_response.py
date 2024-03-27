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

from pay_fit_python_sdk.type.get_contracts_response_contracts import GetContractsResponseContracts
from pay_fit_python_sdk.type.get_contracts_response_meta import GetContractsResponseMeta

class RequiredGetContractsResponse(TypedDict):
    pass

class OptionalGetContractsResponse(TypedDict, total=False):
    contracts: GetContractsResponseContracts

    meta: GetContractsResponseMeta

class GetContractsResponse(RequiredGetContractsResponse, OptionalGetContractsResponse):
    pass
