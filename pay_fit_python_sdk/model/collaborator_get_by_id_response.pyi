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


class CollaboratorGetByIdResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "emails",
            "terminationDate",
            "firstName",
            "lastName",
            "secondLastName",
            "gender",
            "matricule",
            "id",
            "birthDate",
            "birthName",
        }
        
        class properties:
            id = schemas.StrSchema
            
            
            class matricule(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'matricule':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            firstName = schemas.StrSchema
            lastName = schemas.StrSchema
            
            
            class secondLastName(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'secondLastName':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class birthName(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'birthName':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class birthDate(
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
                ) -> 'birthDate':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class terminationDate(
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
                ) -> 'terminationDate':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class gender(
                schemas.EnumBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "male": "MALE",
                        "female": "FEMALE",
                        "other": "OTHER",
                        None: "NONE",
                    }
                
                @schemas.classproperty
                def MALE(cls):
                    return cls("male")
                
                @schemas.classproperty
                def FEMALE(cls):
                    return cls("female")
                
                @schemas.classproperty
                def OTHER(cls):
                    return cls("other")
                
                @schemas.classproperty
                def NONE(cls):
                    return cls(None)
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'gender':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def emails() -> typing.Type['CollaboratorGetByIdResponseEmails']:
                return CollaboratorGetByIdResponseEmails
            
            
            class nationality(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'nationality':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class countryOfBirth(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'countryOfBirth':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class socialSecurityNumber(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'socialSecurityNumber':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class temporaryTechnicalNumber(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'temporaryTechnicalNumber':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class bic(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'bic':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class iban(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'iban':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def phoneNumbers() -> typing.Type['CollaboratorGetByIdResponsePhoneNumbers']:
                return CollaboratorGetByIdResponsePhoneNumbers
        
            @staticmethod
            def addresses() -> typing.Type['CollaboratorGetByIdResponseAddresses']:
                return CollaboratorGetByIdResponseAddresses
            
            
            class managerId(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'managerId':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class teamName(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'teamName':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def contracts() -> typing.Type['CollaboratorGetByIdResponseContracts']:
                return CollaboratorGetByIdResponseContracts
            __annotations__ = {
                "id": id,
                "matricule": matricule,
                "firstName": firstName,
                "lastName": lastName,
                "secondLastName": secondLastName,
                "birthName": birthName,
                "birthDate": birthDate,
                "terminationDate": terminationDate,
                "gender": gender,
                "emails": emails,
                "nationality": nationality,
                "countryOfBirth": countryOfBirth,
                "socialSecurityNumber": socialSecurityNumber,
                "temporaryTechnicalNumber": temporaryTechnicalNumber,
                "bic": bic,
                "iban": iban,
                "phoneNumbers": phoneNumbers,
                "addresses": addresses,
                "managerId": managerId,
                "teamName": teamName,
                "contracts": contracts,
            }
    
    emails: 'CollaboratorGetByIdResponseEmails'
    terminationDate: MetaOapg.properties.terminationDate
    firstName: MetaOapg.properties.firstName
    lastName: MetaOapg.properties.lastName
    secondLastName: MetaOapg.properties.secondLastName
    gender: MetaOapg.properties.gender
    matricule: MetaOapg.properties.matricule
    id: MetaOapg.properties.id
    birthDate: MetaOapg.properties.birthDate
    birthName: MetaOapg.properties.birthName
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["matricule"]) -> MetaOapg.properties.matricule: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firstName"]) -> MetaOapg.properties.firstName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastName"]) -> MetaOapg.properties.lastName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["secondLastName"]) -> MetaOapg.properties.secondLastName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["birthName"]) -> MetaOapg.properties.birthName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["birthDate"]) -> MetaOapg.properties.birthDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["terminationDate"]) -> MetaOapg.properties.terminationDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gender"]) -> MetaOapg.properties.gender: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["emails"]) -> 'CollaboratorGetByIdResponseEmails': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nationality"]) -> MetaOapg.properties.nationality: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["countryOfBirth"]) -> MetaOapg.properties.countryOfBirth: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["socialSecurityNumber"]) -> MetaOapg.properties.socialSecurityNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["temporaryTechnicalNumber"]) -> MetaOapg.properties.temporaryTechnicalNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bic"]) -> MetaOapg.properties.bic: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["iban"]) -> MetaOapg.properties.iban: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phoneNumbers"]) -> 'CollaboratorGetByIdResponsePhoneNumbers': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["addresses"]) -> 'CollaboratorGetByIdResponseAddresses': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["managerId"]) -> MetaOapg.properties.managerId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["teamName"]) -> MetaOapg.properties.teamName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contracts"]) -> 'CollaboratorGetByIdResponseContracts': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "matricule", "firstName", "lastName", "secondLastName", "birthName", "birthDate", "terminationDate", "gender", "emails", "nationality", "countryOfBirth", "socialSecurityNumber", "temporaryTechnicalNumber", "bic", "iban", "phoneNumbers", "addresses", "managerId", "teamName", "contracts", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["matricule"]) -> MetaOapg.properties.matricule: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firstName"]) -> MetaOapg.properties.firstName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastName"]) -> MetaOapg.properties.lastName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["secondLastName"]) -> MetaOapg.properties.secondLastName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["birthName"]) -> MetaOapg.properties.birthName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["birthDate"]) -> MetaOapg.properties.birthDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["terminationDate"]) -> MetaOapg.properties.terminationDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gender"]) -> MetaOapg.properties.gender: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["emails"]) -> 'CollaboratorGetByIdResponseEmails': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nationality"]) -> typing.Union[MetaOapg.properties.nationality, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["countryOfBirth"]) -> typing.Union[MetaOapg.properties.countryOfBirth, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["socialSecurityNumber"]) -> typing.Union[MetaOapg.properties.socialSecurityNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["temporaryTechnicalNumber"]) -> typing.Union[MetaOapg.properties.temporaryTechnicalNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bic"]) -> typing.Union[MetaOapg.properties.bic, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["iban"]) -> typing.Union[MetaOapg.properties.iban, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phoneNumbers"]) -> typing.Union['CollaboratorGetByIdResponsePhoneNumbers', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["addresses"]) -> typing.Union['CollaboratorGetByIdResponseAddresses', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["managerId"]) -> typing.Union[MetaOapg.properties.managerId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["teamName"]) -> typing.Union[MetaOapg.properties.teamName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contracts"]) -> typing.Union['CollaboratorGetByIdResponseContracts', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "matricule", "firstName", "lastName", "secondLastName", "birthName", "birthDate", "terminationDate", "gender", "emails", "nationality", "countryOfBirth", "socialSecurityNumber", "temporaryTechnicalNumber", "bic", "iban", "phoneNumbers", "addresses", "managerId", "teamName", "contracts", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        emails: 'CollaboratorGetByIdResponseEmails',
        terminationDate: typing.Union[MetaOapg.properties.terminationDate, None, str, date, ],
        firstName: typing.Union[MetaOapg.properties.firstName, str, ],
        lastName: typing.Union[MetaOapg.properties.lastName, str, ],
        secondLastName: typing.Union[MetaOapg.properties.secondLastName, None, str, ],
        gender: typing.Union[MetaOapg.properties.gender, None, str, ],
        matricule: typing.Union[MetaOapg.properties.matricule, None, str, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        birthDate: typing.Union[MetaOapg.properties.birthDate, None, str, date, ],
        birthName: typing.Union[MetaOapg.properties.birthName, None, str, ],
        nationality: typing.Union[MetaOapg.properties.nationality, None, str, schemas.Unset] = schemas.unset,
        countryOfBirth: typing.Union[MetaOapg.properties.countryOfBirth, None, str, schemas.Unset] = schemas.unset,
        socialSecurityNumber: typing.Union[MetaOapg.properties.socialSecurityNumber, None, str, schemas.Unset] = schemas.unset,
        temporaryTechnicalNumber: typing.Union[MetaOapg.properties.temporaryTechnicalNumber, None, str, schemas.Unset] = schemas.unset,
        bic: typing.Union[MetaOapg.properties.bic, None, str, schemas.Unset] = schemas.unset,
        iban: typing.Union[MetaOapg.properties.iban, None, str, schemas.Unset] = schemas.unset,
        phoneNumbers: typing.Union['CollaboratorGetByIdResponsePhoneNumbers', schemas.Unset] = schemas.unset,
        addresses: typing.Union['CollaboratorGetByIdResponseAddresses', schemas.Unset] = schemas.unset,
        managerId: typing.Union[MetaOapg.properties.managerId, None, str, schemas.Unset] = schemas.unset,
        teamName: typing.Union[MetaOapg.properties.teamName, None, str, schemas.Unset] = schemas.unset,
        contracts: typing.Union['CollaboratorGetByIdResponseContracts', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CollaboratorGetByIdResponse':
        return super().__new__(
            cls,
            *args,
            emails=emails,
            terminationDate=terminationDate,
            firstName=firstName,
            lastName=lastName,
            secondLastName=secondLastName,
            gender=gender,
            matricule=matricule,
            id=id,
            birthDate=birthDate,
            birthName=birthName,
            nationality=nationality,
            countryOfBirth=countryOfBirth,
            socialSecurityNumber=socialSecurityNumber,
            temporaryTechnicalNumber=temporaryTechnicalNumber,
            bic=bic,
            iban=iban,
            phoneNumbers=phoneNumbers,
            addresses=addresses,
            managerId=managerId,
            teamName=teamName,
            contracts=contracts,
            _configuration=_configuration,
            **kwargs,
        )

from pay_fit_python_sdk.model.collaborator_get_by_id_response_addresses import CollaboratorGetByIdResponseAddresses
from pay_fit_python_sdk.model.collaborator_get_by_id_response_contracts import CollaboratorGetByIdResponseContracts
from pay_fit_python_sdk.model.collaborator_get_by_id_response_emails import CollaboratorGetByIdResponseEmails
from pay_fit_python_sdk.model.collaborator_get_by_id_response_phone_numbers import CollaboratorGetByIdResponsePhoneNumbers
