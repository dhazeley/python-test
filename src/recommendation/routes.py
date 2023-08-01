from flask import Blueprint

rec_api = Blueprint("rec_api", __name__)


@rec_api.route("/recommend", methods=["POST"])
def recommendWithoutTraining():
    """Responds to HTTP request for products recommendation.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The products/services recommendation.
    """

    return "REC Healthy!"
