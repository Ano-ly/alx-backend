#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Class config for babel"""
    LANGUAGES = ["en", "fr"]


app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Get_locale function"""
    req_lang = request.args.get("locale")
    if req_lang in app.config['LANGUAGES']:
        return (req_lang)
    else:
        return (request.accept_languages.best_match(app.config['LANGUAGES']))


def get_user():
    """Get user dictionary"""
    user = request.args.get('login_as')
    if user is None or user not in users.keys():
        return (None)
    else:
        user = int(user)
        for item in users.keys():
            if item == user:
                return (users[item]["name"])


@app.before_request
def before_request():
    user = get_user()
    g.user = user


app.config.from_object(Config)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'


@app.route("/", strict_slashes=False)
def home_page():
    """Render template"""
    return (render_template('5-index.html', username=g.user))


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')