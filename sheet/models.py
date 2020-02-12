"""Defines a model for a character sheet."""

from sheeter.database import db


class Sheet(db.Model):
    """Model for a character sheet."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    layout_id = db.Column(db.Integer, db.ForeignKey('layout.id'))

    # External relationships
    layout = db.relationship('Layout', backref='sheets')

    def __repr__(self):
        """Return the string representation."""
        return f'<Sheet {self.name}>'
