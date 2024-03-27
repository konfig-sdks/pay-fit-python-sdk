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


class RequiredCollaboratorEmailsItem(TypedDict):
    # Email of the collaborator.
    email: str

    # Indicates whether this is a personal or a professional email.
    type: str

class OptionalCollaboratorEmailsItem(TypedDict, total=False):
    pass

class CollaboratorEmailsItem(RequiredCollaboratorEmailsItem, OptionalCollaboratorEmailsItem):
    pass
