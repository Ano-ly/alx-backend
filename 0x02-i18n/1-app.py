#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)

app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'


@app.route("/", strict_slashes=False)
def home_page():
    """Render template"""
    return (render_template('1-index.html'))


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')