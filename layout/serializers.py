"""Defines a serializing schema for the Layout model."""

import re
from marshmallow import validates, validates_schema, ValidationError

from sheeter.database import ma
from layout.models import Layout


class LayoutStructure(ma.Schema):
    """
    Serializer for the layout's structure.

    This schema is used to validate the layout structure at a fine level.
    """
    name = ma.Str(required=True)
    type_ = ma.Str(data_key='type', required=True)
    contents = ma.Field(required=True)

    valid_names = r'[a-zA-Z_][a-zA-Z0-9_]*'

    def _validate_array(self, contents):
        """Validate array fields."""
        if not (isinstance(contents, list) or isinstance(contents, tuple)):
            raise ValidationError('Array fields must be arrays')

        errors = {}
        for entry in contents:
            try:
                schema = LayoutStructure()
                schema.load(entry)
            except ValidationError as error:
                errors[entry['name']] = str(error)

        if errors:
            raise ValidationError(errors)

    def _validate_integer(self, contents):
        """Validate integer fields."""
        if not isinstance(contents, int):
            raise ValidationError('Invalid data for integer type: {}'.format(contents))

    def _validate_string(self, contents):
        """Validate string fields."""
        if not isinstance(contents, str):
            raise ValidationError('Invalid string input: {}'.format(contents))

    @validates('name')
    def validate_name(self, value):
        """Validate the structure name."""
        if not re.fullmatch(self.valid_names, value):
            raise ValidationError('Not a valid name: {}'.format(value))

    @validates_schema
    def validate_internal_structure(self, data, **kwargs):
        """
        Validate the main internal structure.

        The main structure has the contents validation coupled to the type of the field.
        """
        validations = {
            'integer': self._validate_integer,
            'string': self._validate_string,
            'array': self._validate_array,
        }
        validate = validations.get(data['type_'])

        if not validate:
            raise ValidationError('Unknown type: {}'.format(data['type']))

        validate(data['contents'])


class LayoutSchema(ma.ModelSchema):
    """
    Base schema for the Layout model.

    This serializing schema should be used to return layouts through the API.
    """

    class Meta:
        """LayoutSchema Meta."""

        model = Layout

    structure = ma.Nested('LayoutStructure', required=True)
