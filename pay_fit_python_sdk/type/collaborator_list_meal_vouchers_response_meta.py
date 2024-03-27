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


class RequiredCollaboratorListMealVouchersResponseMeta(TypedDict):
    pass

class OptionalCollaboratorListMealVouchersResponseMeta(TypedDict, total=False):
    nextPageToken: typing.Optional[str]

    count: typing.Optional[int]

class CollaboratorListMealVouchersResponseMeta(RequiredCollaboratorListMealVouchersResponseMeta, OptionalCollaboratorListMealVouchersResponseMeta):
    pass