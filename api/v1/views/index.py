#!/usr/bin/python3
"""creates flask app app_views"""

from api.v1.views import app_views
from flask import jsonify
from models import storage

@app_views.route('/status')
def api_status():
    """returns status code"""
    response = {'status': 'OK'}
    return jsonify(response)

@app_views.route('/status', methods =['GET'])
def object_stats():
    """Retrieves the number of object by type"""
    objects = {
        "amenities": storage.count('Amenity'),
        "cities": storage.count('City'),
        "places": storage.count('Place'),
        "reviews": storage.count('Review'),
        "states": storage.count('State'),
        "users": storage.count('User')
    }
    return jsonify(objects)
    