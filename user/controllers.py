"""Defines controllers concerned with users."""

import bcrypt
from flask import request
from flask_restful import Resource
from flask_login import login_user
from marshmallow import ValidationError

from sheeter.database import db
from common.controllers import BaseListController, BaseGetController
from user.models import User
from user.serializers import UserSchema, LoginSchema


class UserListcontroller(BaseListController):
    """
    List of users.

    This route serves as base for returning multiple users
    """

    Model = User
    Serializer = UserSchema

    def post(self):
        if self.InputSerializer is None:
            serializer = self.Serializer()
        else:
            serializer = self.InputSerializer()

        args = request.get_json()
        instance = serializer.load(args, session=db.session)

        try:
            self._validate_data(instance)
        except ValidationError as exc:
            return exc.messages, 400

        instance.password = bcrypt.hashpw(
            instance.password.encode('utf-8'), bcrypt.gensalt(),
        ).decode()

        db.session.add(instance)
        db.session.commit()

        return serializer.dump(instance)


class UserController(BaseGetController):
    """
    Single user.

    This route serves as base for a single detailed user
    """

    Model = User
    Serializer = UserSchema


class LoginController(Resource):
    """Defines a route to log the user in."""

    def post(self):
        """Get a user login and password, then validate and login."""
        serializer = LoginSchema()

        args = request.get_json()

        try:
            instance = serializer.from_dict(args)
        except ValidationError as exc:
            return exc.messages, 400

        user = User.query.get(instance.login)
        if user:
            if bcrypt.checkpw(instance.password.encode('utf-8'), user.password.encode('utf-8')):
                user.authenticated = True
                db.session.add(user)
                db.session.commit()
                login_user(user, remember=True)
                return {'success': True, 'message': 'Login successful!', 'user': user.email}

        return {'success': False, 'message': 'Invalid user or password'}
