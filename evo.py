import base64
import json
import requests
from functools import partial

class Evo(object):
    def __init__(self, host, uri="", port=7777):
        self.host = host
        self.uri = uri
        self.port = port

    def __getattr__(self, attr):
        return partial(self.rpc, method=attr)

    def rpc(self, method, **kwargs):
        args = ' '.join("{key}={value}".format(key=key, value=value) for key, value in kwargs.items())
        url = "http://{host}:{port}{uri}/{method}?params={params}".format(
            host=self.host,
            uri=self.uri,
            port=self.port,
            method=method,
            params=base64.b64encode(args)
        )
        response = requests.get(url)
        return response.json()
