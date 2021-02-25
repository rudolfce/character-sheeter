"""Defines a serializing schema for the Sheet model."""

from sheeter.database import ma
from user.models import User


class UserSchema(ma.ModelSchema):
    """
    Base schema for the User model.

    This serializing schema should be used to return users through the API.
    """

    class Meta:
        """SheetSchema Meta."""

        model = User


class LoginSchema(ma.Schema):
    login = ma.Str(required=True)
    password = ma.Str(required=True)
