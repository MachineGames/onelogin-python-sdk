# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import onelogin
from onelogin.paths.api_2_api_authorizations_api_auth_id_clients_client_app_id import delete  # noqa: E501
from onelogin import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApi2ApiAuthorizationsApiAuthIdClientsClientAppId(ApiTestMixin, unittest.TestCase):
    """
    Api2ApiAuthorizationsApiAuthIdClientsClientAppId unit test stubs
        Remove Client App  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = delete.ApiFordelete(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
