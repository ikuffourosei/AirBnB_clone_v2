#!/usr/bin/python3
"""A script tnat starts a Flask Application
"""

from flask import Flask
from flask import render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """a function that returns HBNB
    """
    return "Hello HBNB"


@app.route('/hbnb', strict_slashes=False)
def app_name():
    """a function that returns 'HBNB' """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Displays C followed by value of text
    Replace '_' with a space
    """
    if "_" in text:
        text = text.replace("_", " ")
    return f"C {escape(text)}"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """display “Python ” followed by the value of the text
    replace underscore _ symbols with a space
    """
    if "_" in text:
        text = text.replace("_", " ")
    return f"Python {escape(text)}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Display '<n> is a number' if n is an integer"""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def template_number(n):
    """display a HTML page only if n is an integer
    H1 tag: “Number: n” inside the tag BODY
    """
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
