#!/usr/bin/python3
"""This module starts a Flask web application and displays states
"""
from flask import Flask
from flask import escape
from flask import render_template
from models import storage
from models import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def display_states():
    state_dict = storage.all(State)
    return render_template('7-states_list.html', state_dict=state_dict)


@app.teardown_appcontext
def teardown_db(self):
    storage.close()

app.run(host='0.0.0.0', port=5000)
