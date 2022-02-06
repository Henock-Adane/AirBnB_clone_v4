#!/usr/bin/python3
"""app.py to connect API"""
import os
from flask import Flask, Blueprint, jsonify, make_response
from flask_cors import CORS
from models import storage
from api.vi.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown_appcontext(code):
    """"teardown_appcontext"""
    storage.close


@app.errorhandler(404)
def page_not_found(error):
    """returns error if page not found"""
    return make_response(jsonify({'error': 'Not Found'}), 404)


if __name__ == "__main__":
    app.run(host=os.getenv('HBNB_API_HOST', '0.0.0.0'),
            port=int(os.getenv('HBNB_API_PORT', '5000')))
