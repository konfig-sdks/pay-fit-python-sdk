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

from pay_fit_python_sdk.pydantic.contract_list_worked_time_by_pay_period_response_contracts import ContractListWorkedTimeByPayPeriodResponseContracts
from pay_fit_python_sdk.pydantic.contract_list_worked_time_by_pay_period_response_meta import ContractListWorkedTimeByPayPeriodResponseMeta

class ContractListWorkedTimeByPayPeriodResponse(BaseModel):
    contracts: ContractListWorkedTimeByPayPeriodResponseContracts = Field(alias='contracts')

    meta: ContractListWorkedTimeByPayPeriodResponseMeta = Field(alias='meta')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
