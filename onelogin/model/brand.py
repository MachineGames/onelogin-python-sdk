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


class Brand(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "custom_label_text_for_login_screen",
            "login_instruction",
            "custom_masking_color",
            "custom_masking_opacity",
            "enabled",
            "mfa_enrollment_message",
            "custom_color",
            "background",
            "custom_support_enabled",
            "enable_custom_label_for_login_screen",
            "hide_onelogin_footer",
            "logo",
            "custom_accent_color",
            "id",
            "login_instruction_title",
        }
        
        class properties:
            id = schemas.IntSchema
            enabled = schemas.BoolSchema
            custom_support_enabled = schemas.BoolSchema
            custom_color = schemas.StrSchema
            custom_accent_color = schemas.StrSchema
            custom_masking_color = schemas.StrSchema
            custom_masking_opacity = schemas.IntSchema
            mfa_enrollment_message = schemas.StrSchema
            enable_custom_label_for_login_screen = schemas.BoolSchema
            custom_label_text_for_login_screen = schemas.StrSchema
            login_instruction = schemas.StrSchema
            login_instruction_title = schemas.StrSchema
            hide_onelogin_footer = schemas.BoolSchema
            
            
            class background(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "urls",
                        "content_type",
                        "updated_at",
                        "file_size",
                    }
                    
                    class properties:
                        
                        
                        class urls(
                            schemas.DictSchema
                        ):
                        
                        
                            class MetaOapg:
                                required = {
                                    "original",
                                    "branding",
                                    "login",
                                }
                                
                                class properties:
                                    original = schemas.StrSchema
                                    login = schemas.StrSchema
                                    branding = schemas.StrSchema
                                    __annotations__ = {
                                        "original": original,
                                        "login": login,
                                        "branding": branding,
                                    }
                            
                            original: MetaOapg.properties.original
                            branding: MetaOapg.properties.branding
                            login: MetaOapg.properties.login
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["original"]) -> MetaOapg.properties.original: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["login"]) -> MetaOapg.properties.login: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["branding"]) -> MetaOapg.properties.branding: ...
                            
                            @typing.overload
                            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                            
                            def __getitem__(self, name: typing.Union[typing_extensions.Literal["original", "login", "branding", ], str]):
                                # dict_instance[name] accessor
                                return super().__getitem__(name)
                            
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["original"]) -> MetaOapg.properties.original: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["login"]) -> MetaOapg.properties.login: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["branding"]) -> MetaOapg.properties.branding: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                            
                            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["original", "login", "branding", ], str]):
                                return super().get_item_oapg(name)
                            
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[dict, frozendict.frozendict, ],
                                original: typing.Union[MetaOapg.properties.original, str, ],
                                branding: typing.Union[MetaOapg.properties.branding, str, ],
                                login: typing.Union[MetaOapg.properties.login, str, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                            ) -> 'urls':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    original=original,
                                    branding=branding,
                                    login=login,
                                    _configuration=_configuration,
                                    **kwargs,
                                )
                        file_size = schemas.IntSchema
                        updated_at = schemas.StrSchema
                        content_type = schemas.StrSchema
                        __annotations__ = {
                            "urls": urls,
                            "file_size": file_size,
                            "updated_at": updated_at,
                            "content_type": content_type,
                        }
                
                urls: MetaOapg.properties.urls
                content_type: MetaOapg.properties.content_type
                updated_at: MetaOapg.properties.updated_at
                file_size: MetaOapg.properties.file_size
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["urls"]) -> MetaOapg.properties.urls: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["file_size"]) -> MetaOapg.properties.file_size: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["content_type"]) -> MetaOapg.properties.content_type: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["urls", "file_size", "updated_at", "content_type", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["urls"]) -> MetaOapg.properties.urls: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["file_size"]) -> MetaOapg.properties.file_size: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["content_type"]) -> MetaOapg.properties.content_type: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["urls", "file_size", "updated_at", "content_type", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    urls: typing.Union[MetaOapg.properties.urls, dict, frozendict.frozendict, ],
                    content_type: typing.Union[MetaOapg.properties.content_type, str, ],
                    updated_at: typing.Union[MetaOapg.properties.updated_at, str, ],
                    file_size: typing.Union[MetaOapg.properties.file_size, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'background':
                    return super().__new__(
                        cls,
                        *_args,
                        urls=urls,
                        content_type=content_type,
                        updated_at=updated_at,
                        file_size=file_size,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class logo(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "urls",
                        "content_type",
                        "updated_at",
                        "file_size",
                    }
                    
                    class properties:
                        
                        
                        class urls(
                            schemas.DictSchema
                        ):
                        
                        
                            class MetaOapg:
                                required = {
                                    "navigation",
                                    "original",
                                    "login",
                                }
                                
                                class properties:
                                    original = schemas.StrSchema
                                    login = schemas.StrSchema
                                    navigation = schemas.StrSchema
                                    __annotations__ = {
                                        "original": original,
                                        "login": login,
                                        "navigation": navigation,
                                    }
                            
                            navigation: MetaOapg.properties.navigation
                            original: MetaOapg.properties.original
                            login: MetaOapg.properties.login
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["original"]) -> MetaOapg.properties.original: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["login"]) -> MetaOapg.properties.login: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["navigation"]) -> MetaOapg.properties.navigation: ...
                            
                            @typing.overload
                            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                            
                            def __getitem__(self, name: typing.Union[typing_extensions.Literal["original", "login", "navigation", ], str]):
                                # dict_instance[name] accessor
                                return super().__getitem__(name)
                            
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["original"]) -> MetaOapg.properties.original: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["login"]) -> MetaOapg.properties.login: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["navigation"]) -> MetaOapg.properties.navigation: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                            
                            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["original", "login", "navigation", ], str]):
                                return super().get_item_oapg(name)
                            
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[dict, frozendict.frozendict, ],
                                navigation: typing.Union[MetaOapg.properties.navigation, str, ],
                                original: typing.Union[MetaOapg.properties.original, str, ],
                                login: typing.Union[MetaOapg.properties.login, str, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                            ) -> 'urls':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    navigation=navigation,
                                    original=original,
                                    login=login,
                                    _configuration=_configuration,
                                    **kwargs,
                                )
                        file_size = schemas.IntSchema
                        updated_at = schemas.StrSchema
                        content_type = schemas.StrSchema
                        __annotations__ = {
                            "urls": urls,
                            "file_size": file_size,
                            "updated_at": updated_at,
                            "content_type": content_type,
                        }
                
                urls: MetaOapg.properties.urls
                content_type: MetaOapg.properties.content_type
                updated_at: MetaOapg.properties.updated_at
                file_size: MetaOapg.properties.file_size
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["urls"]) -> MetaOapg.properties.urls: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["file_size"]) -> MetaOapg.properties.file_size: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["content_type"]) -> MetaOapg.properties.content_type: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["urls", "file_size", "updated_at", "content_type", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["urls"]) -> MetaOapg.properties.urls: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["file_size"]) -> MetaOapg.properties.file_size: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["content_type"]) -> MetaOapg.properties.content_type: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["urls", "file_size", "updated_at", "content_type", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    urls: typing.Union[MetaOapg.properties.urls, dict, frozendict.frozendict, ],
                    content_type: typing.Union[MetaOapg.properties.content_type, str, ],
                    updated_at: typing.Union[MetaOapg.properties.updated_at, str, ],
                    file_size: typing.Union[MetaOapg.properties.file_size, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'logo':
                    return super().__new__(
                        cls,
                        *_args,
                        urls=urls,
                        content_type=content_type,
                        updated_at=updated_at,
                        file_size=file_size,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "id": id,
                "enabled": enabled,
                "custom_support_enabled": custom_support_enabled,
                "custom_color": custom_color,
                "custom_accent_color": custom_accent_color,
                "custom_masking_color": custom_masking_color,
                "custom_masking_opacity": custom_masking_opacity,
                "mfa_enrollment_message": mfa_enrollment_message,
                "enable_custom_label_for_login_screen": enable_custom_label_for_login_screen,
                "custom_label_text_for_login_screen": custom_label_text_for_login_screen,
                "login_instruction": login_instruction,
                "login_instruction_title": login_instruction_title,
                "hide_onelogin_footer": hide_onelogin_footer,
                "background": background,
                "logo": logo,
            }
    
    custom_label_text_for_login_screen: MetaOapg.properties.custom_label_text_for_login_screen
    login_instruction: MetaOapg.properties.login_instruction
    custom_masking_color: MetaOapg.properties.custom_masking_color
    custom_masking_opacity: MetaOapg.properties.custom_masking_opacity
    enabled: MetaOapg.properties.enabled
    mfa_enrollment_message: MetaOapg.properties.mfa_enrollment_message
    custom_color: MetaOapg.properties.custom_color
    background: MetaOapg.properties.background
    custom_support_enabled: MetaOapg.properties.custom_support_enabled
    enable_custom_label_for_login_screen: MetaOapg.properties.enable_custom_label_for_login_screen
    hide_onelogin_footer: MetaOapg.properties.hide_onelogin_footer
    logo: MetaOapg.properties.logo
    custom_accent_color: MetaOapg.properties.custom_accent_color
    id: MetaOapg.properties.id
    login_instruction_title: MetaOapg.properties.login_instruction_title
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enabled"]) -> MetaOapg.properties.enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom_support_enabled"]) -> MetaOapg.properties.custom_support_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom_color"]) -> MetaOapg.properties.custom_color: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom_accent_color"]) -> MetaOapg.properties.custom_accent_color: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom_masking_color"]) -> MetaOapg.properties.custom_masking_color: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom_masking_opacity"]) -> MetaOapg.properties.custom_masking_opacity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mfa_enrollment_message"]) -> MetaOapg.properties.mfa_enrollment_message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_custom_label_for_login_screen"]) -> MetaOapg.properties.enable_custom_label_for_login_screen: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom_label_text_for_login_screen"]) -> MetaOapg.properties.custom_label_text_for_login_screen: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["login_instruction"]) -> MetaOapg.properties.login_instruction: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["login_instruction_title"]) -> MetaOapg.properties.login_instruction_title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hide_onelogin_footer"]) -> MetaOapg.properties.hide_onelogin_footer: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["background"]) -> MetaOapg.properties.background: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["logo"]) -> MetaOapg.properties.logo: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "enabled", "custom_support_enabled", "custom_color", "custom_accent_color", "custom_masking_color", "custom_masking_opacity", "mfa_enrollment_message", "enable_custom_label_for_login_screen", "custom_label_text_for_login_screen", "login_instruction", "login_instruction_title", "hide_onelogin_footer", "background", "logo", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enabled"]) -> MetaOapg.properties.enabled: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom_support_enabled"]) -> MetaOapg.properties.custom_support_enabled: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom_color"]) -> MetaOapg.properties.custom_color: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom_accent_color"]) -> MetaOapg.properties.custom_accent_color: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom_masking_color"]) -> MetaOapg.properties.custom_masking_color: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom_masking_opacity"]) -> MetaOapg.properties.custom_masking_opacity: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mfa_enrollment_message"]) -> MetaOapg.properties.mfa_enrollment_message: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_custom_label_for_login_screen"]) -> MetaOapg.properties.enable_custom_label_for_login_screen: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom_label_text_for_login_screen"]) -> MetaOapg.properties.custom_label_text_for_login_screen: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["login_instruction"]) -> MetaOapg.properties.login_instruction: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["login_instruction_title"]) -> MetaOapg.properties.login_instruction_title: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hide_onelogin_footer"]) -> MetaOapg.properties.hide_onelogin_footer: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["background"]) -> MetaOapg.properties.background: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["logo"]) -> MetaOapg.properties.logo: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "enabled", "custom_support_enabled", "custom_color", "custom_accent_color", "custom_masking_color", "custom_masking_opacity", "mfa_enrollment_message", "enable_custom_label_for_login_screen", "custom_label_text_for_login_screen", "login_instruction", "login_instruction_title", "hide_onelogin_footer", "background", "logo", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        custom_label_text_for_login_screen: typing.Union[MetaOapg.properties.custom_label_text_for_login_screen, str, ],
        login_instruction: typing.Union[MetaOapg.properties.login_instruction, str, ],
        custom_masking_color: typing.Union[MetaOapg.properties.custom_masking_color, str, ],
        custom_masking_opacity: typing.Union[MetaOapg.properties.custom_masking_opacity, decimal.Decimal, int, ],
        enabled: typing.Union[MetaOapg.properties.enabled, bool, ],
        mfa_enrollment_message: typing.Union[MetaOapg.properties.mfa_enrollment_message, str, ],
        custom_color: typing.Union[MetaOapg.properties.custom_color, str, ],
        background: typing.Union[MetaOapg.properties.background, dict, frozendict.frozendict, ],
        custom_support_enabled: typing.Union[MetaOapg.properties.custom_support_enabled, bool, ],
        enable_custom_label_for_login_screen: typing.Union[MetaOapg.properties.enable_custom_label_for_login_screen, bool, ],
        hide_onelogin_footer: typing.Union[MetaOapg.properties.hide_onelogin_footer, bool, ],
        logo: typing.Union[MetaOapg.properties.logo, dict, frozendict.frozendict, ],
        custom_accent_color: typing.Union[MetaOapg.properties.custom_accent_color, str, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        login_instruction_title: typing.Union[MetaOapg.properties.login_instruction_title, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Brand':
        return super().__new__(
            cls,
            *_args,
            custom_label_text_for_login_screen=custom_label_text_for_login_screen,
            login_instruction=login_instruction,
            custom_masking_color=custom_masking_color,
            custom_masking_opacity=custom_masking_opacity,
            enabled=enabled,
            mfa_enrollment_message=mfa_enrollment_message,
            custom_color=custom_color,
            background=background,
            custom_support_enabled=custom_support_enabled,
            enable_custom_label_for_login_screen=enable_custom_label_for_login_screen,
            hide_onelogin_footer=hide_onelogin_footer,
            logo=logo,
            custom_accent_color=custom_accent_color,
            id=id,
            login_instruction_title=login_instruction_title,
            _configuration=_configuration,
            **kwargs,
        )
