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


class RequiredCollaboratorListMealVouchers403Response(TypedDict):
    # A human readable error
    error: str

class OptionalCollaboratorListMealVouchers403Response(TypedDict, total=False):
    details: typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]

class CollaboratorListMealVouchers403Response(RequiredCollaboratorListMealVouchers403Response, OptionalCollaboratorListMealVouchers403Response):
    pass
