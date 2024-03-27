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


class CollaboratorGetByIdResponsePhoneNumbers(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    List of phone numbers of the collaborator. Personal phone number will be available if `collaborators:personal:read` scope is set on the token.
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['CollaboratorGetByIdResponsePhoneNumbersItem']:
            return CollaboratorGetByIdResponsePhoneNumbersItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['CollaboratorGetByIdResponsePhoneNumbersItem'], typing.List['CollaboratorGetByIdResponsePhoneNumbersItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'CollaboratorGetByIdResponsePhoneNumbers':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'CollaboratorGetByIdResponsePhoneNumbersItem':
        return super().__getitem__(i)

from pay_fit_python_sdk.model.collaborator_get_by_id_response_phone_numbers_item import CollaboratorGetByIdResponsePhoneNumbersItem
