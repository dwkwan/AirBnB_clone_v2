#!/usr/bin/python3
"""This module starts a Flask web application and display HBNB"""
from flask import Flask
app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hello_world():
    return 'HBNB'


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'
app.run(host='0.0.0.0', port=5000)
