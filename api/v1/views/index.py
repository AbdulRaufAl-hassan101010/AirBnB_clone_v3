#!/usr/bin/python3
"""
index page for flask that
displays status and stats
"""
from flask import Flask, jsonify, make_response
from api.v1.views import app_views
from models import storage


@app_views.route('/status')
def getStatus():
    return jsonify({'status': 'OK'})
