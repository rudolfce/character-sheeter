"""Defines controllers concerned with sheets."""

from sqlalchemy.inspection import inspect
from marshmallow import ValidationError

from common.controllers import BaseListController, BaseGetController
from sheet.validator import SheetValidator
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

    def _validate_data(self, instance):
        """Validate sheet data with layout data."""
        relationships = inspect(Sheet).relationships
        Layout = relationships.get('layout').mapper.class_
        layout = Layout.query.get(instance.layout_id)

        validator = SheetValidator(layout)

        errors = validator.validate(instance)
        if errors:
            raise ValidationError(errors)


class SheetController(BaseGetController):
    """
    Single sheet.

    This route serves as base for a single detailed character sheet
    """

    Model = Sheet
    Serializer = SheetSchema
