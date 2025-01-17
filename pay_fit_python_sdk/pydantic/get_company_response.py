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


class GetCompanyResponse(BaseModel):
    # Id of the company.
    id: str = Field(alias='id')

    # Name of the company.
    name: str = Field(alias='name')

    # Country of the company.
    country: Literal["FR", "ES", "DE", "GB", "IT"] = Field(alias='country')

    # Number of current active contracts within the company.
    nb_active_contracts: int = Field(alias='nbActiveContracts')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
