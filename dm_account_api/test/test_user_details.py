"""
    DM.API Account

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import dm_account_api
from dm_account_api.model.info_bb_text import InfoBbText
from dm_account_api.model.rating import Rating
from dm_account_api.model.user_role import UserRole
from dm_account_api.model.user_settings import UserSettings
globals()['InfoBbText'] = InfoBbText
globals()['Rating'] = Rating
globals()['UserRole'] = UserRole
globals()['UserSettings'] = UserSettings
from dm_account_api.model.user_details import UserDetails


class TestUserDetails(unittest.TestCase):
    """UserDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUserDetails(self):
        """Test UserDetails"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UserDetails()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()