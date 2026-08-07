"""Shared pytest fixtures for the CSMS application."""

import pytest
from flask import Flask
from flask.testing import FlaskClient

from csms import create_app


@pytest.fixture()
def app() -> Flask:
    """Create a configured application for testing."""
    application = create_app(
        {
            "TESTING": True,
            "DEBUG": False,
            "SECRET_KEY": "test-secret-key",
        }
    )

    yield application


@pytest.fixture()
def client(app: Flask) -> FlaskClient:
    """Create a Flask test client."""
    return app.test_client()