from flask import Flask, request, make_response, redirect, render_template, session, url_for, flash

from .config import Config

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    #app.register_blueprint(bp)

    return app