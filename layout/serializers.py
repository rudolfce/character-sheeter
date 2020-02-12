"""Defines a serializing schema for the Layout model."""

from sheeter.database import ma
from layout.models import Layout


class LayoutSchema(ma.ModelSchema):
    """
    Base schema for the Layout model.

    This serializing schema should be used to return layouts through the API.
    """

    class Meta:
        """LayoutSchema Meta."""

        model = Layout
