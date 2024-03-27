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


class CollaboratorContract(BaseModel):
    # Id of the contract.
    id: str = Field(alias='id')

    # Start date of a contract in the format YYYY-MM-DD.
    start_date: typing.Optional[date] = Field(alias='startDate')

    # End date of a contract in the format YYYY-MM-DD.
    end_date: typing.Optional[date] = Field(alias='endDate')

    # The status of the contract.
    status: Literal["ACTIVE", "ARCHIVED", "PENDING"] = Field(alias='status')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
