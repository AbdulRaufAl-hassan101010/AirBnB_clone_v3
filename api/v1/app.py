#!/usr/bin/python3
""" api setup for AirBnB """
from flask import Flask, abort, make_response, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})
app.register_blueprint(app_views)
app.url_map.strict_slashes = False


@app.errorhandler(404)
def handle_404_error(e):
    response = jsonify({'error': 'Not found'})
    response.status_code = 404
    return response

@app.teardown_appcontext
def close(exception=None):
    """
     Function closes the current session
    """
    storage.close()



if __name__ == "__main__":
    apiHost = getenv("HBNB_API_HOST", default="0.0.0.0")
    apiPort = getenv("HBNB_API_PORT", default=5000)
    app.run(host=apiHost, port=int(apiPort), threaded=True)
