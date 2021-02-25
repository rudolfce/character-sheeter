"""Implements a login manager and an user loader to control a session."""

from flask_login import LoginManager

from user.models import User


login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    """Load a user from its id"""
    return User.query.get(user_id)
