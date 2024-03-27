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

from pay_fit_python_sdk.type.collaborator_get_by_id_response_emails_item import CollaboratorGetByIdResponseEmailsItem

CollaboratorGetByIdResponseEmails = typing.List[CollaboratorGetByIdResponseEmailsItem]