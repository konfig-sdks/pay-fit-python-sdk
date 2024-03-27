operation_parameter_map = {
    '/companies/{companyId}/collaborators-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'nextPageToken'
            },
            {
                'name': 'maxResults'
            },
        ]
    },
    '/companies/{companyId}/collaborators/{collaboratorId}-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'collaboratorId'
            },
        ]
    },
    '/companies/{companyId}/collaborators/meal-vouchers-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'date'
            },
            {
                'name': 'nextPageToken'
            },
            {
                'name': 'maxResults'
            },
        ]
    },
    '/companies/{companyId}/collaborators/{collaboratorId}/payslips-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'collaboratorId'
            },
        ]
    },
    '/companies/{companyId}/collaborators/{collaboratorId}/contracts/{contractId}/payslips/{payslipId}-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'collaboratorId'
            },
            {
                'name': 'contractId'
            },
            {
                'name': 'payslipId'
            },
        ]
    },
    '/companies/{companyId}-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
        ]
    },
    '/companies/{companyId}/accounting-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'date'
            },
        ]
    },
    '/companies/{companyId}/accounting-v2-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'date'
            },
        ]
    },
    '/companies/{companyId}/payroll-status-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'date'
            },
        ]
    },
    '/companies-fr/{companyId}-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
        ]
    },
    '/companies/{companyId}/health-insurance-contracts-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
        ]
    },
    '/companies/{companyId}/provident-fund-contracts-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
        ]
    },
    '/companies/{companyId}/contracts/{contractId}-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'contractId'
            },
        ]
    },
    '/companies/{companyId}/contracts-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'nextPageToken'
            },
            {
                'name': 'maxResults'
            },
        ]
    },
    '/companies/{companyId}/contracts-fr/{contractId}-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'contractId'
            },
        ]
    },
    '/companies/{companyId}/contracts-fr-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'nextPageToken'
            },
            {
                'name': 'maxResults'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/companies/{companyId}/contracts/time-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'date'
            },
            {
                'name': 'nextPageToken'
            },
            {
                'name': 'maxResults'
            },
        ]
    },
    '/companies/{companyId}/contracts-fr/{contractId}/health-insurance-PUT': {
        'parameters': [
            {
                'name': 'healthInsuranceContractIds'
            },
            {
                'name': 'companyId'
            },
            {
                'name': 'contractId'
            },
        ]
    },
    '/companies/{companyId}/contracts-fr/{contractId}/provident-fund-PUT': {
        'parameters': [
            {
                'name': 'providentFundContractIds'
            },
            {
                'name': 'companyId'
            },
            {
                'name': 'contractId'
            },
        ]
    },
};