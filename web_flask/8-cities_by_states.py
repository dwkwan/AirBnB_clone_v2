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


@app.route('/cities_by_states', strict_slashes=False)
def display_cities_by_state():
    state_dict = storage.all(State)
    return render_template('8-cities_by_states.html', state_dict=state_dict)


@app.teardown_appcontext
def teardown_db(self):
    storage.close()

app.run(host='0.0.0.0', port=5000)
