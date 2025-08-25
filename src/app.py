import logging
import os

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from constants import JWT_SECRET_KEY, APP_PORT, DEV_MODE
from logging_config import setup_logging
from routes.root import root_router


logger = logging.getLogger(__name__)


def create_app() -> Flask:  # our #AppFactory | app factory function
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.json.sort_keys = False

    CORS(app)

    # JWT setup
    app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY
    JWTManager(app)

    # ...

    # routes
    app.register_blueprint(root_router)

    return app


if __name__ == "__main__":
    flask_app = create_app()
    setup_logging(debug_mode=DEV_MODE)
    logger.info(f"Starting app {DEV_MODE=}")
    os.environ["FLASK_DEBUG"] = "1" if DEV_MODE else "0"
    debug_mode = os.environ.get("DEBUG_MODE_LOCALLY", "True") == "True"
    flask_app.run(port=APP_PORT, debug=debug_mode)  # blocking