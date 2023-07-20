# coding: utf-8

"""
    OneLogin API

    OpenAPI Specification for OneLogin  # noqa: E501

    The version of the OpenAPI document: 3.1.1
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from onelogin import schemas  # noqa: F401


class Privilege(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "name",
            "privilege",
        }
        
        class properties:
            name = schemas.StrSchema
            
            
            class privilege(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        Version = schemas.StrSchema
                        
                        
                        class Statement(
                            schemas.ListSchema
                        ):
                        
                        
                            class MetaOapg:
                                
                                
                                class items(
                                    schemas.DictSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        required = {
                                            "Action",
                                            "Scope",
                                            "Effect",
                                        }
                                        
                                        class properties:
                                            Effect = schemas.StrSchema
                                            
                                            
                                            class Action(
                                                schemas.ListSchema
                                            ):
                                            
                                            
                                                class MetaOapg:
                                                    
                                                    
                                                    class items(
                                                        schemas.EnumBase,
                                                        schemas.StrSchema
                                                    ):
                                                        
                                                        @schemas.classproperty
                                                        def APPSCREATE(cls):
                                                            return cls("Apps:Create")
                                                        
                                                        @schemas.classproperty
                                                        def APPSDELETE(cls):
                                                            return cls("Apps:Delete")
                                                        
                                                        @schemas.classproperty
                                                        def APPSLIST(cls):
                                                            return cls("Apps:List")
                                                        
                                                        @schemas.classproperty
                                                        def APPSGET(cls):
                                                            return cls("Apps:Get")
                                                        
                                                        @schemas.classproperty
                                                        def APPSUPDATE(cls):
                                                            return cls("Apps:Update")
                                                        
                                                        @schemas.classproperty
                                                        def APPSMANAGE_CONNECTORS(cls):
                                                            return cls("Apps:ManageConnectors")
                                                        
                                                        @schemas.classproperty
                                                        def APPSMANAGE_ROLES(cls):
                                                            return cls("Apps:ManageRoles")
                                                        
                                                        @schemas.classproperty
                                                        def APPSMANAGE_TABS(cls):
                                                            return cls("Apps:ManageTabs")
                                                        
                                                        @schemas.classproperty
                                                        def APPSMANAGE_USERS(cls):
                                                            return cls("Apps:ManageUsers")
                                                        
                                                        @schemas.classproperty
                                                        def APPSREAPPLY_MAPPINGS(cls):
                                                            return cls("Apps:ReapplyMappings")
                                                        
                                                        @schemas.classproperty
                                                        def USERSCREATE(cls):
                                                            return cls("Users:Create")
                                                        
                                                        @schemas.classproperty
                                                        def USERSDELETE(cls):
                                                            return cls("Users:Delete")
                                                        
                                                        @schemas.classproperty
                                                        def USERSLIST(cls):
                                                            return cls("Users:List")
                                                        
                                                        @schemas.classproperty
                                                        def USERSGET(cls):
                                                            return cls("Users:Get")
                                                        
                                                        @schemas.classproperty
                                                        def USERSUPDATE(cls):
                                                            return cls("Users:Update")
                                                        
                                                        @schemas.classproperty
                                                        def USERSASSUME_USER(cls):
                                                            return cls("Users:AssumeUser")
                                                        
                                                        @schemas.classproperty
                                                        def USERSMANAGE_APPS(cls):
                                                            return cls("Users:ManageApps")
                                                        
                                                        @schemas.classproperty
                                                        def USERSUNLOCK(cls):
                                                            return cls("Users:Unlock")
                                                        
                                                        @schemas.classproperty
                                                        def USERSGENERATE_TEMP_MFA_TOKEN(cls):
                                                            return cls("Users:GenerateTempMfaToken")
                                                        
                                                        @schemas.classproperty
                                                        def USERSRESET_PASSWORD(cls):
                                                            return cls("Users:ResetPassword")
                                                        
                                                        @schemas.classproperty
                                                        def USERSREAPPLY_MAPPINGS(cls):
                                                            return cls("Users:ReapplyMappings")
                                                        
                                                        @schemas.classproperty
                                                        def USERSMANAGE_LICENSE(cls):
                                                            return cls("Users:ManageLicense")
                                                        
                                                        @schemas.classproperty
                                                        def USERSINVITE(cls):
                                                            return cls("Users:Invite")
                                                        
                                                        @schemas.classproperty
                                                        def USERSMANAGE_ROLES(cls):
                                                            return cls("Users:ManageRoles")
                                                        
                                                        @schemas.classproperty
                                                        def ROLESCREATE(cls):
                                                            return cls("Roles:Create")
                                                        
                                                        @schemas.classproperty
                                                        def ROLESGET(cls):
                                                            return cls("Roles:Get")
                                                        
                                                        @schemas.classproperty
                                                        def ROLESLIST(cls):
                                                            return cls("Roles:List")
                                                        
                                                        @schemas.classproperty
                                                        def ROLESUPDATE(cls):
                                                            return cls("Roles:Update")
                                                        
                                                        @schemas.classproperty
                                                        def ROLESDELETE(cls):
                                                            return cls("Roles:Delete")
                                                        
                                                        @schemas.classproperty
                                                        def ROLESMANAGE_USERS(cls):
                                                            return cls("Roles:ManageUsers")
                                                        
                                                        @schemas.classproperty
                                                        def ROLESMANAGE_APPS(cls):
                                                            return cls("Roles:ManageApps")
                                                        
                                                        @schemas.classproperty
                                                        def REPORTSCREATE(cls):
                                                            return cls("Reports:Create")
                                                        
                                                        @schemas.classproperty
                                                        def REPORTSGET(cls):
                                                            return cls("Reports:Get")
                                                        
                                                        @schemas.classproperty
                                                        def REPORTSLIST(cls):
                                                            return cls("Reports:List")
                                                        
                                                        @schemas.classproperty
                                                        def REPORTSUPDATE(cls):
                                                            return cls("Reports:Update")
                                                        
                                                        @schemas.classproperty
                                                        def REPORTSDELETE(cls):
                                                            return cls("Reports:Delete")
                                                        
                                                        @schemas.classproperty
                                                        def REPORTSCLONE(cls):
                                                            return cls("Reports:Clone")
                                                        
                                                        @schemas.classproperty
                                                        def EVENTSGET(cls):
                                                            return cls("Events:Get")
                                                        
                                                        @schemas.classproperty
                                                        def EVENTSLIST(cls):
                                                            return cls("Events:List")
                                                        
                                                        @schemas.classproperty
                                                        def GROUPSCREATE(cls):
                                                            return cls("Groups:Create")
                                                        
                                                        @schemas.classproperty
                                                        def GROUPSGET(cls):
                                                            return cls("Groups:Get")
                                                        
                                                        @schemas.classproperty
                                                        def GROUPSLIST(cls):
                                                            return cls("Groups:List")
                                                        
                                                        @schemas.classproperty
                                                        def GROUPSUPDATE(cls):
                                                            return cls("Groups:Update")
                                                        
                                                        @schemas.classproperty
                                                        def GROUPSDELETE(cls):
                                                            return cls("Groups:Delete")
                                                        
                                                        @schemas.classproperty
                                                        def POLICIESCREATE(cls):
                                                            return cls("Policies:Create")
                                                        
                                                        @schemas.classproperty
                                                        def POLICIESGET(cls):
                                                            return cls("Policies:Get")
                                                        
                                                        @schemas.classproperty
                                                        def POLICIESLIST(cls):
                                                            return cls("Policies:List")
                                                        
                                                        @schemas.classproperty
                                                        def POLICIESUPDATE(cls):
                                                            return cls("Policies:Update")
                                                        
                                                        @schemas.classproperty
                                                        def POLICIESDELETE(cls):
                                                            return cls("Policies:Delete")
                                                        
                                                        @schemas.classproperty
                                                        def POLICIESSET_DEFAULT(cls):
                                                            return cls("Policies:SetDefault")
                                            
                                                def __new__(
                                                    cls,
                                                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                                ) -> 'Action':
                                                    return super().__new__(
                                                        cls,
                                                        _arg,
                                                        _configuration=_configuration,
                                                    )
                                            
                                                def __getitem__(self, i: int) -> MetaOapg.items:
                                                    return super().__getitem__(i)
                                            
                                            
                                            class Scope(
                                                schemas.ListSchema
                                            ):
                                            
                                            
                                                class MetaOapg:
                                                    items = schemas.StrSchema
                                            
                                                def __new__(
                                                    cls,
                                                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                                ) -> 'Scope':
                                                    return super().__new__(
                                                        cls,
                                                        _arg,
                                                        _configuration=_configuration,
                                                    )
                                            
                                                def __getitem__(self, i: int) -> MetaOapg.items:
                                                    return super().__getitem__(i)
                                            __annotations__ = {
                                                "Effect": Effect,
                                                "Action": Action,
                                                "Scope": Scope,
                                            }
                                    
                                    Action: MetaOapg.properties.Action
                                    Scope: MetaOapg.properties.Scope
                                    Effect: MetaOapg.properties.Effect
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["Effect"]) -> MetaOapg.properties.Effect: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["Action"]) -> MetaOapg.properties.Action: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["Scope"]) -> MetaOapg.properties.Scope: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                    
                                    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Effect", "Action", "Scope", ], str]):
                                        # dict_instance[name] accessor
                                        return super().__getitem__(name)
                                    
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["Effect"]) -> MetaOapg.properties.Effect: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["Action"]) -> MetaOapg.properties.Action: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["Scope"]) -> MetaOapg.properties.Scope: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                    
                                    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Effect", "Action", "Scope", ], str]):
                                        return super().get_item_oapg(name)
                                    
                                
                                    def __new__(
                                        cls,
                                        *_args: typing.Union[dict, frozendict.frozendict, ],
                                        Action: typing.Union[MetaOapg.properties.Action, list, tuple, ],
                                        Scope: typing.Union[MetaOapg.properties.Scope, list, tuple, ],
                                        Effect: typing.Union[MetaOapg.properties.Effect, str, ],
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                    ) -> 'items':
                                        return super().__new__(
                                            cls,
                                            *_args,
                                            Action=Action,
                                            Scope=Scope,
                                            Effect=Effect,
                                            _configuration=_configuration,
                                            **kwargs,
                                        )
                        
                            def __new__(
                                cls,
                                _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'Statement':
                                return super().__new__(
                                    cls,
                                    _arg,
                                    _configuration=_configuration,
                                )
                        
                            def __getitem__(self, i: int) -> MetaOapg.items:
                                return super().__getitem__(i)
                        __annotations__ = {
                            "Version": Version,
                            "Statement": Statement,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["Version"]) -> MetaOapg.properties.Version: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["Statement"]) -> MetaOapg.properties.Statement: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["Version", "Statement", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["Version"]) -> typing.Union[MetaOapg.properties.Version, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["Statement"]) -> typing.Union[MetaOapg.properties.Statement, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Version", "Statement", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    Version: typing.Union[MetaOapg.properties.Version, str, schemas.Unset] = schemas.unset,
                    Statement: typing.Union[MetaOapg.properties.Statement, list, tuple, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'privilege':
                    return super().__new__(
                        cls,
                        *_args,
                        Version=Version,
                        Statement=Statement,
                        _configuration=_configuration,
                        **kwargs,
                    )
            id = schemas.StrSchema
            description = schemas.StrSchema
            __annotations__ = {
                "name": name,
                "privilege": privilege,
                "id": id,
                "description": description,
            }
    
    name: MetaOapg.properties.name
    privilege: MetaOapg.properties.privilege
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["privilege"]) -> MetaOapg.properties.privilege: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "privilege", "id", "description", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["privilege"]) -> MetaOapg.properties.privilege: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "privilege", "id", "description", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        privilege: typing.Union[MetaOapg.properties.privilege, dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Privilege':
        return super().__new__(
            cls,
            *_args,
            name=name,
            privilege=privilege,
            id=id,
            description=description,
            _configuration=_configuration,
            **kwargs,
        )
