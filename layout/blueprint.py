"""Definition of the character sheet layout main module."""

from flask import Blueprint
from flask_restful import Api

from layout.controllers import LayoutListController, LayoutController


layout_bp = Blueprint('layouts', __name__)
layout_api = Api(layout_bp)
layout_api.add_resource(LayoutListController, '/')
layout_api.add_resource(LayoutController, '/<int:id>')
