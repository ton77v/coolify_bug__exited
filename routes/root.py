from flask import Blueprint


root_router = Blueprint("root", __name__)


@root_router.route("/")
def index() -> tuple[str, int]:
    return "<html><body>Hello, world!</body></html>", 200