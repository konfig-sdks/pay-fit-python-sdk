# coding: utf-8

"""
    Partner API

    A Semi-Private API to let third parties communicate with PayFit

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from pay_fit_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from pay_fit_python_sdk.api_response import AsyncGeneratorResponse
from pay_fit_python_sdk import api_client, exceptions
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

from pay_fit_python_sdk.model.collaborator_list_meal_vouchers403_response import CollaboratorListMealVouchers403Response as CollaboratorListMealVouchers403ResponseSchema
from pay_fit_python_sdk.model.collaborator_list_meal_vouchers400_response import CollaboratorListMealVouchers400Response as CollaboratorListMealVouchers400ResponseSchema
from pay_fit_python_sdk.model.collaborator_list_meal_vouchers_response import CollaboratorListMealVouchersResponse as CollaboratorListMealVouchersResponseSchema
from pay_fit_python_sdk.model.collaborator_list_meal_vouchers401_response import CollaboratorListMealVouchers401Response as CollaboratorListMealVouchers401ResponseSchema
from pay_fit_python_sdk.model.collaborator_list_meal_vouchers404_response import CollaboratorListMealVouchers404Response as CollaboratorListMealVouchers404ResponseSchema

from pay_fit_python_sdk.type.collaborator_list_meal_vouchers403_response import CollaboratorListMealVouchers403Response
from pay_fit_python_sdk.type.collaborator_list_meal_vouchers404_response import CollaboratorListMealVouchers404Response
from pay_fit_python_sdk.type.collaborator_list_meal_vouchers401_response import CollaboratorListMealVouchers401Response
from pay_fit_python_sdk.type.collaborator_list_meal_vouchers400_response import CollaboratorListMealVouchers400Response
from pay_fit_python_sdk.type.collaborator_list_meal_vouchers_response import CollaboratorListMealVouchersResponse

from ...api_client import Dictionary
from pay_fit_python_sdk.pydantic.collaborator_list_meal_vouchers400_response import CollaboratorListMealVouchers400Response as CollaboratorListMealVouchers400ResponsePydantic
from pay_fit_python_sdk.pydantic.collaborator_list_meal_vouchers401_response import CollaboratorListMealVouchers401Response as CollaboratorListMealVouchers401ResponsePydantic
from pay_fit_python_sdk.pydantic.collaborator_list_meal_vouchers404_response import CollaboratorListMealVouchers404Response as CollaboratorListMealVouchers404ResponsePydantic
from pay_fit_python_sdk.pydantic.collaborator_list_meal_vouchers403_response import CollaboratorListMealVouchers403Response as CollaboratorListMealVouchers403ResponsePydantic
from pay_fit_python_sdk.pydantic.collaborator_list_meal_vouchers_response import CollaboratorListMealVouchersResponse as CollaboratorListMealVouchersResponsePydantic

from . import path

# Query params


class DateSchema(
    schemas.StrSchema
):


    class MetaOapg:
        regex=[{
            'pattern': r'^2\d{3}(0[1-9]|1[0-2])$',
        }]


class NextPageTokenSchema(
    schemas.DictSchema
):


    class MetaOapg:
        additional_properties = schemas.NotAnyTypeSchema

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs,
    ) -> 'NextPageTokenSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )


class MaxResultsSchema(
    schemas.DictSchema
):


    class MetaOapg:
        additional_properties = schemas.NotAnyTypeSchema

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs,
    ) -> 'MaxResultsSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'date': typing.Union[DateSchema, str, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'nextPageToken': typing.Union[NextPageTokenSchema, dict, frozendict.frozendict, ],
        'maxResults': typing.Union[MaxResultsSchema, dict, frozendict.frozendict, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_date = api_client.QueryParameter(
    name="date",
    style=api_client.ParameterStyle.FORM,
    schema=DateSchema,
    required=True,
    explode=True,
)
request_query_next_page_token = api_client.QueryParameter(
    name="nextPageToken",
    style=api_client.ParameterStyle.FORM,
    schema=NextPageTokenSchema,
    explode=True,
)
request_query_max_results = api_client.QueryParameter(
    name="maxResults",
    style=api_client.ParameterStyle.FORM,
    schema=MaxResultsSchema,
    explode=True,
)
# Path params
CompanyIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'companyId': typing.Union[CompanyIdSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_company_id = api_client.PathParameter(
    name="companyId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=CompanyIdSchema,
    required=True,
)
_auth = [
    'partner-api-oauth',
]
SchemaFor200ResponseBodyApplicationJson = CollaboratorListMealVouchersResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: CollaboratorListMealVouchersResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: CollaboratorListMealVouchersResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = CollaboratorListMealVouchers400ResponseSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: CollaboratorListMealVouchers400Response


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: CollaboratorListMealVouchers400Response


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = CollaboratorListMealVouchers401ResponseSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: CollaboratorListMealVouchers401Response


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: CollaboratorListMealVouchers401Response


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
SchemaFor403ResponseBodyApplicationJson = CollaboratorListMealVouchers403ResponseSchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: CollaboratorListMealVouchers403Response


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: CollaboratorListMealVouchers403Response


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJson),
    },
)
SchemaFor404ResponseBodyApplicationJson = CollaboratorListMealVouchers404ResponseSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: CollaboratorListMealVouchers404Response


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: CollaboratorListMealVouchers404Response


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '401': _response_for_401,
    '403': _response_for_403,
    '404': _response_for_404,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _list_meal_vouchers_mapped_args(
        self,
        company_id: str,
        date: str,
        next_page_token: typing.Optional[typing.Dict[str, typing.Any]] = None,
        max_results: typing.Optional[typing.Dict[str, typing.Any]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if date is not None:
            _query_params["date"] = date
        if next_page_token is not None:
            _query_params["nextPageToken"] = next_page_token
        if max_results is not None:
            _query_params["maxResults"] = max_results
        if company_id is not None:
            _path_params["companyId"] = company_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _alist_meal_vouchers_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        List all Collaborators Meal Vouchers
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_company_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_date,
            request_query_next_page_token,
            request_query_max_results,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/companies/{companyId}/collaborators/meal-vouchers',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _list_meal_vouchers_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        List all Collaborators Meal Vouchers
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_company_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_date,
            request_query_next_page_token,
            request_query_max_results,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/companies/{companyId}/collaborators/meal-vouchers',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class ListMealVouchersRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist_meal_vouchers(
        self,
        company_id: str,
        date: str,
        next_page_token: typing.Optional[typing.Dict[str, typing.Any]] = None,
        max_results: typing.Optional[typing.Dict[str, typing.Any]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_meal_vouchers_mapped_args(
            company_id=company_id,
            date=date,
            next_page_token=next_page_token,
            max_results=max_results,
        )
        return await self._alist_meal_vouchers_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def list_meal_vouchers(
        self,
        company_id: str,
        date: str,
        next_page_token: typing.Optional[typing.Dict[str, typing.Any]] = None,
        max_results: typing.Optional[typing.Dict[str, typing.Any]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_meal_vouchers_mapped_args(
            company_id=company_id,
            date=date,
            next_page_token=next_page_token,
            max_results=max_results,
        )
        return self._list_meal_vouchers_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class ListMealVouchers(BaseApi):

    async def alist_meal_vouchers(
        self,
        company_id: str,
        date: str,
        next_page_token: typing.Optional[typing.Dict[str, typing.Any]] = None,
        max_results: typing.Optional[typing.Dict[str, typing.Any]] = None,
        validate: bool = False,
        **kwargs,
    ) -> CollaboratorListMealVouchersResponsePydantic:
        raw_response = await self.raw.alist_meal_vouchers(
            company_id=company_id,
            date=date,
            next_page_token=next_page_token,
            max_results=max_results,
            **kwargs,
        )
        if validate:
            return CollaboratorListMealVouchersResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(CollaboratorListMealVouchersResponsePydantic, raw_response.body)
    
    
    def list_meal_vouchers(
        self,
        company_id: str,
        date: str,
        next_page_token: typing.Optional[typing.Dict[str, typing.Any]] = None,
        max_results: typing.Optional[typing.Dict[str, typing.Any]] = None,
        validate: bool = False,
    ) -> CollaboratorListMealVouchersResponsePydantic:
        raw_response = self.raw.list_meal_vouchers(
            company_id=company_id,
            date=date,
            next_page_token=next_page_token,
            max_results=max_results,
        )
        if validate:
            return CollaboratorListMealVouchersResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(CollaboratorListMealVouchersResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        company_id: str,
        date: str,
        next_page_token: typing.Optional[typing.Dict[str, typing.Any]] = None,
        max_results: typing.Optional[typing.Dict[str, typing.Any]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_meal_vouchers_mapped_args(
            company_id=company_id,
            date=date,
            next_page_token=next_page_token,
            max_results=max_results,
        )
        return await self._alist_meal_vouchers_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        company_id: str,
        date: str,
        next_page_token: typing.Optional[typing.Dict[str, typing.Any]] = None,
        max_results: typing.Optional[typing.Dict[str, typing.Any]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_meal_vouchers_mapped_args(
            company_id=company_id,
            date=date,
            next_page_token=next_page_token,
            max_results=max_results,
        )
        return self._list_meal_vouchers_oapg(
            query_params=args.query,
            path_params=args.path,
        )

