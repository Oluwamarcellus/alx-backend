#!/usr/bin/env python3
"""
0-app task module
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index() -> str:
    """
    basic Flask app that simply outputs “Welcome to Holberton” as
    page title (<title>) and “Hello world” as header (<h1>)
    """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run()
