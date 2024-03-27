# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from pay_fit_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    COMPANIES_COMPANY_ID = "/companies/{companyId}"
    COMPANIES_COMPANY_ID_ACCOUNTING = "/companies/{companyId}/accounting"
    COMPANIES_COMPANY_ID_ACCOUNTINGV2 = "/companies/{companyId}/accounting-v2"
    COMPANIES_COMPANY_ID_PAYROLLSTATUS = "/companies/{companyId}/payroll-status"
    COMPANIES_COMPANY_ID_HEALTHINSURANCECONTRACTS = "/companies/{companyId}/health-insurance-contracts"
    COMPANIES_COMPANY_ID_PROVIDENTFUNDCONTRACTS = "/companies/{companyId}/provident-fund-contracts"
    COMPANIESFR_COMPANY_ID = "/companies-fr/{companyId}"
    COMPANIES_COMPANY_ID_CONTRACTS = "/companies/{companyId}/contracts"
    COMPANIES_COMPANY_ID_CONTRACTS_TIME = "/companies/{companyId}/contracts/time"
    COMPANIES_COMPANY_ID_CONTRACTS_CONTRACT_ID = "/companies/{companyId}/contracts/{contractId}"
    COMPANIES_COMPANY_ID_CONTRACTSFR = "/companies/{companyId}/contracts-fr"
    COMPANIES_COMPANY_ID_CONTRACTSFR_CONTRACT_ID = "/companies/{companyId}/contracts-fr/{contractId}"
    COMPANIES_COMPANY_ID_CONTRACTSFR_CONTRACT_ID_HEALTHINSURANCE = "/companies/{companyId}/contracts-fr/{contractId}/health-insurance"
    COMPANIES_COMPANY_ID_CONTRACTSFR_CONTRACT_ID_PROVIDENTFUND = "/companies/{companyId}/contracts-fr/{contractId}/provident-fund"
    COMPANIES_COMPANY_ID_COLLABORATORS = "/companies/{companyId}/collaborators"
    COMPANIES_COMPANY_ID_COLLABORATORS_MEALVOUCHERS = "/companies/{companyId}/collaborators/meal-vouchers"
    COMPANIES_COMPANY_ID_COLLABORATORS_COLLABORATOR_ID = "/companies/{companyId}/collaborators/{collaboratorId}"
    COMPANIES_COMPANY_ID_COLLABORATORS_COLLABORATOR_ID_CONTRACTS_CONTRACT_ID_PAYSLIPS_PAYSLIP_ID = "/companies/{companyId}/collaborators/{collaboratorId}/contracts/{contractId}/payslips/{payslipId}"
    COMPANIES_COMPANY_ID_COLLABORATORS_COLLABORATOR_ID_PAYSLIPS = "/companies/{companyId}/collaborators/{collaboratorId}/payslips"
