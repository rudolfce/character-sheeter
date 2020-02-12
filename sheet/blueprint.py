"""Definition of the character sheet main module."""

from flask import Blueprint
from flask_restful import Api

from sheet.controllers import SheetListController, SheetController


sheet_bp = Blueprint('sheets', __name__)
sheet_api = Api(sheet_bp)
sheet_api.add_resource(SheetListController, '/')
sheet_api.add_resource(SheetController, '/<int:id>')
