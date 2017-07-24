from flask import Flask
from .settings import Conf


def create_app():
    app = Flask(__name__,
                static_folder='./static',
                template_folder='./templates',
                static_url_path='/static')

    app.config.from_object(Conf.Flask)

    return app


app = create_app()
