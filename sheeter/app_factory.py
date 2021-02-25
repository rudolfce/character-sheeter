"""Implements the base app of the Character Sheeter."""

from flask import Flask

from sheeter.database import db, ma, migrate
from sheeter.login_manager import login_manager

from layout.blueprint import layout_bp
from sheet.blueprint import sheet_bp
from user.blueprint import user_bp


def create_app():
    """
    Create a Character Sheeter app.

    The Character Sheeter app currently relies on two sub-apps:
    - layout: a character sheet layout, that serves as a base for a character sheet construction
    - sheet: a character sheet, containing data that defines a player character
    """
    app = Flask(__name__)

    app.config.from_pyfile('../settings.py')

    app.register_blueprint(layout_bp, url_prefix='/layouts')
    app.register_blueprint(sheet_bp, url_prefix='/sheets')
    app.register_blueprint(user_bp, url_prefix='/users')

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app)
    login_manager.init_app(app)

    return app
