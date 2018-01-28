"""Flask APP."""

from flask import Flask
from flask import render_template
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def index():
    """Handle HTTP GET Request for the home route."""
    return "Echo"

@app.route('/api/v1.0/echo/<term>', methods=['GET'])
def echo(term):
    """Handle HTTP GET Request for the echo API endpoint."""
    return jsonify({'msg': term})