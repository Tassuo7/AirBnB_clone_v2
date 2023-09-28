#!/usr/bin/python3
"""
Write a script that
Start a Flask web application
Your web application must be listening on 0.0.0.0, port 5000
You must use storage for fetching data from the storage engine
You must use the option strict_slashes=False in your route definition
"""

from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display a HTML page with list of states listed alphabeticaly"""
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception=None):
    """Close the storage or remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
