#!/usr/bin/python3
# Script that starts a Flask web application
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Print Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """print HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_someword(text):
    """function that print c <someword>"""
    return "c {}".format(text.replace("_", " "))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
