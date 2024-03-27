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


class GetContractResponse(
    schemas.ComposedSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        
        class all_of_0(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "standardWeeklyHours",
                    "fullTimeEquivalent",
                    "isFullTime",
                }
                
                class properties:
                    
                    
                    class standardWeeklyHours(
                        schemas.NumberBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneDecimalMixin
                    ):
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[None, decimal.Decimal, int, float, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'standardWeeklyHours':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                            )
                    
                    
                    class fullTimeEquivalent(
                        schemas.NumberBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneDecimalMixin
                    ):
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[None, decimal.Decimal, int, float, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'fullTimeEquivalent':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                            )
                    
                    
                    class isFullTime(
                        schemas.BoolBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneBoolMixin
                    ):
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[None, bool, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'isFullTime':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                            )
                    __annotations__ = {
                        "standardWeeklyHours": standardWeeklyHours,
                        "fullTimeEquivalent": fullTimeEquivalent,
                        "isFullTime": isFullTime,
                    }
            
            standardWeeklyHours: MetaOapg.properties.standardWeeklyHours
            fullTimeEquivalent: MetaOapg.properties.fullTimeEquivalent
            isFullTime: MetaOapg.properties.isFullTime
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["standardWeeklyHours"]) -> MetaOapg.properties.standardWeeklyHours: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["fullTimeEquivalent"]) -> MetaOapg.properties.fullTimeEquivalent: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["isFullTime"]) -> MetaOapg.properties.isFullTime: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["standardWeeklyHours", "fullTimeEquivalent", "isFullTime", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["standardWeeklyHours"]) -> MetaOapg.properties.standardWeeklyHours: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["fullTimeEquivalent"]) -> MetaOapg.properties.fullTimeEquivalent: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["isFullTime"]) -> MetaOapg.properties.isFullTime: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["standardWeeklyHours", "fullTimeEquivalent", "isFullTime", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                standardWeeklyHours: typing.Union[MetaOapg.properties.standardWeeklyHours, None, decimal.Decimal, int, float, ],
                fullTimeEquivalent: typing.Union[MetaOapg.properties.fullTimeEquivalent, None, decimal.Decimal, int, float, ],
                isFullTime: typing.Union[MetaOapg.properties.isFullTime, None, bool, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_0':
                return super().__new__(
                    cls,
                    *args,
                    standardWeeklyHours=standardWeeklyHours,
                    fullTimeEquivalent=fullTimeEquivalent,
                    isFullTime=isFullTime,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class all_of_1(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "jobName",
                    "companyId",
                    "contractId",
                    "startDate",
                    "collaboratorId",
                    "status",
                }
                
                class properties:
                    contractId = schemas.StrSchema
                    companyId = schemas.StrSchema
                    startDate = schemas.DateSchema
                    
                    
                    class endDate(
                        schemas.DateBase,
                        schemas.StrBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneStrMixin
                    ):
                    
                    
                        class MetaOapg:
                            format = 'date'
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[None, str, date, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'endDate':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                            )
                    
                    
                    class probationEndDate(
                        schemas.DateBase,
                        schemas.StrBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneStrMixin
                    ):
                    
                    
                        class MetaOapg:
                            format = 'date'
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[None, str, date, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'probationEndDate':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                            )
                    jobName = schemas.StrSchema
                    
                    
                    class status(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                        
                        @schemas.classproperty
                        def ACTIVE(cls):
                            return cls("ACTIVE")
                        
                        @schemas.classproperty
                        def ARCHIVED(cls):
                            return cls("ARCHIVED")
                        
                        @schemas.classproperty
                        def PENDING(cls):
                            return cls("PENDING")
                    collaboratorId = schemas.StrSchema
                    __annotations__ = {
                        "contractId": contractId,
                        "companyId": companyId,
                        "startDate": startDate,
                        "endDate": endDate,
                        "probationEndDate": probationEndDate,
                        "jobName": jobName,
                        "status": status,
                        "collaboratorId": collaboratorId,
                    }
            
            jobName: MetaOapg.properties.jobName
            companyId: MetaOapg.properties.companyId
            contractId: MetaOapg.properties.contractId
            startDate: MetaOapg.properties.startDate
            collaboratorId: MetaOapg.properties.collaboratorId
            status: MetaOapg.properties.status
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["contractId"]) -> MetaOapg.properties.contractId: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["companyId"]) -> MetaOapg.properties.companyId: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["startDate"]) -> MetaOapg.properties.startDate: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["endDate"]) -> MetaOapg.properties.endDate: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["probationEndDate"]) -> MetaOapg.properties.probationEndDate: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["jobName"]) -> MetaOapg.properties.jobName: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["collaboratorId"]) -> MetaOapg.properties.collaboratorId: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["contractId", "companyId", "startDate", "endDate", "probationEndDate", "jobName", "status", "collaboratorId", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["contractId"]) -> MetaOapg.properties.contractId: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["companyId"]) -> MetaOapg.properties.companyId: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["startDate"]) -> MetaOapg.properties.startDate: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["endDate"]) -> typing.Union[MetaOapg.properties.endDate, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["probationEndDate"]) -> typing.Union[MetaOapg.properties.probationEndDate, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["jobName"]) -> MetaOapg.properties.jobName: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["collaboratorId"]) -> MetaOapg.properties.collaboratorId: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["contractId", "companyId", "startDate", "endDate", "probationEndDate", "jobName", "status", "collaboratorId", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                jobName: typing.Union[MetaOapg.properties.jobName, str, ],
                companyId: typing.Union[MetaOapg.properties.companyId, str, ],
                contractId: typing.Union[MetaOapg.properties.contractId, str, ],
                startDate: typing.Union[MetaOapg.properties.startDate, str, date, ],
                collaboratorId: typing.Union[MetaOapg.properties.collaboratorId, str, ],
                status: typing.Union[MetaOapg.properties.status, str, ],
                endDate: typing.Union[MetaOapg.properties.endDate, None, str, date, schemas.Unset] = schemas.unset,
                probationEndDate: typing.Union[MetaOapg.properties.probationEndDate, None, str, date, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    jobName=jobName,
                    companyId=companyId,
                    contractId=contractId,
                    startDate=startDate,
                    collaboratorId=collaboratorId,
                    status=status,
                    endDate=endDate,
                    probationEndDate=probationEndDate,
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
    ) -> 'GetContractResponse':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )
