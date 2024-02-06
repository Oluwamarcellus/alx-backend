#!/usr/bin/env python3
"""
Task 2 module
"""
from flask_babel import Babel
from flask import Flask, render_template, request


class Config:
    """
    Flask Babel configurations
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Retrieves the locale from user's requiest
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def get_index() -> str:
    """
    Index page
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
