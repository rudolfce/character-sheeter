"""Main settings for the Character Sheeter project."""

from decouple import config


SQLALCHEMY_DATABASE_URI = config('SQLALCHEMY_DATABASE_URI', default='sqlite:////tmp/test.db')
SQLALCHEMY_TRACK_MODIFICATIONS = config('SQLALCHEMY_TRACK_MODIFICATIONS', default=False, cast=bool)
SECRET_KEY = config('SECRET_KEY', default='dummy')
