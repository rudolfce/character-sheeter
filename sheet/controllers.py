"""Defines controllers concerned with sheets."""

from common.controllers import BaseListController, BaseGetController
from sheet.models import Sheet
from sheet.serializers import SheetSchema, SheetInputSchema


class SheetListController(BaseListController):
    """
    List of sheets.

    This route serves as base for returning multiple sheets
    """

    Model = Sheet
    Serializer = SheetSchema
    InputSerializer = SheetInputSchema


class SheetController(BaseGetController):
    """
    Single sheet.

    This route serves as base for a single detailed character sheet
    """

    Model = Sheet
    Serializer = SheetSchema
