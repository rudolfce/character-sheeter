"""Definition of the character sheet main module."""

from flask import Blueprint
from flask_restful import Api

from user.controllers import UserListcontroller, UserController, LoginController


user_bp = Blueprint('users', __name__)
user_api = Api(user_bp)
user_api.add_resource(UserListcontroller, '/')
user_api.add_resource(UserController, '/<int:id>')
user_api.add_resource(LoginController, '/login')
