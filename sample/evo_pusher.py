"""
Sample Evo API client that pushes streams to another server
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, request
import json
import requests


RTMP_ENDPOINT = "rtmp://10.2.10.51/live"
if len(sys.argv) == 2:
    RTMP_ENDPOINT = sys.argv[1]

from evo import Evo

app = Flask(__name__)

def on_stream(ip, localStreamname):
    server = Evo(ip)
    return server.pushStream(
        uri=RTMP_ENDPOINT,
        keepAlive="1",
        localStreamname=localStreamname)

@app.route("/events", methods = ['POST'])
def on_event():
    data = json.loads(request.data)
    if data["type"] == "inStreamCreated":
        app.logger.info(on_stream(request.remote_addr, data['payload']['name']))
    return "OK"

if __name__ == "__main__":
    print 'Pushing all streams to %s' % RTMP_ENDPOINT
    app.run(host='0.0.0.0', debug=True)
