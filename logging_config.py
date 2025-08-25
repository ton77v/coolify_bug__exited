from typing import Literal
import logging
import os
import sys

from dotenv import load_dotenv


load_dotenv()

# can't use built-in enums since we use it with getattr
LogLevel = Literal["debug", "info", "warning", "error", "exception"]


def setup_external_loggers() -> None:
    # {"topologyId": {"$oid": "67e8c7b8f7cf917bfca73661"}, "message": "Starting topology monitoring"}
    logging.getLogger("pymongo").setLevel(logging.WARNING)  # these two are spammy AF
    logging.getLogger("motor").setLevel(logging.WARNING)


def setup_logging(
    debug_mode: bool = os.environ.get("DEBUG", "False") == "True",
) -> None:
    setup_external_loggers()
    # or use the full config & logging.config
    logging.basicConfig(
        level=logging.DEBUG if debug_mode else logging.INFO,  # like was set in wsgi
        stream=sys.stdout,
        format="[%(filename)s:%(lineno)d] %(levelname)s - %(message)s",
    )