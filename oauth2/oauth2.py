import urllib.request
from jose import jwt
import logging
import os
import re
import json


class OAuth2:

    def __init__(self, certificate=None, certificateUrl=None, audience=None):
        self.certificate = certificate
        self.certificateUrl = certificateUrl
        self.audience = audience

    def authorize(self, request, securityConfiguration):

        # path to validate, allows health endpoint
        path = request.path
        if path.endswith('/health'):
            return

        # group associated with the security configuration
        groups = None
        for key, value in securityConfiguration.items():
            p = re.compile(key)
            if p.match(path):
                logging.debug('path: ' + path + ', matched: ' +
                              key + ', groups: ' + str(value))
                groups = value
                break
        if groups is None:
            raise Exception(
                'No matchers in secuirty configuration for path: ' + path)

        # allow all group to bypass need for security         
        if any('ALLOW_ALL' in s for s in groups):
            logging.debug('ALLOW_ALL matched: ' + path)
            return
        try:
            token = request.headers['Authorization'].replace(
                'Bearer', '').strip()
        except Exception:
            raise Exception(
                'Unable to read JWT Bearer token from Authorization header')

        # certificate used to validate the token
        if self.certificate is None:
            self.certificate = json.loads(urllib.request.urlopen(
                self.certificateUrl).read().decode('utf-8'))
            logging.debug('Certificate recieved from the server: ' +
                          json.dumps(self.certificate))
        authorizations = jwt.decode(
            token, self.certificate, audience=self.audience)
        scopes = authorizations['scp']
        logging.debug('Groups for authorization: ' + str(groups))
        logging.debug('Scopes for authorization: ' + str(scopes))
        
        # checks to make sure a group is in the token scope
        if len(set(groups).intersection(set(scopes))) < 1:
            raise Exception('No matching scopres on JWT Bearer Token')
