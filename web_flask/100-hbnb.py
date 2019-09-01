#!/usr/bin/python3
"""This module starts a Flask web application and displays an integer and if
it is even or odd
"""
from flask import Flask
from flask import escape
from flask import render_template
from models import storage
from models import State
from models import Amenity
from models import Place

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def display_filters():
    state_dict = storage.all(State)
    amenity_dict = storage.all(Amenity)
    place_dict = storage.all(Place)
    return render_template('100-hbnb.html', state_dict=state_dict,
                           amenity_dict=amenity_dict, place_dict=place_dict)


@app.teardown_appcontext
def teardown_db(self):
    storage.close()


app.run(host='0.0.0.0', port=5000)
