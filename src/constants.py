import os


JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "mcKey")
APP_PORT = int(os.environ.get("APP_PORT", "5555"))
DEV_MODE = bool(os.environ.get("DEV_MODE", "True"))