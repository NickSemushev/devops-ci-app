"""Simple Flask application for DevOps CI."""
from flask import Flask

APP = Flask(__name__)
VERSION = "1.0.0"

@APP.route("/")
def index():
    """Return application version."""
    return f"devops-ci-app version {VERSION}\n"

@APP.route("/health")
def health():
    """Health check endpoint."""
    return "ok\n"

if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=5000)