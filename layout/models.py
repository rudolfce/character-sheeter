"""Defines a model for a character sheet layout."""

from sheeter.database import db


class Layout(db.Model):
    """Model for a character sheet layout."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    structure = db.Column(db.JSON())
    field_mapping = db.Column(db.JSON())

    def __repr__(self):
        """Return the string representation."""
        return f'<Layout {self.name}>'
