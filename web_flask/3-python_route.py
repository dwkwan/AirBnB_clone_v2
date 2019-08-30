#!/usr/bin/python3
"""This module starts a Flask web application and displays text starting with
Python
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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hello_python(text="is cool"):
    mod_text = escape(text)
    return 'Python %s' % mod_text.replace("_", " ")

app.run(host='0.0.0.0', port=5000)
