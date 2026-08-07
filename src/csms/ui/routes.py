"""Web routes for the CSMS user interface."""

from flask import Blueprint, current_app, jsonify, render_template

main_blueprint = Blueprint("main", __name__)


@main_blueprint.get("/")
def index() -> str:
    """Display the Sprint 0 welcome page."""
    return render_template(
        "index.html",
        application_name=current_app.config["APP_NAME"],
        application_version=current_app.config["APP_VERSION"],
        current_sprint=current_app.config["CURRENT_SPRINT"],
    )


@main_blueprint.get("/health")
def health():
    """Return a simple application health response."""
    return jsonify(
        {
            "application": current_app.config["APP_NAME"],
            "status": "ok",
            "version": current_app.config["APP_VERSION"],
        }
    )