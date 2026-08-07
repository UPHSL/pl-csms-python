"""Development entry point for the CSMS Flask application."""

from csms import create_app


def main() -> None:
    """Run the development web server."""
    application = create_app()
    application.run(host="127.0.0.1", port=5000, debug=True)


if __name__ == "__main__":
    main()