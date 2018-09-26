

class OAuth2:

    def __init__(self):
        self.certificate = None
        self.audience = None
        self.certificateUrl = None

    def authorize(self, request, securityConfiguration):

        path = request.path
        if path.endswith('/health'):
            return
        groups = None
        for key, value in securityConfiguration.items():
            p = re.compile(key)
            if p.match(path):
                groups = value
                break
        if groups is None:
            raise Exception('No group matchers in secuirty configuration: ' + path)
        if any('ALLOW_ALL' in s for s in groups):
            return
        try:
            token = request.headers['Authorization'].replace('Bearer', '').strip()
        except Exception:
            raise Exception('Unable to read JWT Bearer token from Authorization header')
        authorizations = jwt.decode(token, self.certificate, audience=self.audience)
        scopes = authorizations['scp']
        if len(set(groups).intersection(set(scopes))) < 1:
            raise Exception('No matching scopres on JWT Bearer Token')