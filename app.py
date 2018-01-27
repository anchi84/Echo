"""Flask APP."""

from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def index():
    """Handle HTTP GET Request for the home route."""
    return "Echo"

@app.route('/api/v1.0/echo', methods=['GET'])
@app.route('/api/v1.0/echo/<msg>', methods=['GET'])
def echo(msg=None):
    """Handle HTTP GET Request for the echo API endpoint."""
    data = {}
    if msg:
        data['msg'] = msg
    elif 'msg' in request.args:
        data['msg'] = request.args['msg']
    else:
        data['msg'] = "Nothing to echo ..."
    return jsonify(data)

@app.after_request
def after_request(response):
   """Tweak response."""
   response.headers.add('Access-Control-Allow-Origin', '*')
   # response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
   # response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
   return response