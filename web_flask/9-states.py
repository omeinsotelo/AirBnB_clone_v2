#!/usr/bin/python3
# Script that starts a Flask web application
from flask import Flask, render_template
from models import storage
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


@app.route('/python', strict_slashes=False)
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


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def isodd_iseven_number(n):
    """Print <integer> is a number"""
    if n % 2 == 0:
        msj = "{} is even".format(n)
        return render_template('6-number_odd_or_even.html', rightmsj=msj)
    msj = "{} is odd".format(n)
    return render_template('6-number_odd_or_even.html', rightmsj=msj)


@app.teardown_appcontext
def remove_session(exc):
    """Remove session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def list_states():
    """list all states"""
    data = storage.all("State")
    return render_template('7-states_list.html', statedata=data)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """list all cities by state"""
    data = []
    data.append(storage.all("State"))
    data.append(storage.all("City"))
    return render_template('8-cities_by_states.html', citystdata=data)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def list_states_id(id=None):
    """List states or a state by id"""
    data = []
    if id is not None:
        for findStates in storage.all("State").values():
            if findStates.id == id:
                data.append({"State": findStates})
                data.append(storage.all("City"))
                return render_template("9-states.html", dicState=data)
        return render_template('9-states.html', dicState=None)

    data.append(storage.all("State"))
    return render_template('9-states.html', dicState=data)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
