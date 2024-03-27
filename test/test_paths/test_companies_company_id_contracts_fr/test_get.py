# coding: utf-8

"""
    Partner API

    A Semi-Private API to let third parties communicate with PayFit

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import pay_fit_python_sdk
from pay_fit_python_sdk.paths.companies_company_id_contracts_fr import get
from pay_fit_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestCompaniesCompanyIdContractsFr(ApiTestMixin, unittest.TestCase):
    """
    CompaniesCompanyIdContractsFr unit test stubs
        List all Contracts (FR)
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
