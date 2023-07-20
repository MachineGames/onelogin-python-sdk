# coding: utf-8

"""
    OneLogin API

    OpenAPI Specification for OneLogin  # noqa: E501

    The version of the OpenAPI document: 3.1.1
    Generated by: https://openapi-generator.tech
"""

from onelogin.paths.api_1_events_event_id.get import GetEventById
from onelogin.paths.api_1_events_types.get import GetEventTypes
from onelogin.paths.api_1_events.get import GetEvents


class EventsApi(
    GetEventById,
    GetEventTypes,
    GetEvents,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
