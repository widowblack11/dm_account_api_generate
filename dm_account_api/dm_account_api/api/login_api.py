"""
    DM.API Account

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401
import allure

from dm_account_api.api_client import ApiClient, Endpoint as _Endpoint
from dm_account_api.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from dm_account_api.model.bad_request_error import BadRequestError
from dm_account_api.model.general_error import GeneralError
from dm_account_api.model.login_credentials import LoginCredentials
from dm_account_api.model.user_envelope import UserEnvelope


class LoginApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
	
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        @allure.step("Logout from every device")
        def __v1_account_login_all_delete(
            self,
            x_dm_auth_token,
            **kwargs
        ):
            """Logout from every device  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.v1_account_login_all_delete(x_dm_auth_token, async_req=True)
            >>> result = thread.get()

            Args:
                x_dm_auth_token (str): Authenticated requests require X-Dm-Auth-Token header. You can get the data from POST /account/ method, sending login and password in \"token\" response field

            Keyword Args:
                x_dm_bb_render_mode (str): Requests with user defined texts that allows usage of BB-codes may be rendered differently by passing the X-Dm-Bb-Render-Mode header of one of following values Html, Bb, Text, SafeHtml. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                None
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['x_dm_auth_token'] = \
                x_dm_auth_token
            return self.call_with_http_info(**kwargs)

        self.v1_account_login_all_delete = _Endpoint(
            settings={
                'response_type': None,
                'auth': [],
                'endpoint_path': '/v1/account/login/all',
                'operation_id': 'v1_account_login_all_delete',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_dm_auth_token',
                    'x_dm_bb_render_mode',
                ],
                'required': [
                    'x_dm_auth_token',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'x_dm_auth_token':
                        (str,),
                    'x_dm_bb_render_mode':
                        (str,),
                },
                'attribute_map': {
                    'x_dm_auth_token': 'X-Dm-Auth-Token',
                    'x_dm_bb_render_mode': 'X-Dm-Bb-Render-Mode',
                },
                'location_map': {
                    'x_dm_auth_token': 'header',
                    'x_dm_bb_render_mode': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/plain',
                    'application/json',
                    'text/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__v1_account_login_all_delete
        )

        @allure.step("Logout as current user")
        def __v1_account_login_delete(
            self,
            x_dm_auth_token,
            **kwargs
        ):
            """Logout as current user  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.v1_account_login_delete(x_dm_auth_token, async_req=True)
            >>> result = thread.get()

            Args:
                x_dm_auth_token (str): Authenticated requests require X-Dm-Auth-Token header. You can get the data from POST /account/ method, sending login and password in \"token\" response field

            Keyword Args:
                x_dm_bb_render_mode (str): Requests with user defined texts that allows usage of BB-codes may be rendered differently by passing the X-Dm-Bb-Render-Mode header of one of following values Html, Bb, Text, SafeHtml. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                None
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['x_dm_auth_token'] = \
                x_dm_auth_token
            return self.call_with_http_info(**kwargs)

        self.v1_account_login_delete = _Endpoint(
            settings={
                'response_type': None,
                'auth': [],
                'endpoint_path': '/v1/account/login',
                'operation_id': 'v1_account_login_delete',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_dm_auth_token',
                    'x_dm_bb_render_mode',
                ],
                'required': [
                    'x_dm_auth_token',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'x_dm_auth_token':
                        (str,),
                    'x_dm_bb_render_mode':
                        (str,),
                },
                'attribute_map': {
                    'x_dm_auth_token': 'X-Dm-Auth-Token',
                    'x_dm_bb_render_mode': 'X-Dm-Bb-Render-Mode',
                },
                'location_map': {
                    'x_dm_auth_token': 'header',
                    'x_dm_bb_render_mode': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/plain',
                    'application/json',
                    'text/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__v1_account_login_delete
        )

        @allure.step("Authenticate via credentials")
        def __v1_account_login_post(
            self,
            **kwargs
        ):
            """Authenticate via credentials  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.v1_account_login_post(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                x_dm_bb_render_mode (str): Requests with user defined texts that allows usage of BB-codes may be rendered differently by passing the X-Dm-Bb-Render-Mode header of one of following values Html, Bb, Text, SafeHtml. [optional]
                login_credentials (LoginCredentials): Login credentials. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                UserEnvelope
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.v1_account_login_post = _Endpoint(
            settings={
                'response_type': (UserEnvelope,),
                'auth': [],
                'endpoint_path': '/v1/account/login',
                'operation_id': 'v1_account_login_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_dm_bb_render_mode',
                    'login_credentials',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'x_dm_bb_render_mode':
                        (str,),
                    'login_credentials':
                        (LoginCredentials,),
                },
                'attribute_map': {
                    'x_dm_bb_render_mode': 'X-Dm-Bb-Render-Mode',
                },
                'location_map': {
                    'x_dm_bb_render_mode': 'header',
                    'login_credentials': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/plain',
                    'application/json',
                    'text/json'
                ],
                'content_type': [
                    'application/json',
                    'text/json',
                    'application/*+json'
                ]
            },
            api_client=api_client,
            callable=__v1_account_login_post
        )