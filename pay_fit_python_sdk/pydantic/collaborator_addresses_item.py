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


class CollaboratorAddressesItem(BaseModel):
    # Address of the collaborator containing the streetNumber, streetType and streetName.
    address: str = Field(alias='address')

    # Postcode of the collaborator's address.
    postcode: str = Field(alias='postcode')

    # City of the collaborator's address.
    city: str = Field(alias='city')

    # Type of the address.
    type: Literal["personal"] = Field(alias='type')

    # Country of the collaborator's address.
    country: typing.Optional[str] = Field(None, alias='country')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
