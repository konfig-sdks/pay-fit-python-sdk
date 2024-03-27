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


class CollaboratorGetByIdResponsePhoneNumbersItem(BaseModel):
    # Phone number of the collaborator.
    phone_number: str = Field(alias='phoneNumber')

    # Type of the phone number.
    type: Literal["personal"] = Field(alias='type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
