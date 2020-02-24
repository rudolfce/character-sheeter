"""Common operations on API controllers."""

from flask import request
from flask_restful import Resource

# Must find a clean way to avoid import db from here
from sheeter.database import db


class BaseListController(Resource):
    """
    Base controller for a list of entries.

    This class should be used as base for controller classes to serve the main route for every
    model. Methods standardized here include:
    - get: method to return a list of objects of the desired class
    - post: method to create a new object of the desired class
    """

    Model = None
    Serializer = None

    def get(self):
        """Return serialized data from the underlying model as a list of objects."""
        serializer = self.Serializer(many=True)
        objects = self.Model.query.all()

        return serializer.dump(objects)

    def post(self):
        """Creates a new entry from deserialized data."""
        serializer = self.Serializer()

        args = request.get_json()
        instance = serializer.load(args)

        db.session.add(instance)
        db.session.commit()

        return serializer.dump(instance)


class BaseGetController(Resource):
    """
    Base controller to a object detail visualization.

    This class should be used to visualize single entities in detail. Methods defined here include:
    - get: method to retrieve a given object of the desired class
    - put (TODO): method to update a given object of the desired class
    - delete (TODO): method do remove from database a given object of the desired class
    """

    Model = None
    Serializer = None

    def get(self, id):
        """Return serialized data from the underlying model as a single detailed object."""
        serializer = self.Serializer()

        entry = self.Model.query.get(id)

        return serializer.dump(entry)
