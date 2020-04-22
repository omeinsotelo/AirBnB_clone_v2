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
    """Print HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_someword(text):
    """Print c <someword>"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python/<text>', strict_slashes=False)
def python_someword(text="is cool"):
    """Print python <someword>"""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def n_number(n):
    """Print <n> is a number"""
    return "{} is a number".format(n)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
