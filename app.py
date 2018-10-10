from flask import Flask, abort, request, Response
import json
import os
import logging
from oauth2.oauth2 import OAuth2

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

securityConfig = {
    '.*': ['test']
}

oauth2 = OAuth2(
    certificateUrl='https://dev-729044.oktapreview.com/oauth2/default/v1/keys',  audience='python')


@app.before_request
def before_app_request():
    """filter each request for a token based on security configuration
    """
    try:
        oauth2.authorize(request, securityConfig)
    except Exception as err:
        logging.error(err)
        abort(403)


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
