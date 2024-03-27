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


class Company(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "country",
            "name",
            "nbActiveContracts",
            "id",
        }
        
        class properties:
            id = schemas.StrSchema
            name = schemas.StrSchema
            
            
            class country(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "FR": "FR",
                        "ES": "ES",
                        "DE": "DE",
                        "GB": "GB",
                        "IT": "IT",
                    }
                
                @schemas.classproperty
                def FR(cls):
                    return cls("FR")
                
                @schemas.classproperty
                def ES(cls):
                    return cls("ES")
                
                @schemas.classproperty
                def DE(cls):
                    return cls("DE")
                
                @schemas.classproperty
                def GB(cls):
                    return cls("GB")
                
                @schemas.classproperty
                def IT(cls):
                    return cls("IT")
            nbActiveContracts = schemas.IntSchema
            __annotations__ = {
                "id": id,
                "name": name,
                "country": country,
                "nbActiveContracts": nbActiveContracts,
            }
    
    country: MetaOapg.properties.country
    name: MetaOapg.properties.name
    nbActiveContracts: MetaOapg.properties.nbActiveContracts
    id: MetaOapg.properties.id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country"]) -> MetaOapg.properties.country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nbActiveContracts"]) -> MetaOapg.properties.nbActiveContracts: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "country", "nbActiveContracts", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country"]) -> MetaOapg.properties.country: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nbActiveContracts"]) -> MetaOapg.properties.nbActiveContracts: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "country", "nbActiveContracts", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        country: typing.Union[MetaOapg.properties.country, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        nbActiveContracts: typing.Union[MetaOapg.properties.nbActiveContracts, decimal.Decimal, int, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Company':
        return super().__new__(
            cls,
            *args,
            country=country,
            name=name,
            nbActiveContracts=nbActiveContracts,
            id=id,
            _configuration=_configuration,
            **kwargs,
        )