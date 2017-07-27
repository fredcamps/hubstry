from flask import Flask, jsonify, render_template
from .settings import Conf


def create_app():
    app = Flask(__name__,
                static_folder='./static',
                template_folder='./templates',
                static_url_path='/static')

    app.config.from_object(Conf.Flask)

    return app


app = create_app()


@app.route('/healthcheck')
def healthcheck():
    return jsonify({'status': 200, 'message': 'is alive'})


@app.route('/')
def home():
    return render_template('home.jinja2', data={})
