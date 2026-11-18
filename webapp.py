# webapp.py

import json
from flask import Flask
from waitress import serve
from streamlink import Streamlink
import traceback

streamlink = Streamlink()

app = Flask(__name__)

@app.route("/twitch.tv/<channel>")
def twitch_channel(channel: str):
    pluginname, pluginclass, resolved_url = streamlink.resolve_url(f"twitch.tv/{channel}")
    plugin = pluginclass(streamlink, resolved_url)
    streams = plugin.streams()
    return {
        "streams": {k: json.loads(v.json) for k, v in streams.items()},
        "metadata": plugin.get_metadata(),
        "plugin": pluginname
    }

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
