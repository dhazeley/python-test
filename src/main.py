import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

import logging
from flask import Flask, request
from time import strftime
import traceback
import os

import google.cloud.logging


from recommendation.routes import rec_api
from chat_completion.routes import gpt_api

log_level = os.getenv("LOG_LEVEL", "")
if log_level in ("CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"):
    logging.basicConfig(level=logging.getLevelName(log_level))

if os.getenv("IN_CLOUD", "false").lower() == "true":
    client = google.cloud.logging.Client()
    client.setup_logging()


app = Flask(__name__)


@app.after_request
def after_request(response):
    timestamp = strftime("[%Y-%b-%d %H:%M]")
    logging.info(
        "%s %s %s %s %s %s",
        timestamp,
        request.remote_addr,
        request.method,
        request.scheme,
        request.full_path,
        response.status,
    )
    return response


@app.errorhandler(Exception)
def exceptions(e):
    tb = traceback.format_exc()
    timestamp = strftime("[%Y-%b-%d %H:%M]")
    logging.error(
        "%s %s %s %s %s 5xx INTERNAL SERVER ERROR\n%s",
        timestamp,
        request.remote_addr,
        request.method,
        request.scheme,
        request.full_path,
        tb,
    )
    return e


@app.route("/health")
def hello_world():
    """Health check endpoint.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        Healthy status.
    """
    return "Healthy!"


app.register_blueprint(rec_api)
app.register_blueprint(gpt_api, url_prefix="/gpt")


if __name__ == "__main__":
    debug = my_env = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")
    app.run(debug=debug, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
