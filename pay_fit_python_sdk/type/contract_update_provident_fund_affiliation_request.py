# coding: utf-8

"""
    Partner API

    A Semi-Private API to let third parties communicate with PayFit

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from pay_fit_python_sdk.type.contract_update_provident_fund_affiliation_request_provident_fund_contract_ids import ContractUpdateProvidentFundAffiliationRequestProvidentFundContractIds

class RequiredContractUpdateProvidentFundAffiliationRequest(TypedDict):
    providentFundContractIds: ContractUpdateProvidentFundAffiliationRequestProvidentFundContractIds

class OptionalContractUpdateProvidentFundAffiliationRequest(TypedDict, total=False):
    pass

class ContractUpdateProvidentFundAffiliationRequest(RequiredContractUpdateProvidentFundAffiliationRequest, OptionalContractUpdateProvidentFundAffiliationRequest):
    pass
