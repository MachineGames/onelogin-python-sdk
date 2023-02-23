# onelogin
OpenAPI Specification for OneLogin

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 3.1.1
- Package version: 3.1.2
- Build package: org.openapitools.codegen.languages.PythonNextgenClientCodegen
For more information, please visit [https://support.onelogin.com](https://support.onelogin.com)

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install onelogin
```
(you may need to run `pip` with root permission: `sudo pip install onelogin`)

Then import the package:
```python
import onelogin
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import onelogin
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function

import time
import onelogin
from onelogin.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://your-api-subdomain.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = onelogin.Configuration(
    host = "https://your-api-subdomain.onelogin.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]


# Enter a context with an instance of the API client
with onelogin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = onelogin.APIAuthClaimsApi(api_client)
    content_type = 'application/json' # str |  (default to 'application/json')
    api_auth_id = 'api_auth_id_example' # str | 
    create_auth_claim_request = onelogin.CreateAuthClaimRequest() # CreateAuthClaimRequest |  (optional)

    try:
        # Create Api Auth Server Claim
        api_response = api_instance.create_auth_claim(content_type, api_auth_id, create_auth_claim_request=create_auth_claim_request)
        print("The response of APIAuthClaimsApi->create_auth_claim:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling APIAuthClaimsApi->create_auth_claim: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://your-api-subdomain.onelogin.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*APIAuthClaimsApi* | [**create_auth_claim**](docs/APIAuthClaimsApi.md#create_auth_claim) | **POST** /api/2/api_authorizations/{api_auth_id}/claims | Create Api Auth Server Claim
*APIAuthClaimsApi* | [**delete_auth_claim**](docs/APIAuthClaimsApi.md#delete_auth_claim) | **DELETE** /api/2/api_authorizations/{api_auth_id}/claims/{claim_id} | Delete Api Auth Server Claim
*APIAuthClaimsApi* | [**get_authclaims**](docs/APIAuthClaimsApi.md#get_authclaims) | **GET** /api/2/api_authorizations/{api_auth_id}/claims | Get Api Auth Server claims
*APIAuthClaimsApi* | [**update_claim**](docs/APIAuthClaimsApi.md#update_claim) | **PUT** /api/2/api_authorizations/{api_auth_id}/claims/{claim_id} | Update Api Auth Server Claim
*APIAuthClientAppsApi* | [**add_client_app**](docs/APIAuthClientAppsApi.md#add_client_app) | **POST** /api/2/api_authorizations/{api_auth_id}/clients | Add Client App
*APIAuthClientAppsApi* | [**delete_client_app**](docs/APIAuthClientAppsApi.md#delete_client_app) | **DELETE** /api/2/api_authorizations/{api_auth_id}/clients/{client_app_id} | Remove Client App
*APIAuthClientAppsApi* | [**list_client_apps**](docs/APIAuthClientAppsApi.md#list_client_apps) | **GET** /api/2/api_authorizations/{api_auth_id}/clients | List Clients Apps
*APIAuthClientAppsApi* | [**update_client_app**](docs/APIAuthClientAppsApi.md#update_client_app) | **PUT** /api/2/api_authorizations/{api_auth_id}/clients/{client_app_id} | Update Client App
*APIAuthScopesApi* | [**create_scope**](docs/APIAuthScopesApi.md#create_scope) | **POST** /api/2/api_authorizations/{api_auth_id}/scopes | Create Api Auth Server Scope
*APIAuthScopesApi* | [**delete_scope**](docs/APIAuthScopesApi.md#delete_scope) | **DELETE** /api/2/api_authorizations/{api_auth_id}/scopes/{scope_id} | Delete Api Auth Server Scope
*APIAuthScopesApi* | [**get_scopes**](docs/APIAuthScopesApi.md#get_scopes) | **GET** /api/2/api_authorizations/{api_auth_id}/scopes | Get Api Auth Server Scopes
*APIAuthScopesApi* | [**update_scope**](docs/APIAuthScopesApi.md#update_scope) | **PUT** /api/2/api_authorizations/{api_auth_id}/scopes/{scope_id} | Update Api Auth Server Scope
*APIAuthorizationServerApi* | [**create_auth_server**](docs/APIAuthorizationServerApi.md#create_auth_server) | **POST** /api/2/api_authorizations | Create Api Auth Server
*APIAuthorizationServerApi* | [**delete_auth_server**](docs/APIAuthorizationServerApi.md#delete_auth_server) | **DELETE** /api/2/api_authorizations/{api_auth_id} | Delete Api Auth Server
*APIAuthorizationServerApi* | [**get_auth_server**](docs/APIAuthorizationServerApi.md#get_auth_server) | **GET** /api/2/api_authorizations/{api_auth_id} | Get Api Auth Server
*APIAuthorizationServerApi* | [**list_auth_servers**](docs/APIAuthorizationServerApi.md#list_auth_servers) | **GET** /api/2/api_authorizations | List Api Auth Servers
*APIAuthorizationServerApi* | [**update_auth_server**](docs/APIAuthorizationServerApi.md#update_auth_server) | **PUT** /api/2/api_authorizations/{api_auth_id} | Update Api Auth Server
*AppRulesApi* | [**create_app_rule**](docs/AppRulesApi.md#create_app_rule) | **POST** /api/2/apps/{app_id}/rules | 
*AppRulesApi* | [**delete_rule**](docs/AppRulesApi.md#delete_rule) | **DELETE** /api/2/apps/{app_id}/rules/{rule_id} | Delete Rule
*AppRulesApi* | [**get_app_rule**](docs/AppRulesApi.md#get_app_rule) | **GET** /api/2/apps/{app_id}/rules/{rule_id} | Get Rule
*AppRulesApi* | [**list_action_valies**](docs/AppRulesApi.md#list_action_valies) | **GET** /api/2/apps/{app_id}/rules/actions/{rule_action_value}/values | List Actions Values
*AppRulesApi* | [**list_actions**](docs/AppRulesApi.md#list_actions) | **GET** /api/2/apps/{app_id}/rules/actions | List Actions
*AppRulesApi* | [**list_app_rules**](docs/AppRulesApi.md#list_app_rules) | **GET** /api/2/apps/{app_id}/rules | List Rules
*AppRulesApi* | [**list_condition_operators**](docs/AppRulesApi.md#list_condition_operators) | **GET** /api/2/apps/{app_id}/rules/conditions/{rule_condition_value}/operators | List Conditions Operators
*AppRulesApi* | [**list_condition_values**](docs/AppRulesApi.md#list_condition_values) | **GET** /api/2/apps/{app_id}/rules/conditions/{rule_condition_value}/values | List Conditions Values
*AppRulesApi* | [**list_conditions**](docs/AppRulesApi.md#list_conditions) | **GET** /api/2/apps/{app_id}/rules/conditions | List Conditions
*AppRulesApi* | [**sort_app_rules**](docs/AppRulesApi.md#sort_app_rules) | **PUT** /api/2/apps/{app_id}/rules/sort | Bulk Sort
*AppRulesApi* | [**update_app_rule**](docs/AppRulesApi.md#update_app_rule) | **PUT** /api/2/apps/{app_id}/rules/{rule_id} | Update Rule
*AppsApi* | [**create_app**](docs/AppsApi.md#create_app) | **POST** /api/2/apps | Create App
*AppsApi* | [**delete_app**](docs/AppsApi.md#delete_app) | **DELETE** /api/2/apps/{app_id} | Delete App
*AppsApi* | [**delete_app_parameter**](docs/AppsApi.md#delete_app_parameter) | **DELETE** /api/2/apps/{app_id}/parameters/{parameter_id} | Delete Parameter from App
*AppsApi* | [**get_app**](docs/AppsApi.md#get_app) | **GET** /api/2/apps/{app_id} | Get App
*AppsApi* | [**get_app_users**](docs/AppsApi.md#get_app_users) | **GET** /api/2/apps/{app_id}/users | Get App Users
*AppsApi* | [**list_apps**](docs/AppsApi.md#list_apps) | **GET** /api/2/apps | List Apps
*AppsApi* | [**list_connectors**](docs/AppsApi.md#list_connectors) | **GET** /api/2/connectors | List Connectors
*AppsApi* | [**update_app**](docs/AppsApi.md#update_app) | **PUT** /api/2/apps/{app_id} | Update App
*BrandingServiceApi* | [**create_brand**](docs/BrandingServiceApi.md#create_brand) | **POST** /api/2/branding/brands | Create Brand
*BrandingServiceApi* | [**delete_brand**](docs/BrandingServiceApi.md#delete_brand) | **DELETE** /api/2/branding/brands/{brand_id} | Delete Brand
*BrandingServiceApi* | [**get_brand**](docs/BrandingServiceApi.md#get_brand) | **GET** /api/2/branding/brands/{brand_id} | Get Brand
*BrandingServiceApi* | [**get_brand_apps**](docs/BrandingServiceApi.md#get_brand_apps) | **GET** /api/2/branding/brands/{brand_id}/apps | Get Brand Apps
*BrandingServiceApi* | [**list_brands**](docs/BrandingServiceApi.md#list_brands) | **GET** /api/2/branding/brands | List Account Brands
*BrandingServiceApi* | [**update_brand**](docs/BrandingServiceApi.md#update_brand) | **PUT** /api/2/branding/brands/{brand_id} | Update Brand
*BrandingServiceSMTPApi* | [**delete_email_settings**](docs/BrandingServiceSMTPApi.md#delete_email_settings) | **DELETE** /api/2/branding/email_settings | Delete Custom Email Settings
*BrandingServiceSMTPApi* | [**get_email_settings**](docs/BrandingServiceSMTPApi.md#get_email_settings) | **GET** /api/2/branding/email_settings | Get Email Settings
*BrandingServiceSMTPApi* | [**update_email_settings**](docs/BrandingServiceSMTPApi.md#update_email_settings) | **PUT** /api/2/branding/email_settings | Update Email Settings
*BrandingServiceTemplatesApi* | [**create_message_template**](docs/BrandingServiceTemplatesApi.md#create_message_template) | **POST** /api/2/branding/brands/{brand_id}/templates | Create Message Template
*BrandingServiceTemplatesApi* | [**delete_message_template**](docs/BrandingServiceTemplatesApi.md#delete_message_template) | **DELETE** /api/2/branding/brands/{brand_id}/templates/{template_id} | Delete Message Template
*BrandingServiceTemplatesApi* | [**get_master_by_type**](docs/BrandingServiceTemplatesApi.md#get_master_by_type) | **GET** /api/2/branding/brands/master/templates/{template_type} | Get Master Template by Type
*BrandingServiceTemplatesApi* | [**get_message_template_by_id**](docs/BrandingServiceTemplatesApi.md#get_message_template_by_id) | **GET** /api/2/branding/brands/{brand_id}/templates/{template_id} | Get Message Template
*BrandingServiceTemplatesApi* | [**get_template_by_locale**](docs/BrandingServiceTemplatesApi.md#get_template_by_locale) | **GET** /api/2/branding/brands/{brand_id}/templates/{template_type}/{locale} | Get Template by Type &amp; Locale
*BrandingServiceTemplatesApi* | [**list_message_templates**](docs/BrandingServiceTemplatesApi.md#list_message_templates) | **GET** /api/2/branding/brands/{brand_id}/templates | List Message Templates
*BrandingServiceTemplatesApi* | [**update_message_template_by_id**](docs/BrandingServiceTemplatesApi.md#update_message_template_by_id) | **PUT** /api/2/branding/brands/{brand_id}/templates/{template_id} | Update Message Template
*BrandingServiceTemplatesApi* | [**update_template_by_locale**](docs/BrandingServiceTemplatesApi.md#update_template_by_locale) | **PUT** /api/2/branding/brands/{brand_id}/templates/{template_type}/{locale} | Update Template by Type &amp; Locale
*EventsApi* | [**get_event_by_id**](docs/EventsApi.md#get_event_by_id) | **GET** /api/1/events/{event_id} | Get Event by ID
*EventsApi* | [**get_event_types**](docs/EventsApi.md#get_event_types) | **GET** /api/1/events/types | Get Event Types
*EventsApi* | [**get_events**](docs/EventsApi.md#get_events) | **GET** /api/1/events | Get Events
*GroupsApi* | [**get_group_by_id**](docs/GroupsApi.md#get_group_by_id) | **GET** /api/1/groups/{group_id} | Get Group by ID
*GroupsApi* | [**get_groups**](docs/GroupsApi.md#get_groups) | **GET** /api/1/groups | Get Groups
*InviteLinksApi* | [**get_invite_link**](docs/InviteLinksApi.md#get_invite_link) | **POST** /api/1/invites/get_invite_link | Generate Invite Link
*InviteLinksApi* | [**send_invite_link**](docs/InviteLinksApi.md#send_invite_link) | **POST** /api/1/invites/send_invite_link | Send  Invite Link
*MultiFactorAuthenticationApi* | [**create_device_verification**](docs/MultiFactorAuthenticationApi.md#create_device_verification) | **POST** /api/2/mfa/users/{user_id}/verifications | Create Device Verification
*MultiFactorAuthenticationApi* | [**create_factor_registration**](docs/MultiFactorAuthenticationApi.md#create_factor_registration) | **POST** /api/2/mfa/users/{user_id}/registrations | Create Factor Registration
*MultiFactorAuthenticationApi* | [**delete_enrolled_factor**](docs/MultiFactorAuthenticationApi.md#delete_enrolled_factor) | **DELETE** /api/2/mfa/users/{user_id}/devices/{device_id} | Delete Enrolled Factor
*MultiFactorAuthenticationApi* | [**generate_otp**](docs/MultiFactorAuthenticationApi.md#generate_otp) | **POST** /api/2/mfa/users/{user_id}/mfa_token | Generate MFA token
*MultiFactorAuthenticationApi* | [**get_auth_factors**](docs/MultiFactorAuthenticationApi.md#get_auth_factors) | **GET** /api/2/mfa/users/{user_id}/factors | Get User Factors
*MultiFactorAuthenticationApi* | [**get_authentication_devices**](docs/MultiFactorAuthenticationApi.md#get_authentication_devices) | **GET** /api/2/mfa/users/{user_id}/devices | Get User Devices
*MultiFactorAuthenticationApi* | [**get_user_registration**](docs/MultiFactorAuthenticationApi.md#get_user_registration) | **GET** /api/2/mfa/users/{user_id}/registrations/{registration_id} | Get User Registration
*MultiFactorAuthenticationApi* | [**get_user_verification**](docs/MultiFactorAuthenticationApi.md#get_user_verification) | **GET** /api/2/mfa/users/{user_id}/verifications/{verification_id} | Get User Verification
*MultiFactorAuthenticationApi* | [**verify_user_registration**](docs/MultiFactorAuthenticationApi.md#verify_user_registration) | **PUT** /api/2/mfa/users/{user_id}/registrations/{registration_id} | Verify User Registration
*MultiFactorAuthenticationApi* | [**verify_user_verification**](docs/MultiFactorAuthenticationApi.md#verify_user_verification) | **PUT** /api/2/mfa/users/{user_id}/verifications/{verification_id} | Verify User Verification
*MultiFactorAuthenticationV1Api* | [**activate_mfa_factors**](docs/MultiFactorAuthenticationV1Api.md#activate_mfa_factors) | **POST** /api/1/users/{user_id}/otp_devices/{device_id}/trigger | Activate a Factor
*MultiFactorAuthenticationV1Api* | [**enroll_mfa_factor**](docs/MultiFactorAuthenticationV1Api.md#enroll_mfa_factor) | **POST** /api/1/users/{user_id}/otp_devices | Enroll a Factor
*MultiFactorAuthenticationV1Api* | [**generate_mf_atoken**](docs/MultiFactorAuthenticationV1Api.md#generate_mf_atoken) | **POST** /api/1/users/{user_id}/mfa_token | Generate Temp MFA Token
*MultiFactorAuthenticationV1Api* | [**get_enrolled_factors**](docs/MultiFactorAuthenticationV1Api.md#get_enrolled_factors) | **GET** /api/1/users/{user_id}/otp_devices | Get Enrolled Factors
*MultiFactorAuthenticationV1Api* | [**get_mfa_factors**](docs/MultiFactorAuthenticationV1Api.md#get_mfa_factors) | **GET** /api/1/users/{user_id}/auth_factor | Get Available Factors
*MultiFactorAuthenticationV1Api* | [**remove_mfa_factors**](docs/MultiFactorAuthenticationV1Api.md#remove_mfa_factors) | **DELETE** /api/1/users/{user_id}/otp_devices/{device_id} | Remove an Enrolled Factor
*MultiFactorAuthenticationV1Api* | [**verify_mfa_factor**](docs/MultiFactorAuthenticationV1Api.md#verify_mfa_factor) | **POST** /api/1/users/{user_id}/otp_devices/{device_id}/verify | Verify a Factor
*OAuth2Api* | [**generate_token**](docs/OAuth2Api.md#generate_token) | **POST** /auth/oauth2/v2/token | Generate Token
*OAuth2Api* | [**get_rate_limit**](docs/OAuth2Api.md#get_rate_limit) | **GET** /auth/rate_limit | Get Rate Limit
*OAuth2Api* | [**revoke_tokens**](docs/OAuth2Api.md#revoke_tokens) | **POST** /auth/oauth2/revoke | Revoke Tokens
*PrivilegesApi* | [**add_privilege_to_role**](docs/PrivilegesApi.md#add_privilege_to_role) | **POST** /api/1/privileges/{privilege_id}/roles | Assign a Privilege to Roles
*PrivilegesApi* | [**assign_users_to_privilege**](docs/PrivilegesApi.md#assign_users_to_privilege) | **POST** /api/1/privileges/{privilege_id}/users | Assign Users to a Privilege
*PrivilegesApi* | [**create_privilege**](docs/PrivilegesApi.md#create_privilege) | **POST** /api/1/privileges | Create a Privilege
*PrivilegesApi* | [**delete_privilege**](docs/PrivilegesApi.md#delete_privilege) | **DELETE** /api/1/privileges/{privilege_id} | Delete a Privilege
*PrivilegesApi* | [**delete_role_from_privilege**](docs/PrivilegesApi.md#delete_role_from_privilege) | **DELETE** /api/1/privileges/{privilege_id}/roles/{role_id} | Remove a Privilege from a Role
*PrivilegesApi* | [**get_assigned_user**](docs/PrivilegesApi.md#get_assigned_user) | **GET** /api/1/privileges/{privilege_id}/users | Get Users assigned to a Privilege
*PrivilegesApi* | [**get_privilege**](docs/PrivilegesApi.md#get_privilege) | **GET** /api/1/privileges/{privilege_id} | Get a Privilege
*PrivilegesApi* | [**list_privelege_roles**](docs/PrivilegesApi.md#list_privelege_roles) | **GET** /api/1/privileges/{privilege_id}/roles | Get Roles assigned to Privilege
*PrivilegesApi* | [**list_priveleges**](docs/PrivilegesApi.md#list_priveleges) | **GET** /api/1/privileges | List Privileges
*PrivilegesApi* | [**remove_user_from_privilege**](docs/PrivilegesApi.md#remove_user_from_privilege) | **DELETE** /api/1/privileges/{privilege_id}/users/{user_id} | Remove a Privilege from Users
*PrivilegesApi* | [**update_privilege**](docs/PrivilegesApi.md#update_privilege) | **PUT** /api/1/privileges/{privilege_id} | Update a Privilege
*RolesApi* | [**add_role_admins**](docs/RolesApi.md#add_role_admins) | **POST** /api/2/roles/{role_id}/admins | Add Role Admins
*RolesApi* | [**add_role_users**](docs/RolesApi.md#add_role_users) | **POST** /api/2/roles/{role_id}/users | Add Role Users
*RolesApi* | [**create_roles**](docs/RolesApi.md#create_roles) | **POST** /api/2/roles | Create Role
*RolesApi* | [**delete_role**](docs/RolesApi.md#delete_role) | **DELETE** /api/2/roles/{role_id} | Delete Role by ID
*RolesApi* | [**get_role**](docs/RolesApi.md#get_role) | **GET** /api/2/roles/{role_id} | Get Role by ID
*RolesApi* | [**get_role_admins**](docs/RolesApi.md#get_role_admins) | **GET** /api/2/roles/{role_id}/admins | Get Role Admins
*RolesApi* | [**get_role_apps**](docs/RolesApi.md#get_role_apps) | **GET** /api/2/roles/{role_id}/apps | Get all Apps assigned to Role
*RolesApi* | [**get_role_by_id**](docs/RolesApi.md#get_role_by_id) | **GET** /api/1/roles/{role_id} | Get Role by ID
*RolesApi* | [**get_role_by_name**](docs/RolesApi.md#get_role_by_name) | **GET** /api/1/roles | Get Role by Name
*RolesApi* | [**get_role_users**](docs/RolesApi.md#get_role_users) | **GET** /api/2/roles/{role_id}/users | Get Role Users
*RolesApi* | [**list_roles**](docs/RolesApi.md#list_roles) | **GET** /api/2/roles | List Roles
*RolesApi* | [**remove_role_admins**](docs/RolesApi.md#remove_role_admins) | **DELETE** /api/2/roles/{role_id}/admins | Remove Role Admins
*RolesApi* | [**remove_role_users**](docs/RolesApi.md#remove_role_users) | **DELETE** /api/2/roles/{role_id}/users | Remove Role Users
*RolesApi* | [**set_role_apps**](docs/RolesApi.md#set_role_apps) | **PUT** /api/2/roles/{role_id}/apps | Set Role Apps
*RolesApi* | [**update_role**](docs/RolesApi.md#update_role) | **PUT** /api/2/roles/{role_id} | Update Role
*SAMLAssertionsApi* | [**generate_saml_assert**](docs/SAMLAssertionsApi.md#generate_saml_assert) | **POST** /api/1/saml_assertion | Generate SAML Assertion
*SAMLAssertionsApi* | [**generate_saml_assert2**](docs/SAMLAssertionsApi.md#generate_saml_assert2) | **POST** /api/2/saml_assertion | Generate SAML Assertion
*SAMLAssertionsApi* | [**ver_factor_saml**](docs/SAMLAssertionsApi.md#ver_factor_saml) | **POST** /api/1/saml_assertion/verify_factor | Verify Factor SAML
*SAMLAssertionsApi* | [**ver_factor_saml2**](docs/SAMLAssertionsApi.md#ver_factor_saml2) | **POST** /api/2/saml_assertion/verify_factor | Verify Factor SAML
*UserMappingsApi* | [**create_mapping**](docs/UserMappingsApi.md#create_mapping) | **POST** /api/2/mappings | Create Mapping
*UserMappingsApi* | [**delete_mapping**](docs/UserMappingsApi.md#delete_mapping) | **DELETE** /api/2/mappings/{mapping_id} | Delete Mapping
*UserMappingsApi* | [**get_mapping**](docs/UserMappingsApi.md#get_mapping) | **GET** /api/2/mappings/{mapping_id} | Get Mapping
*UserMappingsApi* | [**list_mapping_action_values**](docs/UserMappingsApi.md#list_mapping_action_values) | **GET** /api/2/mappings/actions/{mapping_action_value}/values | List Actions Values
*UserMappingsApi* | [**list_mapping_conditions**](docs/UserMappingsApi.md#list_mapping_conditions) | **GET** /api/2/mappings/conditions | List Conditions
*UserMappingsApi* | [**list_mapping_conditions_operators**](docs/UserMappingsApi.md#list_mapping_conditions_operators) | **GET** /api/2/mappings/conditions/{mapping_condition_value}/operators | List Conditions Operators
*UserMappingsApi* | [**list_mapping_contion_values**](docs/UserMappingsApi.md#list_mapping_contion_values) | **GET** /api/2/mappings/conditions/{mapping_condition_value}/values | List Conditions Values
*UserMappingsApi* | [**list_mappings**](docs/UserMappingsApi.md#list_mappings) | **GET** /api/2/mappings | List Mappings
*UserMappingsApi* | [**list_mappings_actions**](docs/UserMappingsApi.md#list_mappings_actions) | **GET** /api/2/mappings/actions | List Actions
*UserMappingsApi* | [**sort_mappings**](docs/UserMappingsApi.md#sort_mappings) | **PUT** /api/2/mappings/sort | Bulk Sort
*UserMappingsApi* | [**update_mapping**](docs/UserMappingsApi.md#update_mapping) | **PUT** /api/2/mappings/{mapping_id} | Update Mapping
*UsersV1Api* | [**add_roles_to_user**](docs/UsersV1Api.md#add_roles_to_user) | **PUT** /api/1/users/{user_id}/add_roles | Add Roles for a User
*UsersV1Api* | [**create_user**](docs/UsersV1Api.md#create_user) | **POST** /api/1/users | Create a User
*UsersV1Api* | [**delete_user**](docs/UsersV1Api.md#delete_user) | **DELETE** /api/1/users/{user_id} | Delete a User
*UsersV1Api* | [**get_custom_attributes**](docs/UsersV1Api.md#get_custom_attributes) | **GET** /api/1/users/custom_attributes | Get Custom Attributes
*UsersV1Api* | [**get_user_apps**](docs/UsersV1Api.md#get_user_apps) | **GET** /api/1/users/{user_id}/apps | Get Apps for a User
*UsersV1Api* | [**get_user_by_id**](docs/UsersV1Api.md#get_user_by_id) | **GET** /api/1/users/{user_id} | Get User by ID
*UsersV1Api* | [**get_user_roles**](docs/UsersV1Api.md#get_user_roles) | **GET** /api/1/users/{user_id}/roles | Get Roles for a User
*UsersV1Api* | [**list_users**](docs/UsersV1Api.md#list_users) | **GET** /api/1/users | List Users
*UsersV1Api* | [**lock_account_user**](docs/UsersV1Api.md#lock_account_user) | **PUT** /api/1/users/{user_id}/lock_user | Lock User Account
*UsersV1Api* | [**log_out_user**](docs/UsersV1Api.md#log_out_user) | **PUT** /api/1/users/{user_id}/logout | Log User Out
*UsersV1Api* | [**remove_user_role**](docs/UsersV1Api.md#remove_user_role) | **PUT** /api/1/users/{user_id}/remove_roles | Remove Roles for a User
*UsersV1Api* | [**set_user_state**](docs/UsersV1Api.md#set_user_state) | **PUT** /api/1/users/{user_id}/set_state | Set User State
*UsersV1Api* | [**update_password_insecure**](docs/UsersV1Api.md#update_password_insecure) | **PUT** /api/1/users/set_password_clear_text/{user_id} | Set Password Using ID in Cleartext
*UsersV1Api* | [**update_password_secure**](docs/UsersV1Api.md#update_password_secure) | **PUT** /api/1/users/set_password_using_salt/{user_id} | Set Password Using ID and SHA-256 and Salt
*UsersV1Api* | [**update_user**](docs/UsersV1Api.md#update_user) | **PUT** /api/1/users/{user_id} | Update a User
*UsersV2Api* | [**create_user2**](docs/UsersV2Api.md#create_user2) | **POST** /api/2/users | Create User
*UsersV2Api* | [**delete_user2**](docs/UsersV2Api.md#delete_user2) | **DELETE** /api/2/users/{user_id} | Delete User
*UsersV2Api* | [**get_user2**](docs/UsersV2Api.md#get_user2) | **GET** /api/2/users/{user_id} | Get User
*UsersV2Api* | [**get_user_apps2**](docs/UsersV2Api.md#get_user_apps2) | **GET** /api/2/users/{user_id}/apps | Get User Apps
*UsersV2Api* | [**list_users2**](docs/UsersV2Api.md#list_users2) | **GET** /api/2/users | List Users
*UsersV2Api* | [**update_user2**](docs/UsersV2Api.md#update_user2) | **PUT** /api/2/users/{user_id} | Update User
*VigilanceAIApi* | [**create_risk_rule**](docs/VigilanceAIApi.md#create_risk_rule) | **POST** /api/2/risk/rules | Create Rule
*VigilanceAIApi* | [**delete_risk_rule**](docs/VigilanceAIApi.md#delete_risk_rule) | **DELETE** /api/2/risk/rules/{rule_id} | Delete Rule
*VigilanceAIApi* | [**get_risk_rule**](docs/VigilanceAIApi.md#get_risk_rule) | **GET** /api/2/risk/rules/{rule_id} | get Risk Rule
*VigilanceAIApi* | [**get_risk_score**](docs/VigilanceAIApi.md#get_risk_score) | **POST** /api/2/risk/verify | Get a Risk Score
*VigilanceAIApi* | [**get_risk_scores**](docs/VigilanceAIApi.md#get_risk_scores) | **GET** /api/2/risk/scores | Get Score Summary
*VigilanceAIApi* | [**list_risk_rules**](docs/VigilanceAIApi.md#list_risk_rules) | **GET** /api/2/risk/rules | List Rules
*VigilanceAIApi* | [**track_risk_event**](docs/VigilanceAIApi.md#track_risk_event) | **POST** /api/2/risk/events | Track an Event
*VigilanceAIApi* | [**update_risk_rule**](docs/VigilanceAIApi.md#update_risk_rule) | **PUT** /api/2/risk/rules/{rule_id} | Update Rule


## Documentation For Models

 - [ActivateMfaFactorsRequest](docs/ActivateMfaFactorsRequest.md)
 - [AddClientApp201Response](docs/AddClientApp201Response.md)
 - [AddClientAppRequest](docs/AddClientAppRequest.md)
 - [AddPrivilegeToRole201Response](docs/AddPrivilegeToRole201Response.md)
 - [AddPrivilegeToRoleRequest](docs/AddPrivilegeToRoleRequest.md)
 - [AddRolesToUserRequest](docs/AddRolesToUserRequest.md)
 - [AssignUsersToPrivilegeRequest](docs/AssignUsersToPrivilegeRequest.md)
 - [CreateAppRequest](docs/CreateAppRequest.md)
 - [CreateAppRequestOneOf](docs/CreateAppRequestOneOf.md)
 - [CreateAppRequestOneOf1](docs/CreateAppRequestOneOf1.md)
 - [CreateAppRequestOneOf1Configuration](docs/CreateAppRequestOneOf1Configuration.md)
 - [CreateAppRequestOneOf1Parameters](docs/CreateAppRequestOneOf1Parameters.md)
 - [CreateAppRequestOneOf1ParametersSamlUsername](docs/CreateAppRequestOneOf1ParametersSamlUsername.md)
 - [CreateAppRequestOneOfConfiguration](docs/CreateAppRequestOneOfConfiguration.md)
 - [CreateAuthClaimRequest](docs/CreateAuthClaimRequest.md)
 - [CreateBrand201Response](docs/CreateBrand201Response.md)
 - [CreateBrand201ResponseBackground](docs/CreateBrand201ResponseBackground.md)
 - [CreateBrand201ResponseBackgroundUrls](docs/CreateBrand201ResponseBackgroundUrls.md)
 - [CreateBrand201ResponseLogo](docs/CreateBrand201ResponseLogo.md)
 - [CreateBrand201ResponseLogoUrls](docs/CreateBrand201ResponseLogoUrls.md)
 - [CreateBrandRequest](docs/CreateBrandRequest.md)
 - [CreateDeviceVerification201Response](docs/CreateDeviceVerification201Response.md)
 - [CreateDeviceVerificationRequest](docs/CreateDeviceVerificationRequest.md)
 - [CreateFactorRegistration201Response](docs/CreateFactorRegistration201Response.md)
 - [CreateFactorRegistrationRequest](docs/CreateFactorRegistrationRequest.md)
 - [CreateMessageTemplateRequest](docs/CreateMessageTemplateRequest.md)
 - [CreateMessageTemplateRequestTemplate](docs/CreateMessageTemplateRequestTemplate.md)
 - [CreateMessageTemplateRequestTemplateOneOf](docs/CreateMessageTemplateRequestTemplateOneOf.md)
 - [CreateMessageTemplateRequestTemplateOneOf1](docs/CreateMessageTemplateRequestTemplateOneOf1.md)
 - [CreateMessageTemplateRequestTemplateOneOf1AllOf](docs/CreateMessageTemplateRequestTemplateOneOf1AllOf.md)
 - [CreateMessageTemplateRequestTemplateOneOfAllOf](docs/CreateMessageTemplateRequestTemplateOneOfAllOf.md)
 - [CreatePrivilege200Response](docs/CreatePrivilege200Response.md)
 - [CreateRoles201ResponseInner](docs/CreateRoles201ResponseInner.md)
 - [CreateScope200Response](docs/CreateScope200Response.md)
 - [CreateScopeRequest](docs/CreateScopeRequest.md)
 - [EnrollMfaFactor200Response](docs/EnrollMfaFactor200Response.md)
 - [EnrollMfaFactorRequest](docs/EnrollMfaFactorRequest.md)
 - [GenerateMFAtoken200Response](docs/GenerateMFAtoken200Response.md)
 - [GenerateMFAtokenRequest](docs/GenerateMFAtokenRequest.md)
 - [GenerateOTP201Response](docs/GenerateOTP201Response.md)
 - [GenerateOTPRequest](docs/GenerateOTPRequest.md)
 - [GenerateSamlAssert200Response](docs/GenerateSamlAssert200Response.md)
 - [GenerateSamlAssertRequest](docs/GenerateSamlAssertRequest.md)
 - [GenerateToken200Response](docs/GenerateToken200Response.md)
 - [GenerateToken400Response](docs/GenerateToken400Response.md)
 - [GenerateTokenRequest](docs/GenerateTokenRequest.md)
 - [GetAssignedUser200Response](docs/GetAssignedUser200Response.md)
 - [GetAuthFactors200Response](docs/GetAuthFactors200Response.md)
 - [GetAuthclaims200ResponseInner](docs/GetAuthclaims200ResponseInner.md)
 - [GetAuthenticationDevices200ResponseInner](docs/GetAuthenticationDevices200ResponseInner.md)
 - [GetBrandApps200ResponseInner](docs/GetBrandApps200ResponseInner.md)
 - [GetCustomAttributes200Response](docs/GetCustomAttributes200Response.md)
 - [GetEmailSettings200Response](docs/GetEmailSettings200Response.md)
 - [GetEmailSettings200ResponseOneOf](docs/GetEmailSettings200ResponseOneOf.md)
 - [GetEmailSettings200ResponseOneOf1](docs/GetEmailSettings200ResponseOneOf1.md)
 - [GetEnrolledFactors200Response](docs/GetEnrolledFactors200Response.md)
 - [GetEnrolledFactors200ResponseData](docs/GetEnrolledFactors200ResponseData.md)
 - [GetEnrolledFactors200ResponseDataOtpDevicesInner](docs/GetEnrolledFactors200ResponseDataOtpDevicesInner.md)
 - [GetEventById200Response](docs/GetEventById200Response.md)
 - [GetEventById200ResponseStatus](docs/GetEventById200ResponseStatus.md)
 - [GetEventTypes200Response](docs/GetEventTypes200Response.md)
 - [GetEventTypes200ResponseDataInner](docs/GetEventTypes200ResponseDataInner.md)
 - [GetEvents200Response](docs/GetEvents200Response.md)
 - [GetEvents200ResponseDataInner](docs/GetEvents200ResponseDataInner.md)
 - [GetEvents200ResponsePagination](docs/GetEvents200ResponsePagination.md)
 - [GetGroups200Response](docs/GetGroups200Response.md)
 - [GetGroups200ResponseDataInner](docs/GetGroups200ResponseDataInner.md)
 - [GetInviteLink200Response](docs/GetInviteLink200Response.md)
 - [GetInviteLinkRequest](docs/GetInviteLinkRequest.md)
 - [GetMFAFactors200Response](docs/GetMFAFactors200Response.md)
 - [GetMFAFactors200ResponseData](docs/GetMFAFactors200ResponseData.md)
 - [GetMFAFactors200ResponseDataAuthFactorsInner](docs/GetMFAFactors200ResponseDataAuthFactorsInner.md)
 - [GetRateLimit200Response](docs/GetRateLimit200Response.md)
 - [GetRateLimit200ResponseData](docs/GetRateLimit200ResponseData.md)
 - [GetRiskScore200Response](docs/GetRiskScore200Response.md)
 - [GetRiskScoreRequest](docs/GetRiskScoreRequest.md)
 - [GetRiskScores200Response](docs/GetRiskScores200Response.md)
 - [GetRiskScores200ResponseScores](docs/GetRiskScores200ResponseScores.md)
 - [GetRoleApps200ResponseInner](docs/GetRoleApps200ResponseInner.md)
 - [GetRoleById200Response](docs/GetRoleById200Response.md)
 - [GetRoleById200ResponseDataInner](docs/GetRoleById200ResponseDataInner.md)
 - [GetRoleByName200Response](docs/GetRoleByName200Response.md)
 - [GetRoleByName200ResponseDataInner](docs/GetRoleByName200ResponseDataInner.md)
 - [GetRoleByName200ResponsePagination](docs/GetRoleByName200ResponsePagination.md)
 - [GetScopes200ResponseInner](docs/GetScopes200ResponseInner.md)
 - [GetScopes200ResponseInnerConfiguration](docs/GetScopes200ResponseInnerConfiguration.md)
 - [GetScopes401Response](docs/GetScopes401Response.md)
 - [GetUserApps200ResponseInner](docs/GetUserApps200ResponseInner.md)
 - [GetUserRoles200Response](docs/GetUserRoles200Response.md)
 - [GetUserVerification200Response](docs/GetUserVerification200Response.md)
 - [ListActions200ResponseInner](docs/ListActions200ResponseInner.md)
 - [ListAppRules200ResponseInner](docs/ListAppRules200ResponseInner.md)
 - [ListApps200ResponseInner](docs/ListApps200ResponseInner.md)
 - [ListApps200ResponseInnerProvisioning](docs/ListApps200ResponseInnerProvisioning.md)
 - [ListBrands200ResponseInner](docs/ListBrands200ResponseInner.md)
 - [ListClientApps200Response](docs/ListClientApps200Response.md)
 - [ListClientApps200ResponseScopesInner](docs/ListClientApps200ResponseScopesInner.md)
 - [ListConditionOperators200ResponseInner](docs/ListConditionOperators200ResponseInner.md)
 - [ListConditions200ResponseInner](docs/ListConditions200ResponseInner.md)
 - [ListConnectors200Response](docs/ListConnectors200Response.md)
 - [ListMappingActionValues200ResponseInner](docs/ListMappingActionValues200ResponseInner.md)
 - [ListMappingConditions200Response](docs/ListMappingConditions200Response.md)
 - [ListMappingConditionsOperators200ResponseInner](docs/ListMappingConditionsOperators200ResponseInner.md)
 - [ListMappingContionValues200ResponseInner](docs/ListMappingContionValues200ResponseInner.md)
 - [ListMappings200ResponseInner](docs/ListMappings200ResponseInner.md)
 - [ListMappings200ResponseInnerActionsInner](docs/ListMappings200ResponseInnerActionsInner.md)
 - [ListMappings200ResponseInnerConditionsInner](docs/ListMappings200ResponseInnerConditionsInner.md)
 - [ListMappingsActions200ResponseInner](docs/ListMappingsActions200ResponseInner.md)
 - [ListMessageTemplates200ResponseInner](docs/ListMessageTemplates200ResponseInner.md)
 - [ListPrivelegeRoles200Response](docs/ListPrivelegeRoles200Response.md)
 - [ListPriveleges200ResponseInner](docs/ListPriveleges200ResponseInner.md)
 - [ListPriveleges200ResponseInnerPrivilege](docs/ListPriveleges200ResponseInnerPrivilege.md)
 - [ListPriveleges200ResponseInnerPrivilegeStatementInner](docs/ListPriveleges200ResponseInnerPrivilegeStatementInner.md)
 - [ListRiskRules200ResponseInner](docs/ListRiskRules200ResponseInner.md)
 - [ListRiskRules200ResponseInnerSource](docs/ListRiskRules200ResponseInnerSource.md)
 - [ListRoles200ResponseInner](docs/ListRoles200ResponseInner.md)
 - [ListUsers200ResponseInner](docs/ListUsers200ResponseInner.md)
 - [LockAccountUserRequest](docs/LockAccountUserRequest.md)
 - [RemoveRoleUsersRequest](docs/RemoveRoleUsersRequest.md)
 - [RemoveUserRoleRequest](docs/RemoveUserRoleRequest.md)
 - [RemoveUserRoleRequestRoleIdArrayInner](docs/RemoveUserRoleRequestRoleIdArrayInner.md)
 - [RevokeTokensRequest](docs/RevokeTokensRequest.md)
 - [SendInviteLink200Response](docs/SendInviteLink200Response.md)
 - [SendInviteLinkRequest](docs/SendInviteLinkRequest.md)
 - [SetUserStateRequest](docs/SetUserStateRequest.md)
 - [TrackRiskEventRequest](docs/TrackRiskEventRequest.md)
 - [TrackRiskEventRequestDevice](docs/TrackRiskEventRequestDevice.md)
 - [TrackRiskEventRequestSession](docs/TrackRiskEventRequestSession.md)
 - [TrackRiskEventRequestUser](docs/TrackRiskEventRequestUser.md)
 - [UpdateClientAppRequest](docs/UpdateClientAppRequest.md)
 - [UpdatePasswordInsecureRequest](docs/UpdatePasswordInsecureRequest.md)
 - [UpdatePasswordSecureRequest](docs/UpdatePasswordSecureRequest.md)
 - [UpdatePrivilege200Response](docs/UpdatePrivilege200Response.md)
 - [UpdateRiskRuleRequest](docs/UpdateRiskRuleRequest.md)
 - [VerFactorSaml200Response](docs/VerFactorSaml200Response.md)
 - [VerFactorSamlRequest](docs/VerFactorSamlRequest.md)
 - [VerifyMfaFactorRequest](docs/VerifyMfaFactorRequest.md)
 - [VerifyUserRegistration200Response](docs/VerifyUserRegistration200Response.md)
 - [VerifyUserRegistrationRequest](docs/VerifyUserRegistrationRequest.md)
 - [VerifyUserVerificationRequest](docs/VerifyUserVerificationRequest.md)


## Documentation For Authorization


## OAuth2

- **Type**: OAuth
- **Flow**: application
- **Authorization URL**: 
- **Scopes**: 
 - **Authentication Only**: Gives the credential pair the ability to generate an access token that can perform POST calls only to authentication endpoints, providing least privileged access to authentication code. These endpoints include:   - Verify Factor (SAML Assertion)   - Generate SAML Assertion   - Verify Factor (Login)   - Create Session Login Token   - Log User Out
 - **Read Users**: Gives the credential pair the ability to generate an access token that can perform GET calls available for the User, Role, and Group API resources.
 - **Manage users**: Gives the credential pair the ability to generate an access token that can perform GET, POST, PUT, and DELETE calls available for the User, Role, and Group API resources, with the exception of setting passwords and assigning and removing roles
 - **Manage All**: Gives the credential pair the ability to generate an access token that can perform GET, POST, PUT, and DELETE calls for all available API resources, including the ability to set passwords and assign and remove roles.
 - **Read All**: Gives the credential pair the ability to generate an access token that can perform GET calls available for all API resources.


## basicAuth

- **Type**: HTTP basic authentication


## Author




