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


class CollaboratorListPayslipsResponsePayslipsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "month",
            "year",
            "payslipId",
            "payslipUrl",
            "contractId",
        }
        
        class properties:
            year = schemas.StrSchema
            month = schemas.StrSchema
            contractId = schemas.StrSchema
            payslipId = schemas.StrSchema
            payslipUrl = schemas.StrSchema
            __annotations__ = {
                "year": year,
                "month": month,
                "contractId": contractId,
                "payslipId": payslipId,
                "payslipUrl": payslipUrl,
            }
    
    month: MetaOapg.properties.month
    year: MetaOapg.properties.year
    payslipId: MetaOapg.properties.payslipId
    payslipUrl: MetaOapg.properties.payslipUrl
    contractId: MetaOapg.properties.contractId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["year"]) -> MetaOapg.properties.year: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["month"]) -> MetaOapg.properties.month: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contractId"]) -> MetaOapg.properties.contractId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payslipId"]) -> MetaOapg.properties.payslipId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payslipUrl"]) -> MetaOapg.properties.payslipUrl: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["year", "month", "contractId", "payslipId", "payslipUrl", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["year"]) -> MetaOapg.properties.year: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["month"]) -> MetaOapg.properties.month: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contractId"]) -> MetaOapg.properties.contractId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payslipId"]) -> MetaOapg.properties.payslipId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payslipUrl"]) -> MetaOapg.properties.payslipUrl: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["year", "month", "contractId", "payslipId", "payslipUrl", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        month: typing.Union[MetaOapg.properties.month, str, ],
        year: typing.Union[MetaOapg.properties.year, str, ],
        payslipId: typing.Union[MetaOapg.properties.payslipId, str, ],
        payslipUrl: typing.Union[MetaOapg.properties.payslipUrl, str, ],
        contractId: typing.Union[MetaOapg.properties.contractId, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CollaboratorListPayslipsResponsePayslipsItem':
        return super().__new__(
            cls,
            *args,
            month=month,
            year=year,
            payslipId=payslipId,
            payslipUrl=payslipUrl,
            contractId=contractId,
            _configuration=_configuration,
            **kwargs,
        )
