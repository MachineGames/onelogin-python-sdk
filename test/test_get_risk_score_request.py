"""
    OneLogin API

    OneLogin API generated with openapi-generator

    The version of the OpenAPI document: 3.0.0-alpha.1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import onelogin
from onelogin.model.risk_device import RiskDevice
from onelogin.model.risk_user import RiskUser
from onelogin.model.session import Session
from onelogin.model.source import Source
globals()['RiskDevice'] = RiskDevice
globals()['RiskUser'] = RiskUser
globals()['Session'] = Session
globals()['Source'] = Source
from onelogin.model.get_risk_score_request import GetRiskScoreRequest


class TestGetRiskScoreRequest(unittest.TestCase):
    """GetRiskScoreRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetRiskScoreRequest(self):
        """Test GetRiskScoreRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = GetRiskScoreRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
