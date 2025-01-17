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

from pay_fit_python_sdk.pydantic.get_collaborators_response_collaborators_item_addresses_item import GetCollaboratorsResponseCollaboratorsItemAddressesItem

GetCollaboratorsResponseCollaboratorsItemAddresses = typing.List[GetCollaboratorsResponseCollaboratorsItemAddressesItem]
