from flask import Flask,Blueprint

from .views import main

def create_app(config_file="config.py"):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    app.register_blueprint(main)

    return app