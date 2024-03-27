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


class ContractListWorkedTimeByPayPeriodResponseContracts(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        
        class items(
            schemas.ComposedSchema,
        ):
        
        
            class MetaOapg:
                
                
                class all_of_0(
                    schemas.DictSchema
                ):
                
                
                    class MetaOapg:
                        required = {
                            "payedWorkedTime",
                            "workTimeUnit",
                            "effectiveWorkedTime",
                        }
                        
                        class properties:
                            
                            
                            class effectiveWorkedTime(
                                schemas.NumberBase,
                                schemas.NoneBase,
                                schemas.Schema,
                                schemas.NoneDecimalMixin
                            ):
                            
                            
                                def __new__(
                                    cls,
                                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                ) -> 'effectiveWorkedTime':
                                    return super().__new__(
                                        cls,
                                        *args,
                                        _configuration=_configuration,
                                    )
                            
                            
                            class payedWorkedTime(
                                schemas.NumberBase,
                                schemas.NoneBase,
                                schemas.Schema,
                                schemas.NoneDecimalMixin
                            ):
                            
                            
                                def __new__(
                                    cls,
                                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                ) -> 'payedWorkedTime':
                                    return super().__new__(
                                        cls,
                                        *args,
                                        _configuration=_configuration,
                                    )
                            
                            
                            class workTimeUnit(
                                schemas.EnumBase,
                                schemas.StrBase,
                                schemas.NoneBase,
                                schemas.Schema,
                                schemas.NoneStrMixin
                            ):
                            
                            
                                class MetaOapg:
                                    enum_value_to_name = {
                                        "days": "DAYS",
                                        "hours": "HOURS",
                                    }
                                
                                @schemas.classproperty
                                def DAYS(cls):
                                    return cls("days")
                                
                                @schemas.classproperty
                                def HOURS(cls):
                                    return cls("hours")
                            
                            
                                def __new__(
                                    cls,
                                    *args: typing.Union[None, str, ],
                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                ) -> 'workTimeUnit':
                                    return super().__new__(
                                        cls,
                                        *args,
                                        _configuration=_configuration,
                                    )
                            __annotations__ = {
                                "effectiveWorkedTime": effectiveWorkedTime,
                                "payedWorkedTime": payedWorkedTime,
                                "workTimeUnit": workTimeUnit,
                            }
                    
                    payedWorkedTime: MetaOapg.properties.payedWorkedTime
                    workTimeUnit: MetaOapg.properties.workTimeUnit
                    effectiveWorkedTime: MetaOapg.properties.effectiveWorkedTime
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["effectiveWorkedTime"]) -> MetaOapg.properties.effectiveWorkedTime: ...
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["payedWorkedTime"]) -> MetaOapg.properties.payedWorkedTime: ...
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["workTimeUnit"]) -> MetaOapg.properties.workTimeUnit: ...
                    
                    @typing.overload
                    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                    
                    def __getitem__(self, name: typing.Union[typing_extensions.Literal["effectiveWorkedTime", "payedWorkedTime", "workTimeUnit", ], str]):
                        # dict_instance[name] accessor
                        return super().__getitem__(name)
                    
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["effectiveWorkedTime"]) -> MetaOapg.properties.effectiveWorkedTime: ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["payedWorkedTime"]) -> MetaOapg.properties.payedWorkedTime: ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["workTimeUnit"]) -> MetaOapg.properties.workTimeUnit: ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                    
                    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["effectiveWorkedTime", "payedWorkedTime", "workTimeUnit", ], str]):
                        return super().get_item_oapg(name)
                    
                
                    def __new__(
                        cls,
                        *args: typing.Union[dict, frozendict.frozendict, ],
                        payedWorkedTime: typing.Union[MetaOapg.properties.payedWorkedTime, None, decimal.Decimal, int, float, ],
                        workTimeUnit: typing.Union[MetaOapg.properties.workTimeUnit, None, str, ],
                        effectiveWorkedTime: typing.Union[MetaOapg.properties.effectiveWorkedTime, None, decimal.Decimal, int, float, ],
                        _configuration: typing.Optional[schemas.Configuration] = None,
                        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                    ) -> 'all_of_0':
                        return super().__new__(
                            cls,
                            *args,
                            payedWorkedTime=payedWorkedTime,
                            workTimeUnit=workTimeUnit,
                            effectiveWorkedTime=effectiveWorkedTime,
                            _configuration=_configuration,
                            **kwargs,
                        )
                
                
                class all_of_1(
                    schemas.DictSchema
                ):
                
                
                    class MetaOapg:
                        required = {
                            "contractId",
                        }
                        
                        class properties:
                            contractId = schemas.StrSchema
                            __annotations__ = {
                                "contractId": contractId,
                            }
                    
                    contractId: MetaOapg.properties.contractId
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["contractId"]) -> MetaOapg.properties.contractId: ...
                    
                    @typing.overload
                    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                    
                    def __getitem__(self, name: typing.Union[typing_extensions.Literal["contractId", ], str]):
                        # dict_instance[name] accessor
                        return super().__getitem__(name)
                    
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["contractId"]) -> MetaOapg.properties.contractId: ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                    
                    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["contractId", ], str]):
                        return super().get_item_oapg(name)
                    
                
                    def __new__(
                        cls,
                        *args: typing.Union[dict, frozendict.frozendict, ],
                        contractId: typing.Union[MetaOapg.properties.contractId, str, ],
                        _configuration: typing.Optional[schemas.Configuration] = None,
                        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                    ) -> 'all_of_1':
                        return super().__new__(
                            cls,
                            *args,
                            contractId=contractId,
                            _configuration=_configuration,
                            **kwargs,
                        )
                
                @classmethod
                @functools.lru_cache()
                def all_of(cls):
                    # we need this here to make our import statements work
                    # we must store _composed_schemas in here so the code is only run
                    # when we invoke this method. If we kept this at the class
                    # level we would get an error because the class level
                    # code would be run when this module is imported, and these composed
                    # classes don't exist yet because their module has not finished
                    # loading
                    return [
                        cls.all_of_0,
                        cls.all_of_1,
                    ]
        
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'items':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ContractListWorkedTimeByPayPeriodResponseContracts':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
