"""
    OneLogin API

    OneLogin API generated with openapi-generator

    The version of the OpenAPI document: 3.0.0-alpha.1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import onelogin
from onelogin.model.hook_conditions_inner import HookConditionsInner
from onelogin.model.hook_options import HookOptions
globals()['HookConditionsInner'] = HookConditionsInner
globals()['HookOptions'] = HookOptions
from onelogin.model.hook import Hook


class TestHook(unittest.TestCase):
    """Hook unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testHook(self):
        """Test Hook"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Hook()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
