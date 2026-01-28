"""Enums."""

from __future__ import annotations

from enum import Enum, StrEnum


class Method(StrEnum):
    """Method enum"""

    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"


class Version(Enum):
    """Version enum"""

    V1 = 1
    V2 = 2


class ActionType(StrEnum):
    """ActionType enum"""

    DEFAULT = "default"
    SCENE = "scene"
    DEVICE = "device"


class EffectCategory(StrEnum):
    """EffectCategory enum"""

    NONE = "none"
    DEFAULT = "default_presets"
    CUSTOM = "custom_presets"
