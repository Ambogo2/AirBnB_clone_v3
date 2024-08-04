#!/usr/bin/python3
"""Returns a json response"""

from flask import jsonify
from api.v1.views import app_views
from models import storage
