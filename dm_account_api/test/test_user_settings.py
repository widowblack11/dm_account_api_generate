"""
    DM.API Account

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import dm_account_api
from dm_account_api.model.color_schema import ColorSchema
from dm_account_api.model.paging_settings import PagingSettings
globals()['ColorSchema'] = ColorSchema
globals()['PagingSettings'] = PagingSettings
from dm_account_api.model.user_settings import UserSettings


class TestUserSettings(unittest.TestCase):
    """UserSettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUserSettings(self):
        """Test UserSettings"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UserSettings()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
