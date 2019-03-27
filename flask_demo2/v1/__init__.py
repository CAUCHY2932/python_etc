from flask import Flask


def register_blueprints(app):
    from v1.views import api
    app.register_blueprint(api)


def create_app():
    app = Flask(__name__)
    register_blueprints(app)

    return app




