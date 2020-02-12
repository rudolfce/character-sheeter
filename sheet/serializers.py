"""Defines a serializing schema for the Sheet model."""

from sheeter.database import ma
from sheet.models import Sheet


class SheetSchema(ma.ModelSchema):
    """
    Base schema for the Sheet model.

    This serializing schema should be used to return sheets through the API.
    """

    class Meta:
        """SheetSchema Meta."""

        model = Sheet

    layout = ma.Nested('LayoutSchema')
