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


class RequiredTimeInformation(TypedDict):
    # Weekly hours defined in the contract. It will be available if `contracts:time-information:read` scope is set on the token.
    standardWeeklyHours: typing.Optional[typing.Union[int, float]]

    # Percentage of weekly hours in the contract. It will be available if `contracts:time-information:read` scope is set on the token.
    fullTimeEquivalent: typing.Optional[typing.Union[int, float]]

    # Will be set to `true` if `fullTimeEquivalent` is at 1. It will be available if `contracts:time-information:read` scope is set on the token.
    isFullTime: typing.Optional[bool]

class OptionalTimeInformation(TypedDict, total=False):
    pass

class TimeInformation(RequiredTimeInformation, OptionalTimeInformation):
    pass
