import typing_extensions

from pay_fit_python_sdk.paths import PathValues
from pay_fit_python_sdk.apis.paths.companies_company_id import CompaniesCompanyId
from pay_fit_python_sdk.apis.paths.companies_company_id_accounting import CompaniesCompanyIdAccounting
from pay_fit_python_sdk.apis.paths.companies_company_id_accounting_v2 import CompaniesCompanyIdAccountingV2
from pay_fit_python_sdk.apis.paths.companies_company_id_payroll_status import CompaniesCompanyIdPayrollStatus
from pay_fit_python_sdk.apis.paths.companies_company_id_health_insurance_contracts import CompaniesCompanyIdHealthInsuranceContracts
from pay_fit_python_sdk.apis.paths.companies_company_id_provident_fund_contracts import CompaniesCompanyIdProvidentFundContracts
from pay_fit_python_sdk.apis.paths.companies_fr_company_id import CompaniesFrCompanyId
from pay_fit_python_sdk.apis.paths.companies_company_id_contracts import CompaniesCompanyIdContracts
from pay_fit_python_sdk.apis.paths.companies_company_id_contracts_time import CompaniesCompanyIdContractsTime
from pay_fit_python_sdk.apis.paths.companies_company_id_contracts_contract_id import CompaniesCompanyIdContractsContractId
from pay_fit_python_sdk.apis.paths.companies_company_id_contracts_fr import CompaniesCompanyIdContractsFr
from pay_fit_python_sdk.apis.paths.companies_company_id_contracts_fr_contract_id import CompaniesCompanyIdContractsFrContractId
from pay_fit_python_sdk.apis.paths.companies_company_id_contracts_fr_contract_id_health_insurance import CompaniesCompanyIdContractsFrContractIdHealthInsurance
from pay_fit_python_sdk.apis.paths.companies_company_id_contracts_fr_contract_id_provident_fund import CompaniesCompanyIdContractsFrContractIdProvidentFund
from pay_fit_python_sdk.apis.paths.companies_company_id_collaborators import CompaniesCompanyIdCollaborators
from pay_fit_python_sdk.apis.paths.companies_company_id_collaborators_meal_vouchers import CompaniesCompanyIdCollaboratorsMealVouchers
from pay_fit_python_sdk.apis.paths.companies_company_id_collaborators_collaborator_id import CompaniesCompanyIdCollaboratorsCollaboratorId
from pay_fit_python_sdk.apis.paths.companies_company_id_collaborators_collaborator_id_contracts_contract_id_payslips_payslip_id import CompaniesCompanyIdCollaboratorsCollaboratorIdContractsContractIdPayslipsPayslipId
from pay_fit_python_sdk.apis.paths.companies_company_id_collaborators_collaborator_id_payslips import CompaniesCompanyIdCollaboratorsCollaboratorIdPayslips

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.COMPANIES_COMPANY_ID: CompaniesCompanyId,
        PathValues.COMPANIES_COMPANY_ID_ACCOUNTING: CompaniesCompanyIdAccounting,
        PathValues.COMPANIES_COMPANY_ID_ACCOUNTINGV2: CompaniesCompanyIdAccountingV2,
        PathValues.COMPANIES_COMPANY_ID_PAYROLLSTATUS: CompaniesCompanyIdPayrollStatus,
        PathValues.COMPANIES_COMPANY_ID_HEALTHINSURANCECONTRACTS: CompaniesCompanyIdHealthInsuranceContracts,
        PathValues.COMPANIES_COMPANY_ID_PROVIDENTFUNDCONTRACTS: CompaniesCompanyIdProvidentFundContracts,
        PathValues.COMPANIESFR_COMPANY_ID: CompaniesFrCompanyId,
        PathValues.COMPANIES_COMPANY_ID_CONTRACTS: CompaniesCompanyIdContracts,
        PathValues.COMPANIES_COMPANY_ID_CONTRACTS_TIME: CompaniesCompanyIdContractsTime,
        PathValues.COMPANIES_COMPANY_ID_CONTRACTS_CONTRACT_ID: CompaniesCompanyIdContractsContractId,
        PathValues.COMPANIES_COMPANY_ID_CONTRACTSFR: CompaniesCompanyIdContractsFr,
        PathValues.COMPANIES_COMPANY_ID_CONTRACTSFR_CONTRACT_ID: CompaniesCompanyIdContractsFrContractId,
        PathValues.COMPANIES_COMPANY_ID_CONTRACTSFR_CONTRACT_ID_HEALTHINSURANCE: CompaniesCompanyIdContractsFrContractIdHealthInsurance,
        PathValues.COMPANIES_COMPANY_ID_CONTRACTSFR_CONTRACT_ID_PROVIDENTFUND: CompaniesCompanyIdContractsFrContractIdProvidentFund,
        PathValues.COMPANIES_COMPANY_ID_COLLABORATORS: CompaniesCompanyIdCollaborators,
        PathValues.COMPANIES_COMPANY_ID_COLLABORATORS_MEALVOUCHERS: CompaniesCompanyIdCollaboratorsMealVouchers,
        PathValues.COMPANIES_COMPANY_ID_COLLABORATORS_COLLABORATOR_ID: CompaniesCompanyIdCollaboratorsCollaboratorId,
        PathValues.COMPANIES_COMPANY_ID_COLLABORATORS_COLLABORATOR_ID_CONTRACTS_CONTRACT_ID_PAYSLIPS_PAYSLIP_ID: CompaniesCompanyIdCollaboratorsCollaboratorIdContractsContractIdPayslipsPayslipId,
        PathValues.COMPANIES_COMPANY_ID_COLLABORATORS_COLLABORATOR_ID_PAYSLIPS: CompaniesCompanyIdCollaboratorsCollaboratorIdPayslips,
    }
)

path_to_api = PathToApi(
    {
        PathValues.COMPANIES_COMPANY_ID: CompaniesCompanyId,
        PathValues.COMPANIES_COMPANY_ID_ACCOUNTING: CompaniesCompanyIdAccounting,
        PathValues.COMPANIES_COMPANY_ID_ACCOUNTINGV2: CompaniesCompanyIdAccountingV2,
        PathValues.COMPANIES_COMPANY_ID_PAYROLLSTATUS: CompaniesCompanyIdPayrollStatus,
        PathValues.COMPANIES_COMPANY_ID_HEALTHINSURANCECONTRACTS: CompaniesCompanyIdHealthInsuranceContracts,
        PathValues.COMPANIES_COMPANY_ID_PROVIDENTFUNDCONTRACTS: CompaniesCompanyIdProvidentFundContracts,
        PathValues.COMPANIESFR_COMPANY_ID: CompaniesFrCompanyId,
        PathValues.COMPANIES_COMPANY_ID_CONTRACTS: CompaniesCompanyIdContracts,
        PathValues.COMPANIES_COMPANY_ID_CONTRACTS_TIME: CompaniesCompanyIdContractsTime,
        PathValues.COMPANIES_COMPANY_ID_CONTRACTS_CONTRACT_ID: CompaniesCompanyIdContractsContractId,
        PathValues.COMPANIES_COMPANY_ID_CONTRACTSFR: CompaniesCompanyIdContractsFr,
        PathValues.COMPANIES_COMPANY_ID_CONTRACTSFR_CONTRACT_ID: CompaniesCompanyIdContractsFrContractId,
        PathValues.COMPANIES_COMPANY_ID_CONTRACTSFR_CONTRACT_ID_HEALTHINSURANCE: CompaniesCompanyIdContractsFrContractIdHealthInsurance,
        PathValues.COMPANIES_COMPANY_ID_CONTRACTSFR_CONTRACT_ID_PROVIDENTFUND: CompaniesCompanyIdContractsFrContractIdProvidentFund,
        PathValues.COMPANIES_COMPANY_ID_COLLABORATORS: CompaniesCompanyIdCollaborators,
        PathValues.COMPANIES_COMPANY_ID_COLLABORATORS_MEALVOUCHERS: CompaniesCompanyIdCollaboratorsMealVouchers,
        PathValues.COMPANIES_COMPANY_ID_COLLABORATORS_COLLABORATOR_ID: CompaniesCompanyIdCollaboratorsCollaboratorId,
        PathValues.COMPANIES_COMPANY_ID_COLLABORATORS_COLLABORATOR_ID_CONTRACTS_CONTRACT_ID_PAYSLIPS_PAYSLIP_ID: CompaniesCompanyIdCollaboratorsCollaboratorIdContractsContractIdPayslipsPayslipId,
        PathValues.COMPANIES_COMPANY_ID_COLLABORATORS_COLLABORATOR_ID_PAYSLIPS: CompaniesCompanyIdCollaboratorsCollaboratorIdPayslips,
    }
)
