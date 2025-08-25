import logging
import os

from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

from app import create_app
from logging_config import setup_logging


def create_wsgi_app() -> Flask:
    debug_mode = os.environ.get("FLASK_DEBUG") == "1"

    setup_logging(debug_mode=debug_mode)
    logger = logging.getLogger(__name__)

    flask_app = create_app()
    flask_app.wsgi_app = ProxyFix(
        flask_app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_port=1, x_prefix=1
    )

    logger.info("🏎️ WSGI app started")

    return flask_app
