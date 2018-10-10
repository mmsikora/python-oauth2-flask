from flask import Flask, abort, request, Response
import json
import os
import logging
from oauth2.oauth2 import OAuth2

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

@app.route('/health')
def health():
    """default health reponse to show app is up
    """
    logging.debug('health called')
    msg = {'status': 'UP'}
    dat = json.dumps(msg)
    return Response(response=dat, status=200, mimetype='application/json')


@app.route('/hello')
def hello():
    """hello response to test application
    """
    logging.debug('hello called')
    msg = {'message': 'hello'}
    dat = json.dumps(msg)
    return Response(response=dat, status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5001)))
