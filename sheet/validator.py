"""Defines a sheet validator that compares sheet_data with expected layout_structure"""

import json


class SheetValidator:
    """A sheet validator"""
    def __init__(self, layout):
        self.structure = layout.structure

    def get_structure_value(self, structure, structure_key):
        for entry in structure['contents']:
            if entry['name'] == structure_key:
                return entry
        else:
            raise KeyError(structure_key)

    def type_validate(self, value, structure_value):
        expected_type = structure_value['type']

        if expected_type == 'integer':
            assert isinstance(value, int)
        elif expected_type == 'string':
            assert isinstance(value, str)

    def validate(self, instance):
        """Perform a validation."""
        data = json.loads(instance.sheet_data)

        if not data:
            return ['No data to be validated']

        errors = []

        for key, value in data.items():
            hierarchy = key.split('.')

            structure_value = self.structure

            for structure_key in hierarchy:
                try:
                    structure_value = self.get_structure_value(structure_value, structure_key)
                except KeyError:
                    errors.append('{0}: invalid key'.format(key))
                    break
            else:
                try:
                    self.type_validate(value, structure_value)
                except AssertionError:
                    errors.append(
                        '{0}: invalid value for {1} ({2})'.format(value, structure_value, key)
                    )

        return errors
