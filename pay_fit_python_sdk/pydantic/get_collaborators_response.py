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

from pay_fit_python_sdk.pydantic.get_collaborators_response_collaborators import GetCollaboratorsResponseCollaborators
from pay_fit_python_sdk.pydantic.get_collaborators_response_meta import GetCollaboratorsResponseMeta

class GetCollaboratorsResponse(BaseModel):
    collaborators: GetCollaboratorsResponseCollaborators = Field(alias='collaborators')

    meta: typing.Optional[GetCollaboratorsResponseMeta] = Field(None, alias='meta')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
