#!/usr/bin/python3
# Script that starts a Flask web application
from flask import Flask, render_template
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
    return "c {}".format(text.replace("_", " "))


@app.route('/python/<text>', strict_slashes=False)
def python_someword(text="is cool"):
    """Print python <someword>"""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def n_number(n):
    """Print <n> is a number"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def template_hn(n):
    """Set number in H1"""
    return render_template('5-number.html', myh=n)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
