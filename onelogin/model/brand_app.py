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


class BrandApp(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "auth_method",
            "visible",
            "updated_at",
            "connector_id",
            "name",
            "created_at",
            "description",
            "id",
            "auth_method_description",
        }
        
        class properties:
            id = schemas.IntSchema
            updated_at = schemas.StrSchema
            name = schemas.StrSchema
            connector_id = schemas.IntSchema
            auth_method_description = schemas.StrSchema
            description = schemas.StrSchema
            auth_method = schemas.IntSchema
            created_at = schemas.StrSchema
            visible = schemas.BoolSchema
            __annotations__ = {
                "id": id,
                "updated_at": updated_at,
                "name": name,
                "connector_id": connector_id,
                "auth_method_description": auth_method_description,
                "description": description,
                "auth_method": auth_method,
                "created_at": created_at,
                "visible": visible,
            }
    
    auth_method: MetaOapg.properties.auth_method
    visible: MetaOapg.properties.visible
    updated_at: MetaOapg.properties.updated_at
    connector_id: MetaOapg.properties.connector_id
    name: MetaOapg.properties.name
    created_at: MetaOapg.properties.created_at
    description: MetaOapg.properties.description
    id: MetaOapg.properties.id
    auth_method_description: MetaOapg.properties.auth_method_description
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["connector_id"]) -> MetaOapg.properties.connector_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["auth_method_description"]) -> MetaOapg.properties.auth_method_description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["auth_method"]) -> MetaOapg.properties.auth_method: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["visible"]) -> MetaOapg.properties.visible: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "updated_at", "name", "connector_id", "auth_method_description", "description", "auth_method", "created_at", "visible", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["connector_id"]) -> MetaOapg.properties.connector_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["auth_method_description"]) -> MetaOapg.properties.auth_method_description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["auth_method"]) -> MetaOapg.properties.auth_method: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["visible"]) -> MetaOapg.properties.visible: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "updated_at", "name", "connector_id", "auth_method_description", "description", "auth_method", "created_at", "visible", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        auth_method: typing.Union[MetaOapg.properties.auth_method, decimal.Decimal, int, ],
        visible: typing.Union[MetaOapg.properties.visible, bool, ],
        updated_at: typing.Union[MetaOapg.properties.updated_at, str, ],
        connector_id: typing.Union[MetaOapg.properties.connector_id, decimal.Decimal, int, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        created_at: typing.Union[MetaOapg.properties.created_at, str, ],
        description: typing.Union[MetaOapg.properties.description, str, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        auth_method_description: typing.Union[MetaOapg.properties.auth_method_description, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BrandApp':
        return super().__new__(
            cls,
            *_args,
            auth_method=auth_method,
            visible=visible,
            updated_at=updated_at,
            connector_id=connector_id,
            name=name,
            created_at=created_at,
            description=description,
            id=id,
            auth_method_description=auth_method_description,
            _configuration=_configuration,
            **kwargs,
        )
