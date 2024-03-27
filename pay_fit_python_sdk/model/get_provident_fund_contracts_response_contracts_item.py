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


class GetProvidentFundContractsResponseContractsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "codePopulation",
            "affiliatedContractIds",
            "baseDeCotisation",
            "modeCalculCotisation",
            "refContrat",
            "codeOption",
            "idContrat",
        }
        
        class properties:
            idContrat = schemas.StrSchema
            
            
            class refContrat(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'refContrat':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class codePopulation(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'codePopulation':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class codeOption(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'codeOption':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def affiliatedContractIds() -> typing.Type['GetProvidentFundContractsResponseContractsItemAffiliatedContractIds']:
                return GetProvidentFundContractsResponseContractsItemAffiliatedContractIds
            
            
            class modeCalculCotisation(
                schemas.EnumBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "1": "POSITIVE_1",
                        "2": "POSITIVE_2",
                        "3": "POSITIVE_3",
                    }
                
                @schemas.classproperty
                def POSITIVE_1(cls):
                    return cls("1")
                
                @schemas.classproperty
                def POSITIVE_2(cls):
                    return cls("2")
                
                @schemas.classproperty
                def POSITIVE_3(cls):
                    return cls("3")
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'modeCalculCotisation':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class baseDeCotisation(
                schemas.EnumBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "1": "POSITIVE_1",
                        "2": "POSITIVE_2",
                        "3": "POSITIVE_3",
                        "4": "POSITIVE_4",
                        "5": "POSITIVE_5",
                    }
                
                @schemas.classproperty
                def POSITIVE_1(cls):
                    return cls("1")
                
                @schemas.classproperty
                def POSITIVE_2(cls):
                    return cls("2")
                
                @schemas.classproperty
                def POSITIVE_3(cls):
                    return cls("3")
                
                @schemas.classproperty
                def POSITIVE_4(cls):
                    return cls("4")
                
                @schemas.classproperty
                def POSITIVE_5(cls):
                    return cls("5")
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'baseDeCotisation':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "idContrat": idContrat,
                "refContrat": refContrat,
                "codePopulation": codePopulation,
                "codeOption": codeOption,
                "affiliatedContractIds": affiliatedContractIds,
                "modeCalculCotisation": modeCalculCotisation,
                "baseDeCotisation": baseDeCotisation,
            }
    
    codePopulation: MetaOapg.properties.codePopulation
    affiliatedContractIds: 'GetProvidentFundContractsResponseContractsItemAffiliatedContractIds'
    baseDeCotisation: MetaOapg.properties.baseDeCotisation
    modeCalculCotisation: MetaOapg.properties.modeCalculCotisation
    refContrat: MetaOapg.properties.refContrat
    codeOption: MetaOapg.properties.codeOption
    idContrat: MetaOapg.properties.idContrat
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["idContrat"]) -> MetaOapg.properties.idContrat: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["refContrat"]) -> MetaOapg.properties.refContrat: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["codePopulation"]) -> MetaOapg.properties.codePopulation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["codeOption"]) -> MetaOapg.properties.codeOption: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["affiliatedContractIds"]) -> 'GetProvidentFundContractsResponseContractsItemAffiliatedContractIds': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["modeCalculCotisation"]) -> MetaOapg.properties.modeCalculCotisation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["baseDeCotisation"]) -> MetaOapg.properties.baseDeCotisation: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["idContrat", "refContrat", "codePopulation", "codeOption", "affiliatedContractIds", "modeCalculCotisation", "baseDeCotisation", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["idContrat"]) -> MetaOapg.properties.idContrat: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["refContrat"]) -> MetaOapg.properties.refContrat: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["codePopulation"]) -> MetaOapg.properties.codePopulation: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["codeOption"]) -> MetaOapg.properties.codeOption: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["affiliatedContractIds"]) -> 'GetProvidentFundContractsResponseContractsItemAffiliatedContractIds': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["modeCalculCotisation"]) -> MetaOapg.properties.modeCalculCotisation: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["baseDeCotisation"]) -> MetaOapg.properties.baseDeCotisation: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["idContrat", "refContrat", "codePopulation", "codeOption", "affiliatedContractIds", "modeCalculCotisation", "baseDeCotisation", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        codePopulation: typing.Union[MetaOapg.properties.codePopulation, None, str, ],
        affiliatedContractIds: 'GetProvidentFundContractsResponseContractsItemAffiliatedContractIds',
        baseDeCotisation: typing.Union[MetaOapg.properties.baseDeCotisation, None, str, ],
        modeCalculCotisation: typing.Union[MetaOapg.properties.modeCalculCotisation, None, str, ],
        refContrat: typing.Union[MetaOapg.properties.refContrat, None, str, ],
        codeOption: typing.Union[MetaOapg.properties.codeOption, None, str, ],
        idContrat: typing.Union[MetaOapg.properties.idContrat, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GetProvidentFundContractsResponseContractsItem':
        return super().__new__(
            cls,
            *args,
            codePopulation=codePopulation,
            affiliatedContractIds=affiliatedContractIds,
            baseDeCotisation=baseDeCotisation,
            modeCalculCotisation=modeCalculCotisation,
            refContrat=refContrat,
            codeOption=codeOption,
            idContrat=idContrat,
            _configuration=_configuration,
            **kwargs,
        )

from pay_fit_python_sdk.model.get_provident_fund_contracts_response_contracts_item_affiliated_contract_ids import GetProvidentFundContractsResponseContractsItemAffiliatedContractIds