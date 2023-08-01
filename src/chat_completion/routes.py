from flask import Blueprint


gpt_api = Blueprint("gpt_api", __name__)


@gpt_api.route("/health")
def hello_world():
    """Health check endpoint.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        Healthy status.
    """
    return "GPT Healthy!"
