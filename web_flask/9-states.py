#!/usr/bin/python3
"""This module starts a Flask web application and displays an integer and if
it is even or odd
"""
from flask import Flask
from flask import escape
from flask import render_template
from models import storage
from models import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def display_states_and_cities(id=None):
    state_dict = storage.all(State)
    found = None
    if id is not None:
        for state in state_dict.values():
            if state.id == id:
                found = state

    return render_template('9-states.html', state_dict=state_dict, id=id,
                           found=found)


@app.teardown_appcontext
def teardown_db(self):
    storage.close()

app.run(host='0.0.0.0', port=5000)
