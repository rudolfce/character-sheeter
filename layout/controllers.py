"""Defines controllers concerned with sheet layouts."""

from common.controllers import BaseListController, BaseGetController

from layout.models import Layout
from layout.serializers import LayoutSchema


class LayoutListController(BaseListController):
    """
    List of sheet layouts.

    This route serves as base for returning multiple sheet layouts
    """

    Model = Layout
    Serializer = LayoutSchema


class LayoutController(BaseGetController):
    """
    Single sheet layout.

    This route serves as base for returning a single detailed character sheet layout.
    """

    Model = Layout
    Serializer = LayoutSchema
