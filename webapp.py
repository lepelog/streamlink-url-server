# webapp.py

import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
from streamlink import Streamlink

streamlink = Streamlink()

class WebRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        url = urlparse(self.path)
        path = url.path.lstrip('/')
        if not path.startswith('twitch.tv/'):
            self.send_error(404)
            return
        try:
            _pluginname, pluginclass, resolved_url = streamlink.resolve_url(url)
            plugin = pluginclass(streamlink, resolved_url, options)
            streams = plugin.streams()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({
                "streams": {k: json.loads(v.json) for k, v in streams.items()},
                "metadata": plugin.get_metadata()
            }).encode("utf-8"))
        except Exception as e:
            self.send_error(400, f"Error: {e}")
            return

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), WebRequestHandler)
    server.serve_forever()
