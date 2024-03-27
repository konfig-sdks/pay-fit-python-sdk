# coding: utf-8

"""
    Partner API

    A Semi-Private API to let third parties communicate with PayFit

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from pay_fit_python_sdk import schemas  # noqa: F401


class CollaboratorEmails(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    List of emails of the collaborator.
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['CollaboratorEmailsItem']:
            return CollaboratorEmailsItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['CollaboratorEmailsItem'], typing.List['CollaboratorEmailsItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'CollaboratorEmails':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'CollaboratorEmailsItem':
        return super().__getitem__(i)

from pay_fit_python_sdk.model.collaborator_emails_item import CollaboratorEmailsItem
