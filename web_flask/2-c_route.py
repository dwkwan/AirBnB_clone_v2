#!/usr/bin/python3
"""This module starts a Flask web application and displays text starting with C
"""
from flask import Flask
from flask import escape
app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hello_world():
    return 'HBNB'


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/c/<text>', strict_slashes=False)
def hello_c(text):
    mod_text = escape(text)
    return 'C %s' % mod_text.replace("_", " ")

app.run(host='0.0.0.0', port=5000)