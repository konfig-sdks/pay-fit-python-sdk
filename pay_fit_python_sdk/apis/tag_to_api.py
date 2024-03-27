import typing_extensions

from pay_fit_python_sdk.apis.tags import TagValues
from pay_fit_python_sdk.apis.tags.company_api import CompanyApi
from pay_fit_python_sdk.apis.tags.contract_api import ContractApi
from pay_fit_python_sdk.apis.tags.collaborator_api import CollaboratorApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.COMPANY: CompanyApi,
        TagValues.CONTRACT: ContractApi,
        TagValues.COLLABORATOR: CollaboratorApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.COMPANY: CompanyApi,
        TagValues.CONTRACT: ContractApi,
        TagValues.COLLABORATOR: CollaboratorApi,
    }
)
