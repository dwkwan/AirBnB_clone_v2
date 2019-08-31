#!/usr/bin/python3
"""This module starts a Flask web application and display Hello HBNB! """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    return 'Hello HBNB!'
app.run(host='0.0.0.0', port=5000)