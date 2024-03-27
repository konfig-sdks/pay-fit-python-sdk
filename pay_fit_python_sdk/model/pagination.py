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


class Pagination(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class nextPageToken(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    additional_properties = schemas.NotAnyTypeSchema
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs,
                ) -> 'nextPageToken':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class maxResults(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    additional_properties = schemas.NotAnyTypeSchema
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs,
                ) -> 'maxResults':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "nextPageToken": nextPageToken,
                "maxResults": maxResults,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nextPageToken"]) -> MetaOapg.properties.nextPageToken: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxResults"]) -> MetaOapg.properties.maxResults: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["nextPageToken", "maxResults", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nextPageToken"]) -> typing.Union[MetaOapg.properties.nextPageToken, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxResults"]) -> typing.Union[MetaOapg.properties.maxResults, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["nextPageToken", "maxResults", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        nextPageToken: typing.Union[MetaOapg.properties.nextPageToken, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        maxResults: typing.Union[MetaOapg.properties.maxResults, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Pagination':
        return super().__new__(
            cls,
            *args,
            nextPageToken=nextPageToken,
            maxResults=maxResults,
            _configuration=_configuration,
            **kwargs,
        )
